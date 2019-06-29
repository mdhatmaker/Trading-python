import win32gui
import win32con
import win32api
import pywinauto
from pywinauto import Application
import time
import winsound


print "Bring up Microsoft Excel and whatever workbook you want the RTD links in."
print "Select the worksheet cell at the top of a blank column (this app will fill"
print "in the cells in that column with the RTD links which you can then copy/"
print "paste wherever you want in your workbook)."
print ""
print "Position cursor over technical indicator line and click left mouse button"
print "(you may have to click it twice since the first click will put focus on the"
print "chart window)..."
print ""

while True:
    point = win32gui.GetCursorPos()
    #print point
    #cursor = win32gui.GetCursor()
    #print cursor & win32con.WM_LBUTTONDOWN, cursor & win32con.WM_LBUTTONUP
    state = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)
    if state == -32767: break
    #print state
    
    time.sleep(.1)

#print point

hwnd = win32gui.WindowFromPoint(point)
#print hwnd
pt = win32gui.ScreenToClient(hwnd, point)
hw = pywinauto.controls.HwndWrapper.HwndWrapper(hwnd)

#print hw.MenuItems()


rowCount = 30


# connect to Excel
xlapp = Application()
xlapp.connect_(title_re = ".*Microsoft Excel")

# create the XStudy application using a window handle
app = Application()
app.connect_(handle = hwnd)     # pass the window handle of one of the app's window

# play a short sound for each value retrieved
winsound.Beep(880, 200)

# right-click on the indicator
hw.Click(button='right', coords=pt)

# current value
#hw.TypeKeys('l~c', pause=0.5)
app.PopupMenu.MenuItem("Link To Excel->Current Value").Click()
xlapp.top_window_().TypeKeys("^v~")

print "1/"+str(rowCount)

# grab rows (user can discard data if 30 is too much)
for i in range(1, rowCount):
    # play short sound for each value retrieved
    winsound.Beep(880, 200)
    
    # right-click on the indicator
    hw.Click(button='right', coords=pt)

    # previous value
    #hw.TypeKeys('l~p', pause=0.5)
    app.PopupMenu.MenuItem("Link To Excel->Previous Value").Click()

    #linkPrevious = app.window_(title_re = "Link Previous Value")
    #linkPrevious.Wait('exists', timeout = 5)
    #linkPrevious.Edit.SetText("69")

    #app.LinkPreviousValue.Wait('enabled')
    app.LinkPreviousValue.Edit.SetText(str(i))
    app.LinkPreviousValue.OK.Click()
    
    #xlapp.
    xlapp.top_window_().TypeKeys("^v~")
    
    print str(i+1) + "/" +str(rowCount)

# play ending sound
winsound.Beep(880,150)
winsound.Beep(440,150)
winsound.Beep(880,150)

print "Done."
