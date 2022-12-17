import time
from tkinter import *
import cv2
from PIL import Image, ImageTk



class Graphics:
    new_image = None
    def running(self):
        return self.can_run
    def on_closing(self):
        self.can_run = False
    def one(self):
        self.game_mode = 1
        self.drive.config(default="active")
        self.stand.config(default="normal")
    def two(self):
        self.game_mode = 0
        self.drive.config(default="normal")
        self.stand.config(default="active")

    def __init__(self):
        self.game_mode = 0
        self.next_clicked = False
        self.started = False
        self.selected_time = 3
        self.selected_sensitivity = 0
        self.initial_run = False
        self.can_run = True

        self.win = Tk()
        self.win.geometry("1000x430+250+300")
        self.win.resizable(False, False)
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.mode = Canvas(self.win, width=640, height=600)
        self.mode.grid(row=0, column=2)
        self.canvas = Canvas(self.win, width=640, height=600)
        self.canvas.grid(row=0, column=0, rowspan=9)
        self.pad = Canvas(self.win, width=50, height=100)
        self.pad.grid(row=0, rowspan=9, column=1)
        self.canvas2 = Canvas(self.win, width=200, height=100)
        self.canvas2.grid(row=3, column=2)
        self.canvas3 = Canvas(self.win, width=200, height=100)
        self.canvas3.grid(row=1, column=2)
        self.canvas4 = Canvas(self.win, width=200, height=100)
        self.canvas4.grid(row=2, column=2)
        self.text = Label(self.canvas2, text="Wheel not detected", font="Helvetica 14 italic", foreground="red")
        self.text2 = Label(self.canvas2, text="Wheel not upright", font="Helvetica 14 italic", foreground="red")
        self.text3 = Label(self.canvas2, text="Hold the wheel upright in view:", font="Helvetica 14 bold")
        self.pad_text = Canvas(self.canvas2, width=50, height=10)
        self.button = Button(self.canvas2, text='Start', command=self.start)
        self.button["state"] = "disabled"

        self.button_1 = Button(self.canvas3, text='3', command=self.five, default="active")
        self.button_2 = Button(self.canvas3, text='5', command=self.ten)
        self.button_3 = Button(self.canvas3, text='7', command=self.teen)
        self.welcome_text = Label(self.canvas3, text="Please select a switching time:")

        self.drive_text = Label(self.mode, text="Welcome! Select a fwd input type:")
        self.drive = Button(self.mode, text='Automatic', command=self.one)
        self.stand = Button(self.mode, text='Manual', command=self.two, default="active")
        self.drive_text.grid(row=0, column=0, columnspan=2)
        self.drive.grid(row=1, column=0)
        self.stand.grid(row=1, column=1)


        self.Button_1 = Button(self.canvas4, text='low', command=self.high)
        self.Button_2 = Button(self.canvas4, text='normal', command=self.normal)
        self.Button_3 = Button(self.canvas4, text='high', command=self.low)
        self.Text = Label(self.canvas4, text="Please select a sensitivity level:")

        self.welcome_text.grid(row=0, column=0, columnspan=3)
        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)
        self.next_func()

    def get_mode(self):
        return self.game_mode
    def high(self):
        self.selected_sensitivity = 2
        self.then()
        self.Button_1.config(default="active")
        self.Button_2.config(default="normal")
        self.Button_3.config(default="normal")

    def update(self, detected, upright):
        if detected:
            self.text.config(foreground="green", text="Wheel is detected")
        else:
            self.text.config(foreground="red", text="Wheel not detected")
        if upright:
            self.text2.config(foreground="green", text="Wheel is upright")
        else:
            self.text2.config(foreground="red", text="Wheel not upright")
        if not self.initial_run:
            if detected and upright:
                self.button["state"] = "active"
            else:
                self.button["state"] = "disabled"
        self.win.update_idletasks()
        self.win.update()

    def get_start(self):
        return self.started

    def get_sensitivity(self):
        return self.selected_sensitivity

    def upd_img(self, img_orig):
        global new_image
        cv2image = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        new_image = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        self.canvas.create_image(10, 10, anchor=NW, image=new_image)

    def normal(self):
        self.selected_sensitivity = 1
        self.then()
        self.Button_2.config(default="active")
        self.Button_1.config(default="normal")
        self.Button_3.config(default="normal")

    def low(self):
        self.selected_sensitivity = 0
        self.then()
        self.Button_3.config(default="active")
        self.Button_2.config(default="normal")
        self.Button_1.config(default="normal")

    def then(self):
        self.button.grid(row=4, column=0, sticky="we")
        self.text.grid(row=2, column=0, sticky="we")
        self.text2.grid(row=3, column=0, sticky="we")
        self.text3.grid(row=0, column=0, sticky="we")
        self.pad_text.grid(row=1, column=0, sticky="we")

    def next_func(self):
        if not self.next_clicked:
            self.Button_1.grid(row=1, column=0)
            self.Button_2.grid(row=1, column=1)
            self.Button_3.grid(row=1, column=2)
            self.Text.grid(row=0, column=0, columnspan=3)
            self.next_clicked = True

    def five(self):
        self.selected_time = 3
        self.button_1.config(default="active")
        self.button_2.config(default="normal")
        self.button_3.config(default="normal")

    def ten(self):
        self.selected_time = 5
        self.button_2.config(default="active")
        self.button_1.config(default="normal")
        self.button_3.config(default="normal")

    def teen(self):
        self.selected_time = 7
        self.button_3.config(default="active")
        self.button_2.config(default="normal")
        self.button_1.config(default="normal")
    def started(self):
        return self.started

    def start(self):
        self.initial_run = True
        if not self.started:
            self.button.config(text="Stop")
            self.started = True
            time.sleep(self.selected_time)
        else:
            self.button.config(text="Start")
            self.started = False

