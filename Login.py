import tkinter
from tkinter import *
from tkinter import messagebox

class Login(object):
    _images = [] # Holds image refs to prevent GC
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('icon_lock_key.gif', file = 'icon_lock_key.gif'))

        # Widget Initialization
        self._frame_1 = tkinter.Frame(root,background = "#FF7B7E",)
        self._frame_2 = tkinter.Frame(root,background = "#FF7B7E",)
        self._frame_3 = tkinter.Frame(root,background = "#FF7B7E",)
        self._label_1 = tkinter.Label(root,
            activebackground = "#D83827",
            activeforeground = "#D83827",
            background = "#D83827",
            font = "{MS Sans Serif} 4 bold",
            foreground = "#000000",
            text = "  !! PLEASE ENTER THE CORRECT INFORMATION !!  ",)
        self._label_7 = tkinter.Label(root,
            activebackground = "#FF7B7E",
            activeforeground = "#990000",
            background = "#FF7B7E",
            foreground = "#990000",
            image = "icon_lock_key.gif",
            text = "_label_7",)
        self._label_2 = tkinter.Label(root,activebackground = "#FF7B7E",background = "#FF7B7E",font = "{Agency FB} 30 bold underline",text = "L O G I N",)
        self._label_3 = tkinter.Label(root,activebackground = "#FF7B7E",background = "#FF7B7E",font = "{High Tower Text} 14 bold",text = " Username  ",)
        self._label_4 = tkinter.Label(root,activebackground = "#FF7B7E",background = "#FF7B7E",font = "{High Tower Text} 14 bold",text = "Password",)
        self.password = tkinter.Entry(self._frame_2,insertwidth = 4,width = 50,show="*",)
        self.username = tkinter.Entry(self._frame_1,insertwidth = 4,width = 50,)
        self.cancel = tkinter.Button(root,
            activebackground = "#C0392B",
            background = "#C0392B",
            borderwidth = 4,
            cursor = "hand2",
            font = "{MS Gothic} 10 bold",
            overrelief = "flat",
            text = "Cancel",)
        self.login = tkinter.Button(root,
            activebackground = "#219403",
            background = "#219403",
            borderwidth = 3,
            cursor = "hand2",
            font = "{MS Gothic} 10 bold",
            overrelief = "flat",
            text = "Login",)

        # widget commands
        self.cancel.configure(command = self.cancel_command)
        self.login.configure(command = self.login_command)

        # Geometry Management
        self._frame_1.grid(in_ = root,column = 3,row = 3,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._frame_2.grid(in_ = root,column = 3,row = 4,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._frame_3.grid(in_  = root,column = 2,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "news")
        self._label_1.grid(in_ = root,column = 1,row = 1,columnspan = 4,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_7.grid(in_ = root,column = 1,row = 2,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 5,sticky = "nsew")
        self._label_2.grid(in_ = root,column = 2,row = 2,columnspan = 3,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_3.grid(in_ = root,column = 2,row = 3,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_4.grid(in_ = root,column = 2,row = 4,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.password.grid(in_ = self._frame_2,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.username.grid(in_ = self._frame_1,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.login.grid(in_ = root,column = 2,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "nsew")
        self.cancel.grid(in_ = root,column = 4,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "nsew")

        # Resize Behavior
        root.grid_rowconfigure(1, weight = 1, minsize = 13, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 70, pad = 0)
        root.grid_rowconfigure(3, weight = 1, minsize = 64, pad = 0)
        root.grid_rowconfigure(4, weight = 1, minsize = 46, pad = 0)
        root.grid_rowconfigure(5, weight = 1, minsize = 24, pad = 0)
        root.grid_rowconfigure(6, weight = 0, minsize = 3, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 100, pad = 0)
        root.grid_columnconfigure(2, weight = 1, minsize = 113, pad = 0)
        root.grid_columnconfigure(3, weight = 0, minsize = 179, pad = 0)
        root.grid_columnconfigure(4, weight = 0, minsize = 196, pad = 0)
        self._frame_1.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_1.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_2.grid_rowconfigure(1, weight = 0, minsize = 87, pad = 0)
        self._frame_2.grid_columnconfigure(1, weight = 0, minsize = 59, pad = 0)

class CustomLogin(Login):
    print("Login Window Opened.")
    pass

    def cancel_command(self):
        print("Cancel Buttton pressed.")
        print("Login Window Closed.")
        quit(0)
        pass

    def login_command(self):
        print("Login Buttton pressed.")
        import main
        self.newwindow = tkinter.Toplevel()
        self.demo = main.CustomMain(self.newwindow)
        pass

def main():
    root = Tk()
    demo = CustomLogin(root)
    root.title('Login')
    root.mainloop()

if __name__ == '__main__': main()
