import win32gui
import win32con
import win32api
import pywinauto
from pywinauto import Application
import time
import winsound
from datetime import datetime
import sys

print "Click the left mouse button in the XTrader windows you want to align..."
print "(press SPACE BAR when done)"

# empty list to hold x,y mouse coordinates from each click
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
    sys.exit()

print "Select:"
print "(1) align tops"
print "(2) align bottoms"
print "(3) align lefts"
print "(4) align rights"

# create the XStudy application using a window handle from the first point
hwnd = win32gui.WindowFromPoint(points[0])
app = Application()
app.connect_(handle = hwnd)     # pass the window handle of one of the app's window

# empty list to hold windows and window rects
windows = []

for point in points:
    # get the window handle from the point that was clicked
    hwnd = win32gui.WindowFromPoint(point)
    #pt = win32gui.ScreenToClient(hwnd, point)
    # this is the pywinauto HwndWrapper created using the window handle
    hw = pywinauto.controls.HwndWrapper.HwndWrapper(hwnd)
    # what was clicked could be a control or any type of window, so get
    # the "TopLevelParent" which is the actual "window" we will be moving
    top = hw.TopLevelParent()
    # store this window along with its window rect as a tuple
    windows.append((top, top.Rectangle()))
    
win, rect = windows[0]
# now let the user move around the first window and place it
while True:
    point = win32gui.GetCursorPos()
    win.MoveWindow(x=point[0], y=point[1])

    # exit when left-button clicked
    state = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)
    if state == -32767:
        # update the rect with the new window coordinates
        rect = win.Rectangle()
        print point
        winsound.Beep(880, 200)
        break
    
    time.sleep(.1)

width = rect.right-rect.left
xPos = rect.left + width
for i in range(1,len(windows)):
    w, r = windows[i]
    w.MoveWindow(x=xPos,y=rect.top)
    width = r.right - r.left
    xPos += width

    


    
sys.exit()

