# interview-code-portfolio
Store code for interview

MAKE SURE TO CD INTO EACH DIRECTORY BEFORE RUNNING (eg 'cd file_mover' before running it)

Much of this code is quite poorly documented, but I'm working on trying to make it clearer with more comments. 
I coded all of these on windows, but I've tested them on Fedora Linux 37, with python 3.11.1. They mostly work on linux, but some features don't, so I would RECOMMEND USING WINDOWS. 
If I remember correctly, all of this is my own work, done without tutorials (I had previously learnt python online), though obviously I used the python docs, etc.

## file_mover
In short, file_mover checks for files in from_folder, and moves them to destination. 

WINDOWS ONLY: It will automatically change the name of a file if a file of the same name already exists in the destination foler. (eg if destination contained a file called text.txt, and the program tried to move another text.txt file to the destination folder, the file would be renamed as "text (1).txt". This repeats, changing the number until it finds one that isn't taken (eg "text (2).txt", etc.) To test this, try pasting the same file into from_folder several times, waiting briefly in between until it has been moved). - this doesn't work on linux becuase it requires on an error being thrown if files have the same name. In linux, the file is silently replaced instead of throwing an error. Therefore, I recommend using windows to test these. 

Some of the code for this may appear redundant or useless. This is for two reasons. First, it was programmed relatively quickly, and I only did a single draft (I didn't think much about how I could write it differently, though I can see different ways now). Second, I had originally intended it to be used on the downloads folder, and sort files into other folders (eg photos, installers, etc.), though I never implemented this functionality (mostly becuase I didn't want to lose any files due to bugs). This meant that some of the code may have been designed so I could use parts to determine the type of file. 
When programming with this, I was experimenting with OOP. Admittedly, I've not used it much since (I tend to use functions-based, just because it's easier for small projects), but it was a fun experiment. 

### NOTES:
There is a .placeholder file in file_mover/from_folder and file_mover/destination. If these cause errors they can be deleted. 

Should be run on WINDOWS

## file_searcher
I was unsure whether to include this, as it's only a basic framework and I haven't tried fleshing it out. However, I've included it as additional evidence.
The program searches a file for the search term, then prints the next `output_length` characters on that line after the search term. 

Empty search terms print the whole file

The search file defaults to the one already there

Show failures will list the line numbers where the search term is not present

## speed_test
A simple typing speed test, which has the user copy out a text of variable length. There are two word lists included in the program, supposedly the top 100 and 200 words (I took them from the internet so they may not be accurate). The program times the amount of time taken to copy the text, and records the number of errors. It then outputs WPM. Correct WPM factors in errors. 

The two words can be changed on line 121 (... word_list_loader("./200_words.txt")). I'm aware I could easily have the user input this, but having it hardcoded saves having to process the input to ensure it's valid, etc. 

## numbers_quiz
This was originally based on a set of "OCR coding challenges" we were given in school, though I expanded slightly on it (if you know the challenges I'm referring to, it was number 39).

For this reason, the program is only slightly funcions-based, as I had originally stored it in a single main.py file with several other challenges, with all the code as a single function. Since then, I have spent some small amount of time splitting it into some functions, but a lot of it would need completely rewriting to convert it entirely to functions. 

This is the most recent of the programs I have put on this repo (I coded it in late 2022). It was originally programmed on replit (at school), so there may be bugs when run on windows but I've at least tested it on fedora linux and I think it runs okay. 

The quiz asks a series of maths questions, then stores them in a dictionary according to the inputted name. This dictionary is pickled so the scores are saved after the program is exited.

Entering "scores()" when asked for your name will print all of the scores.
