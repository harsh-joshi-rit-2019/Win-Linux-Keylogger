Welcome to our keylogger! We are designing a keylogger that works on both Windows and Linux, with support for retrieving the logs off the infected machine. To test the keylogger follow the instructions below.

If testing Linux:
You can use an RLES VM for free through your browser from http://rlesvcloud.rit.edu . Just log in with your RIT credentials and request a deployment. All of the dev testing for the Linux keylogger was done on an ubuntu machine. The creds are student , student
I believe you might have to install python using sudo apt-get install python. 
Navigate to the directory with the files on the terminal and run the keylogger with the command “python keylogger.py”. If any dependency issues occur, install the packages with sudo apt-get install. At the very least you will need to install xlib via the command “sudo apt-get install python-xlib”. Contact Tyler if issues occur.
The keylogger will store its log on the desktop. The file is named file.log. A copy of the log will be sent to a gmail we made whenever the keylogger is run, or every 10 minutes during consecutive execution.
To stopping logging keys type the grave key (`). This should terminate the keylogger as well, if it does not terminate the keylogger just control-C it on the terminal.

If testing Windows:
Python installation required. (https://www.python.org/downloads/)
Check python installation by opening a windows command prompt and typing python, then press enter.
If python is not recognized as a command, follow 
https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/
Open keylogger.py in IDLE
Press F5
Or if your system is configured correctly, you can drag and drop your script from Explorer onto the Command Line window and press enter.
The keylogger will store its log in the User\user1\.py\Logs folder. The file is named key_log.txt. A copy of the log will be sent to a gmail we made whenever the keylogger is run, or every 10 minutes during consecutive execution.
To end the running keylogger, close the terminal. 

