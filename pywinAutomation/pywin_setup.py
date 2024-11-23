import win32api
import win32com.client
import win32gui

# print("windows version: ", win32api.GetVersion())
# print("Computer Name: ", win32api.GetComputerName())
# print("System Metrics: ", win32api.GetSystemMetrics(0))

#win32gui.MessageBox(0,"Hello, Pywin32", "Message Box Demo",1)

def custom_message_box():
    result = win32gui.MessageBox(0,"Is python great?", "Customer question:",1)
    print(result)
    if(result == 1):
        win32gui.MessageBox(0, str(result), "Your Output", 1)

custom_message_box()