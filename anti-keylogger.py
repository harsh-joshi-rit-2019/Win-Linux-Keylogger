import psutil
import os


# loop through running processes to check for potential keyloggers
def scan_processes():
    for proc in psutil.process_iter():
        # make sure process is still running before trying to get info about it
        if proc.is_running():
            try:
                name = ' '.join(proc.cmdline())
                # get name of each process and check for ones containing keywords
                if "keylog" in name or "hook" in name:
                    print("Potentially harmful process found!")
                    print("Would you like to kill the process: {}?".format(name))
                    stop = raw_input("Type y for yes or n for no.\n")

                    # user allows process to continue running
                    if stop == "n":
                        print("OK, process will not be killed.\n")
                    # user wants to kill process
                    elif stop == "y":
                        print("OK, process will be killed.")
                        try:
                            proc.kill()
                            print("Process successfully killed.\n")
                        # process was stopped before user responded
                        except psutil.NoSuchProcess:
                            print("Process does not exist!\n")
                    else:
                        print("Invalid response.")
            except psutil.AccessDenied:
                continue


# loop through files on machine to check for potential keylogger scripts and log files
def scan_files():
    # get home directory for current user
    homedir = os.path.expanduser('~')

    for subdir, dirs, files in os.walk(homedir):
        for f in files:
            # check name of each fir and check for ones containing keywords
            if "keylog" in f or "key_log" in f or "file.log" in f:
                print("Potentially harmful file found!")
                print("Would you like to delete the file: {}?".format(f))
                delete = raw_input("Type y for yes or n for no.\n")

                # user allows file to stay on system
                if delete == "n":
                    print("OK, file will not be deleted.\n")
                # user wants to delete file
                elif delete == "y":
                    print("OK, file will be deleted.")
                    try:
                        os.remove(f)
                        print("File successfully deleted.\n")
                    # file was deleted before user responded
                    except OSError:
                        print("File does not exist!\n")
                else:
                    print("Invalid response.")


# scan running processes and files to check for potential keylogger malware
if __name__ == '__main__':
    scan_processes()
    scan_files()
