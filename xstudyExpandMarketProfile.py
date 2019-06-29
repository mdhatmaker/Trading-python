import win32gui
import win32con
import win32api
import pywinauto
from pywinauto import Application
import time
import winsound
from datetime import datetime

print "Position cursor over TPA's and click left mouse button..."
print "(press SPACE BAR when done)"

points = []

while True:
    point = win32gui.GetCursorPos()
    #print point
    #cursor = win32gui.GetCursor()
    #print cursor & win32con.WM_LBUTTONDOWN, cursor & win32con.WM_LBUTTONUP

    # save the mouse coordinates when left-button clicked
    state = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)
    if state == -32767:
        points.append(point)
        print point
        winsound.Beep(880, 200)
    # break SPACE BAR pressed
    #state = win32api.GetAsyncKeyState(win32con.VK_RBUTTON)
    state = win32api.GetAsyncKeyState(win32con.VK_SPACE)
    if state == -32767:
        break
    #print state
    
    time.sleep(.1)

winsound.Beep(440, 500)

# if no points were selected, then exit the app
if len(points) == 0:
    print "No coordinates selected. Exiting..."
    exit()

print "Mouse coordinates collected. Charts will be updated every 30 minutes."

hwnd = win32gui.WindowFromPoint(points[0])
# create the XStudy application using a window handle
app = Application()
app.connect_(handle = hwnd)     # pass the window handle of one of the app's window

point = points[0]
hwnd = win32gui.WindowFromPoint(point)
pt = win32gui.ScreenToClient(hwnd, point)
hw = pywinauto.controls.HwndWrapper.HwndWrapper(hwnd)
#hw.Click(button='right', coords = pt)
#app.PopupMenu.MenuItem("Split All").Click()

# first time through we run the code to ensure all charts start off split
firstTime = True

while True:
    dt = datetime.now()
    # execute this code at the top and bottom of every hour (xx:00 and xx:30)
    if firstTime == True or dt.minute == 0 or dt.minute == 30:
        firstTime = False
        # play a little sound to inform user app is working
        winsound.Beep(440,150)
        winsound.Beep(880,150)
        winsound.Beep(440,150)
        for point in points:
            hwnd = win32gui.WindowFromPoint(point)
            pt = win32gui.ScreenToClient(hwnd, point)
            hw = pywinauto.controls.HwndWrapper.HwndWrapper(hwnd)

            print point, pt
            
            # right-click on the indicator and select Split All from popup menu
            hw.Click(button='right', coords=pt)
            #time.sleep(5)
            app.PopupMenu.MenuItem("Split All").Click()
        # sleep for 60 seconds so we do not check for this minute multiple times
        time.sleep(60)
         
    time.sleep(15)  # retest every minute (60 seconds)
    
