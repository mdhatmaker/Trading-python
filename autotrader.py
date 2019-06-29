from pywinauto import Application

app = Application()
app.connect_(title_re = "Autotrader")

dlg = app.Autotrader.AfxFrameOrView100

notepad = Application()
notepad.connect_(title_re = ".*Notepad$")
notedlg = notepad.top_window_()

# move to the upper-left cell of the grid
dlg.TypeKeys("{LEFT 50}{UP 50}")
#dlg.TypeKeys("{DOWN}")

for row in range(7):
    notedlg.TypeKeys("{= 40}{ENTER}")
    for column in range(31):
        dlg.TypeKeys("^c")
        notedlg.TypeKeys("^v{ENTER}")
        dlg.TypeKeys("{RIGHT}") 

    dlg.TypeKeys("{DOWN}")
    dlg.TypeKeys("{LEFT 31}")
    

notedlg.TypeKeys("{= 40}{ENTER}")
