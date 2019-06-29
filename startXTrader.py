from pywinauto import application
from pywinauto import findwindows

import time

app = application.Application()
app.start_(r"c:\tt\x_trader\bin\x_trader.exe")

#for w in app.windows_(): print w.WindowText(), w.Class()

#app.TTLogin.Wait(wait_for = "exists", timeout = 20, retry_interval = 1)
counter = 0
while True:
    try:
        app.connect_(title = "TT Login", class_name = "#32770")
        break
    except findwindows.WindowNotFoundError:
        time.sleep(1)

    counter = counter + 1
    if counter > 10: break
    
#for w in app.windows_(): print w.WindowText(), w.Class()
app.TTLogin.DrawOutline()
app.TTLogin.Edit2.SetText("12345678")
app.TTLogin.LoginButton.Click()
#app.TTLogin.LoginButton.Click()


