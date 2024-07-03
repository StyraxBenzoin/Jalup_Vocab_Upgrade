**Japanese Level Up Maximum Package Vocabulary Upgrade**
=============================================

### Introduction

[Japanese Level Up (Jalup)](https://web.archive.org/web/20240409124146/https://japaneselevelup.com/) is a Japanese language learning system created by it's founder Adam Shapiro (Adshap). 

Jalup flashcards for Anki feature perfect i(nfo)+1 material, native audio, and bilingual to monolingual (Japanese in Japanese) transitioning.

Although the website is sadly gone, there is a community that still lives on! Join me `@Benzene` in the Jalup discord group [here](https://discord.gg/pCy8WPU)!

The Jalup Anki decks are still available to purchace directly from Adam. Links are in the `#jalup-deck-info` channel of the JALUP Adventurers Discord.

Jalup has partnered with [Nihongo Lessons](https://lessons.nihongo-app.com/) as it's new home. It's a neat app with a 'card linking' feature which makes it easy to look up words used in the flashcard, linking back to the card in which it was originally seen. Unfortunately, Nihongo Lessons is an iOS app only, so us PC/Android users have been severely missing out on this powerful tool.

This script aims to solve that problem by upgrading your Japanese Level Up maximum package to include a vocabulary section on your cards. There's also some nice card styling too (light and dark mode). The upgrade allows you to keep all your learning progress even if you have already started. 

Here's an example screenshot in Ankidroid card browser:

<p align="center">
  <img src="https://github.com/StyraxBenzoin/Jalup_Vocab_Upgrade/assets/66492803/acf86927-fc8f-411e-b9e1-0ddb2d9ec50e" width="250" alt="Jalup vocabulary upgrade Ankidroid screenshot">
</p>


# Prerequisites 

This script is written in Python and therefore must be installed to run. Here is a super short bullet point guide on how to install Python for Linux and Windows:

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

# Upgrade Steps

Unfortunately, due to the nature in which the Anki decks are supplied (inconsistencies and non-standardised formatting), it's extremely difficult to automate the entire process. There are some important steps that must be carried out manually. All of these steps are critical. Follow exactly.

### Step 0: Backup

**CREATE A BACKUP**. I will not be held responsible for data loss if mistakes are made during this process. Go to **File** > **Export** > **All Decks** and save the file to a safe location.

### Step 1: Import Jalup Files

New users: Import all the Jalup `.apkg` files into Anki. This will import all the media too. 

Existing users: Skip this step.

### Step 2: Create Jalup Deck

Create a deck called Jalup with subdecks in ascending order. E.g. 'Jalup::01 Beginner', 'Jalup::02 Intermediate', 'Jalup::03 Intermediate', etc.

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

### Step 5: Change Note Type

Go to each subdeck and select all cards, change note type to the 'Jalup' note we just made. Take care to map the correct fields.

**IMPORTANT**: Take extra care when changing note type of the master deck. Some cards (I believe it's the first 250 cards, stage 1) use a different note type where there is no 'Notes' field like the other cards, so select these separately when changing note type and pay attention to the field mapping.

### Step 7: Edit Card Template

Edit the Front, Back, and CSS Styling of the card. Just overwrite what is there with copy and paste from my templates in this repository.

### Step 8: Export Jalup Deck

Export with the following options:
* **Notes in plain text**
* **Include**: Select your Jalup parent deck
  - Note: Subdecks MUST be named sequentially (e.g. 01 Beginner, 02 Intermediate, etc.)
* **Include HTML and media references**
* **Include deck name**
* Leave all other options unchecked

### Step 9: Sort Exported File

Unfortunately, despite all that work, the exported file is not in deck order (and for some reason nothing I do in pandas will sort it the way we need!). Open the file, select all, copy, paste into Google sheets, highlight column A, sort column A to Z ascending, save/download file as `.tsv` (tab separated values)

### Step 10: Prepare Python Script

Place your sorted and saved `.tsv` file in the same folder as this python script. Open `Jalup_Vocab_Upgrade.py` in a text editor and change the string of `input_file` to match your filename. e.g. `input_file = 'myfile.tsv'`

### Step 11: Install Requirements

**Installing Dependencies with `pip`**

**Linux**

* Open a terminal and navigate to the directory where your `requirements.txt` file is located
* Run the following command: `pip install -r requirements.txt`

**Windows**

* Open a command prompt and navigate to the directory where your `requirements.txt` file is located
* Run the following command: `pip install -r requirements.txt`

**Note:** Make sure you have Python and `pip` installed on your system before running this command.

### Step 12: Run Python Script

Run `Jalup_Vocab_Upgrade.py`. After a minute or so, a new file `myfile_Vocab_Upgrade.txt` will be written.

**Running a `.py` file**

**Linux**
* `python Jalup_Vocab_Upgrade.py` (from the terminal)
* `./Jalup_Vocab_Upgrade.py` (if the file is executable and in the current directory)

**Windows**
* `Jalup_Vocab_Upgrade.py` (from the command prompt)
* Double-click the `Jalup_Vocab_Upgrade.py` file (if Python is associated with `.py` files)

### Step 13: Import Upgraded File

In Anki, import text file.

**Anki Import Options**

1. **Field separator**: Tab
2. **Allow HTML in fields**: Yes
3. **Notetype**: Jalup
4. **Existing notes**: Update
5. **Match Scope**: Notetype and deck
6. **Field mapping**: Double check that it is correct

Click Import.

### Step 14: Congratulations!

Congratulations! You should now have a fancy vocab upgrade for your Jalup decks. If anything went wrong, you can restore from backup. You DID backup, right?
