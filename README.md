**Japanese Level Up Maximum Package Vocabulary Upgrade**
=============================================

# Introduction

[Japanese Level Up (Jalup)](https://web.archive.org/web/20240409124146/https://japaneselevelup.com/) is a Japanese language learning blog and system created by it's founder Adam Shapiro (Adshap). 

Jalup flashcards for Anki feature perfect i(nfo)+1 material reviewed for correctness by native speakers, native audio, and bilingual to monolingual (Japanese in Japanese) transitioning.

The website ran for 11 years from 2011 to 2022 before the announcement that Adam wanted to focus more on family life, and finally closed down in 2024. It was a fantastic resource with a wealth of information, guides, and motivational articles. Although the website is sadly gone, there is a community that still lives on! Join me `@Benzene` in the Jalup discord group [here](https://discord.gg/pCy8WPU)!

The Jalup Anki decks are still available to purchace directly from Adam. Links are in the `#jalup-deck-info` channel of the JALUP Adventurers Discord.

Jalup has partnered with [Nihongo Lessons](https://lessons.nihongo-app.com/) which have a licensed the use of the Jalup decks so that it may continue. It's a neat app with a 'card linking' feature which makes it easy to look up words used in the flashcard, linking back to the card in which it was originally seen. Unfortunately, Nihongo Lessons is an iOS app only, so us PC/Android users have been severely missing out on this powerful tool.

This script aims to solve that problem by upgrading your Japanese Level Up maximum package to include a vocabulary section on your cards. There's also some nice card styling too (light and dark mode). The upgrade allows you to keep all your learning progress even if you have already started. 

Here's an example screenshot in Ankidroid card browser:

<p align="center">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/acf86927-fc8f-411e-b9e1-0ddb2d9ec50e" width=30% alt="Jalup vocabulary upgrade Ankidroid screenshot">
</p>

# Prerequisites 

### Installing Python

This script is written in Python and therefore must be installed to run. The version of Python should work with any version `3.8` or greater. I have tested it with `3.8.19` and `3.12.4`. Here is a super short bullet point guide on how to install Python for Linux and Windows:

**Linux:**

(Linux usually has Python preinstalled)

* Open a terminal and run `sudo apt-get update` (for Ubuntu-based systems) or `sudo yum update` (for RPM-based systems)
* Install Python with `sudo apt-get install python3` (for Ubuntu-based systems) or `sudo yum install python3` (for RPM-based systems)
* Verify installation with `python3 --version`

**Windows:**

* Go to the official Python download page and download the latest version of Python for Windows
* Run the installer and follow the prompts to install Python
* Make sure to select the option to add Python to your PATH during installation
* Verify installation by opening a new Command Prompt or PowerShell and typing `python --version`

### Making a virtual environment

I recommend using `pyenv` to manage Python versions and for making a virtual environment for your projects. Here's a super short guide to installing and using pyenv to create a virtual environment in Linux or Windows:

1. **Installation**:
   - **Linux**:
     - Install dependencies: `sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev`
     - Clone pyenv: `git clone https://github.com/pyenv/pyenv.git ~/.pyenv`
     - Add pyenv to your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`): 
       ```
       echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
       echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
       echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
       ```
     - Restart your shell or run `source ~/.bashrc` to apply the changes.

   - **Windows**:
     - Install pyenv-win: Follow the instructions on the pyenv-win GitHub page: https://github.com/pyenv-win/pyenv-win

2. **Usage**:
   - **Create a virtual environment**:
     - List available Python versions: `pyenv install --list`
     - Install a specific Python version: `pyenv install <version>`
     - Set a local Python version for a directory: `pyenv local <version>`
     - Create a virtual environment: `pyenv virtualenv <version> <env_name>`
     - Activate the virtual environment: `pyenv activate <env_name>`

That's it! You now have a virtual environment set up using pyenv in Linux or Windows.

# Upgrade Steps

Unfortunately, due to the nature in which the Anki decks are supplied (inconsistencies and non-standardised formatting), it's extremely difficult to automate the entire process. There are some important steps that must be carried out manually. All of these steps are critical. Follow exactly.

### Step 0: Backup

**CREATE A BACKUP**. I will not be held responsible for data loss if mistakes are made during this process. Go to **File** > **Export** > **All Decks** and save the file to a safe location.

### Step 1: Import Jalup Files

Existing users: Skip this step if you've already imported and are using Jalup.

New users: Import all the Jalup `.apkg` files into Anki. This will import all the media too. 

### Step 2: Create Jalup Deck

Create a deck called 'Jalup' with the sentence subdecks in ascending order. E.g. 'Jalup::01 Beginner', 'Jalup::02 Intermediate', 'Jalup::03 Intermediate', etc. You will have a total of 7 subdecks. Do not include Kana Conqueror or Kanji Kingdom, etc.

<p align="center">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/1ee330d5-1cd3-4b49-bf1e-9c59b7890251" width=50% alt="Deck naming">
</p>

### Step 3: Move Cards

Move your cards to their corresponding decks.

### Step 4: Create Jalup Note Type

Make a new note type called 'Jalup' and make the following fields. Order is critical! 

1. Sentence
2. Explanation
3. Note
4. Media
5. Sentence Reading
6. Vocabulary

<p align="center">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/7da816be-d6aa-4551-b570-62f17f7356ae" width=50% alt="Create note type">
</p>

### Step 5: Change Note Type

Go to each subdeck and select all cards, change note type to the 'Jalup' note we just made. Take care to map the correct fields.

**IMPORTANT**: Take extra care when changing note type of the master deck. Some cards (I believe it's the first 250 cards, stage 1) use a different note type where there is no 'Notes' field like the other cards, so select these separately when changing note type and pay attention to the field mapping.

<p align="center">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/1d2b2556-4d11-4274-b0db-cd66caf4c53e" width=50% alt="Change note type">
</p>

### Step 7: Edit Card Template

Edit the Front, Back, and CSS Styling of the card. Just overwrite what is there with copy and paste from my templates in this repository.

<p align="center">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/de933e7c-1088-4cef-b132-13a40c2dc087" width=50% alt="Card styling">
</p>

### Step 8: Export Jalup Deck

Export with the following options:
* **Notes in plain text**
* **Include**: Select your Jalup parent deck
  - Note: Subdecks MUST be named sequentially (e.g. 01 Beginner, 02 Intermediate, etc.)
* **Include HTML and media references**
* **Include deck name**
* Leave all other options unchecked

<p align="center">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/dba46b60-6e40-4aae-88c1-eb70f9a0273a" width=50% alt="Deck export">
</p>

### Step 9: Sort Exported File

Unfortunately, despite all that work, the exported file is not in deck order (and for some reason nothing I do in pandas will sort it the way we need!). Open the file, select all, copy, paste into Google sheets, highlight column A, sort column A to Z ascending, save/download file as `.tsv` (tab separated values)

<div style="display: flex; justify-content: center;">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/3f98f3c4-c605-48e7-b788-8a80d7afb1ce" style="width: 45%;" alt="Sort by column A">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/d4a78777-6c69-4d2a-9d97-78f2c87e760a" style="width: 45%;" alt="Download as .tsv">
</div>

### Step 10: Prepare Python Script

Clone this repo with in command prompt or terminal using `git clone https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade.git`, then `cd Jalup_Vocab_Upgrade` to navigate inside the directory. This is when you probably want to use a virtual environment with pyenv. Use a file explorer to move your `.tsv` file into the same folder as this python script. Open `Jalup_Vocab_Upgrade.py` in a text editor and change the string of `input_file` to match your filename. e.g. `input_file = 'myfile.tsv'`

### Step 11: Install Requirements

Activate your virtual environment and install the `requirements.txt`

**Installing Dependencies with `pip`**

**Linux**

* In the terminal, navigate to the directory where `requirements.txt` file is located
* Run the following command: `pip install -r requirements.txt`

**Windows**

* Open a command prompt activate your virtual environment and navigate to the directory where `requirements.txt` file is located
* Run the following command: `pip install -r requirements.txt`

### Step 12: Run Python Script

Run the `Jalup_Vocab_Upgrade.py`. After a minute or so, a new file `myfile_Vocab_Upgrade.txt` will be written.

**Running a `.py` file**

**Linux**
* `python Jalup_Vocab_Upgrade.py` (from the terminal)

**Windows**
* `Jalup_Vocab_Upgrade.py` (from the command prompt)

### Step 13: Import Upgraded File

In Anki, import text file.

**Anki Import Options**

1. **Field separator**: Tab
2. **Allow HTML in fields**: Yes
3. **Notetype**: Jalup
4. **Existing notes**: Update
5. **Match Scope**: Notetype and deck
6. **Field mapping**: Double check that it is correct

<p align="center">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/193ad7df-0159-4c78-a8fe-f4d09b5a6938" width=50% alt="Import to Anki">
</p>

Click Import.

### Step 14: Congratulations!

<p align="center">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/5a2e14a0-96c2-4f3d-a6fc-953993d52d07" width=50% alt="Import to Anki">
</p>
<p align="center">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/61da74c0-a7c5-4a3b-9971-18a1109bf966" width=50% alt="Preview card">
</p>

Congratulations! You should now have a fancy vocab upgrade for your Jalup decks. If anything went wrong, you can restore from backup. You DID backup, right?

# How does it work?

Mecab-python3 is a Python wrapper for the MeCab library, a popular Japanese tokenization and morphological analysis tool. It works by breaking down Japanese text into individual words or morphemes, and then analyzing each morpheme's grammatical features, such as part of speech, reading, and base form.

Here's an example of how mecab-python3 would parse the sentence: 映画の始まりは超面白かった！

```
import MeCab

mecab = MeCab.Tagger()
sentence = "映画の始まりは超面白かった！"
parse_result = mecab.parse(sentence)

print(parse_result)
```

The output would be:
```
映画	エーガ	エイガ	映画	名詞-普通名詞-一般			0,1
の	ノ	ノ	の	助詞-格助詞			
始まり	ハジマリ	ハジマリ	始まり	名詞-普通名詞-一般			0
は	ワ	ハ	は	助詞-係助詞			
超	チョー	チョウ	超	接頭辞			
面白かっ	オモシロカッ	オモシロイ	面白い	形容詞-一般	形容詞	連用形-促音便	4
た	タ	タ	た	助動詞	助動詞-タ	終止形-一般	
！			！	補助記号-句点			
EOS
```
The output of mecab-python3 is a tab-separated table, where each line represents a morpheme, and the columns represent the following information:

1. The original text of the morpheme
2. The reading of the morpheme in katakana
3. The reading of the morpheme in kanji (if applicable)
4. The base form of the morpheme (e.g., 映画, 面白い)
5. The part of speech and grammatical features (e.g., 名詞-普通名詞-一般 for a general noun)
6. Additional information about the morpheme (e.g., 0,1 for the position of the morpheme in the sentence)

The script applies this method to all the text in the card and generates a list of unique words in their base form. It then matches those words to cards where it has been defined previously, then takes that definition and example sentence, and appends it to a new vocabulary field with some HTML formatting that is handled by Anki.

# Limitations

While this method is not foolproof, it has proven to be highly effective in most cases. Its accuracy is largely dependent on MeCab's text parsing and the presentation of definitions on the cards. Fortunately, from the intermediate deck onward, definitions are provided in their base dictionary form, making matches relatively straightforward. However, a significant number of cards in the beginner deck feature definitions that are not in their base form, which, combined with potential discrepancies in MeCab's parsing of certain grammar points, can lead to some omissions. Despite these limitations, the method has demonstrated sufficient accuracy for the majority of cases. Considering the hundreds of hours invested in card linking for the original Jalup app, this approach represents a significant improvement.

# Credits

- [MeCab](http://taku910.github.io/mecab/)
- [mecab-python3](https://github.com/SamuraiT/mecab-python3)
- [ipadic](https://pypi.org/project/ipadic) (I know it's outdated but it was reliable. The other dictionary option `Unidic` kept returning dictionary forms in kanji for words that usually only appear in kana, e.g. ゴミ returns as 塵.)
- Jalup Beginner and Intermediate 'Ultimate Version Update' (no longer available) by Adam which formed the basis of the card styling.
