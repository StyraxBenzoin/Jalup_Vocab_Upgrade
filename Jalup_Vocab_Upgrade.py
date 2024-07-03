#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from pathlib import Path
import re
import MeCab
import ipadic

# This script is to upgrade your Japanese Level Up maximum package to include a vocabulary section on your cards.
# Read the guide at https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade

# Load the file. EDIT TO MATCH YOUR FILENAME.
input_file = "Sorted_Jalup_Max_All_Decks.tsv"

# Make a dataframe from the input file. Skip the first 3 rows as they are tags for Anki. We will add the tags later when writing the output.
df = pd.read_csv(input_file, sep="\t", skiprows=(0, 1, 2), header=None)
df.columns = [
    "Deck Name",
    "Sentence",
    "Explanation",
    "Note",
    "Media",
    "Sentence Reading",
]


# Chasen arguments for MeCab ipadic dictionary.
CHASEN_ARGS = r' -F "%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n"'
CHASEN_ARGS += r' -U "%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n"'

# Initialize MeCab with the IPADIC dictionary
mecab = MeCab.Tagger(ipadic.MECAB_ARGS + CHASEN_ARGS)


def parse_japanese_text(text):
    """Parse Japanese text and return a list of unique dictionary forms in the order they appear, excluding particles."""
    text_str = str(text)  # Convert text to a string
    parsed = mecab.parse(text_str)
    unique_words = []
    seen = set()
    for line in parsed.splitlines():
        if line == "EOS":
            break
        parts = line.split("\t")
        if len(parts) > 3:
            lemma = parts[2]  # Dictionary form (lemma)
            pos = parts[3].split("-")[0]  # Part of speech
            # Exclude particles and punctuation
            if pos not in ["助詞", "記号"] and lemma not in seen:
                # Exlude some more all too common terms that would flood our vocabulary section. We shouldn't need these defined over and over again.
                if lemma not in [
                    "の",
                    "ない",
                    "だ",
                    "いる",
                    "ある",
                ]:  # "います", "あります", '食べる', 'お母さん', '彼'
                    unique_words.append(lemma)
                    seen.add(lemma)
    return unique_words


def extract_keyword(text):
    """Function to extract text before ':' or '：'"""
    if isinstance(text, str):
        match = re.search(r"([^:：]+)", text)
        if match:
            return match.group(1).strip()
    return ""


# Apply the extract_keyword function to the 'Explanation' column and store the result in a new 'Keyword' column
df["Keyword"] = df["Explanation"].apply(extract_keyword)

# Concatonate the sentence and explanation into a single string to parse with MeCab.
df["Text to parse"] = df["Sentence"] + df["Explanation"]


# Make a new column with the example and sentence reading with HTML formatting to be handled by Anki CSS styling.
# We will use this column later when the parsed text is matched to a keyword, the and this HTML formatted definition will be appended to the Vocabulary column.
df["Definition"] = (
    '<div class="vocabulary-definition"><span class="definition">'
    + df["Explanation"]
    + '</span><br><span class="example">ex.  '
    + df["Sentence Reading"]
    + "</span><br></div><br>"
)


# Parse the text in 'Text to parse' and output to 'Parsed Text' column
df["Parsed Text"] = df["Text to parse"].apply(parse_japanese_text)


# Iterate over the list of words in the 'Parsed Text' column and match each with 'Keyword' column, then append the related 'Definition' to 'Vocabulary'
for i, row in df.iterrows():
    definitions = []
    for word in row["Parsed Text"]:
        # Exclude the keyword from the same row
        if word == row["Keyword"]:
            continue
        # Find matching rows in the 'Keyword' column, only considering rows with index < i
        matching_definitions = df.loc[df.index < i, "Definition"][
            df.loc[df.index < i, "Keyword"] == word
        ].tolist()
        definitions.extend(matching_definitions)
    # Concatenate and assign to the 'Vocabulary' column
    df.at[i, "Vocabulary"] = "".join(definitions)


# Drop the unecessary columns we made along the way.
# The remaining columns are in the same order as the Anki note we exported from. [Deck Name, Sentence, Explanation, Note, Media, Sentence Reading, Vocabulary]
df = df.drop(["Keyword", "Text to parse", "Definition", "Parsed Text"], axis=1)


# Make a dataframe with tags to add back in. Anki will read these on import.
df_tags = pd.DataFrame(
    [
        ["#separator:tab", "", "", "", "", "", ""],
        ["#html:true", "", "", "", "", "", ""],
        ["#deck column:1", "", "", "", "", "", ""],
    ],
    columns=df.columns,
)


# Concatonate the dataframes to place the tags first.
df_output = pd.concat([df_tags, df]).reset_index(drop=True)

# Save the file, removing the dataframe headers and index.
output_file = Path(input_file).stem + "_Vocab_Upgrade"
df_output.to_csv(output_file + ".txt", sep="\t", index=False, header=False)
