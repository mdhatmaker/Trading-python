from pywinauto import application

app = application.Application()
app.connect_(title = "X_TRADER Pro")
app.kill_()
