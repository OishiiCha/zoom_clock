import time
from time import strftime
from tkinter import *
import webbrowser

def timed():
    string = strftime('%H:%M:%S %p')
    clock_text.config(text = string)
    clock_text.after(1000, timed)

def enter_data():
    txt_name = id_box.get()
    meeting_id = txt_name.replace(" ", "")
    if len(meeting_id) in (10,11):
        link = "https://pwa.zoom.us/wc/join/" + meeting_id
        error_message = Label(root, bg="skyblue2", fg="black", font=('calibri', 30, 'bold'), justify="center", text="                                                     ")
        error_message.place(x=int(root_w/2), y=int((root_h/5)*4), anchor="center")
        time.sleep(1)
        webbrowser.open(link, 1)
    else:
        error_message = Label(root, bg="skyblue2", fg="black", font=('calibri', 30, 'bold'), justify="center", text="Please enter a valid meeting ID")
        error_message.place(x=int(root_w/2), y=int((root_h/5)*4), anchor="center")

# Geometry
clockw_h = 300
clockw_w = 500
root_h = 300
root_w = 500

# Windows
root = Tk()
root.title("Zoom Web")
root.resizable(width=False, height=False)
root.configure(bg='skyblue2')
root.geometry(str(root_w) + "x" + str(root_h))


clockw = Tk()
clockw.title("Clock")
clockw.resizable(width=False, height=False)
clockw.configure(bg='black')
clockw.geometry(str(clockw_w) + "x" + str(clockw_h))




clock_text = Label(clockw, bg="black", fg="white", font=('calibri', 70, 'bold'))
clock_text.place(x=int(clockw_w/2), y=int(clockw_h/2), anchor="center")

zoom_label = Label(root, text="Enter Zoom ID", bg="skyblue2", fg="black", font=('calibri', 50, 'bold'), justify="center")
zoom_label.place(x=int(root_w/2), y=int((root_h/5)*1), anchor="center")

id_box = Entry(root, bg="white", fg="black", font=('calibri', 30, 'bold'), justify="center")
id_box.place(x=int(root_w/2), y=int((root_h/5)*2), anchor="center")

btn = Button(root, text="Enter", bg="black", fg="black", font=('calibri', 30, 'bold'), justify="center", command=enter_data)
btn.place(x=int(root_w/2), y=int((root_h/5)*3), anchor="center")

timed()
root.mainloop()