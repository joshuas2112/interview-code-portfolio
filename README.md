# interview-code-portfolio
Store code for interview
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

## file_searcher
I was unsure whether to include this, as it's only a basic framework and I haven't tried fleshing it out. However, I've included it as additional evidence.
The program searches a file for 
