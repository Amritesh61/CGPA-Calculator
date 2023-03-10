from tkinter import *
from tkinter import messagebox
import tkinter

class Newuser(object):
    _images = [] # Holds image refs to prevent GC
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('new_user.gif', file = 'new_user.gif'))

        # Widget Initialization
        self._frame_1 = tkinter.Frame(root,background = "#3498DB",)
        self._frame_2 = tkinter.Frame(root,background = "#3498DB",)
        self._frame_3 = tkinter.Frame(root,background = "#3498DB",)
        self._frame_4 = tkinter.Frame(root,background = "#3498DB",)
        self._frame_6 = tkinter.Frame(root,background = "#3498DB",)
        self._label_1 = tkinter.Label(root,
            activebackground = "#ffffff",
            activeforeground = "#000099",
            background = "#ffffff",
            borderwidth = 0,
            foreground = "#000099",
            image = "new_user.gif",
            text = "_label_1",)
        self._label_2 = tkinter.Label(root,activebackground = "#3498DB",background = "#3498DB",font = "{MS Serif} 18 bold",takefocus = 1,text = "New User",)
        self._label_3 = tkinter.Label(root,activebackground = "#3498DB",background = "#3498DB",borderwidth = 0,font = "{MS Sans Serif} 8 bold",text = "Name",)
        self._label_4 = tkinter.Label(root,activebackground = "#3498DB",background = "#3498DB",font = "{MS Sans Serif} 8 bold",text = "User ID",)
        self.userid = tkinter.Entry(self._frame_2,background = "#ffffff",width = 50,)
        self.password = tkinter.Entry(self._frame_3,width = 50,show="*")
        '''self._label_5 = tkinter.Label(root,
            activebackground = "#b8010f",
            activeforeground = "#ffffff",
            background = "#A93226",
            font = "{High Tower Text} 8 bold",
            foreground = "#ffffff",
            text = "!! ENTER YOUR DETAILS TO MAKE A NEW ACCOUNT !!",)'''
        self._label_6 = tkinter.Label(root,activebackground = "#3498DB",background = "#3498DB",font = "{MS Sans Serif} 8 bold",text = "Password",)
        self.cpassword = tkinter.Entry(self._frame_4,width = 50,show="*")
        self._label_7 = tkinter.Label(root,activebackground = "#3498DB",background = "#3498DB",font = "{MS Sans Serif} 8 bold",text = "Confirm Password",)
        self.ok = tkinter.Button(root,
            activebackground = "#28B463",
            background = "#28B463",
            borderwidth = 5,
            cursor="hand2",
            font = "{MS Sans Serif} 8 bold",
            text = "OK",)
        self.close = tkinter.Button(root,
            activebackground = "#EC7063",
            background = "#EC7063",
            borderwidth = 5,
            cursor="hand2",
            font = "{MS Sans Serif} 8 bold",
            text = "Close",)
        self.name = tkinter.Entry(self._frame_1,background = "#ffffff",width = 50,)

        # widget commands
        self.ok.configure(command = self.ok_command)
        self.close.configure(command = self.close_command)

        # Geometry Management
        self._frame_1.grid(in_ = root,column = 3,row = 3,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._frame_2.grid(in_ = root,column = 3,row = 4,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._frame_3.grid(in_ = root,column = 3,row = 5,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._frame_4.grid(in_ = root,column = 3,row = 6,columnspan = 2,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._frame_6.grid(in_ = root,column = 2,row = 7,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._label_1.grid(in_ = root,column = 1,row = 2,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 6,sticky = "nsew")
        self._label_2.grid(in_ = root,column = 2,row = 2,columnspan = 3,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_3.grid(in_ = root,column = 2,row = 3,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_4.grid(in_ = root,column = 2,row = 4,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.userid.grid(in_ = self._frame_2,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self.password.grid(in_ = self._frame_3,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        '''self._label_5.grid(in_ = root,column = 1,row = 1,columnspan = 4,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")'''
        self._label_6.grid(in_ = root,column = 2,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.cpassword.grid(in_ = self._frame_4,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")
        self._label_7.grid(in_ = root,column = 2,row = 6,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.ok.grid(in_ = root,column = 3,row = 7,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.close.grid(in_ = root,column = 4,row = 7,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.name.grid(in_ = self._frame_1,column = 1,row = 1,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "ew")

        # Resize Behavior
        root.grid_rowconfigure(1, weight = 0, minsize = 6, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 71, pad = 0)
        root.grid_rowconfigure(3, weight = 0, minsize = 5, pad = 0)
        root.grid_rowconfigure(4, weight = 0, minsize = 43, pad = 0)
        root.grid_rowconfigure(5, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(6, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(7, weight = 0, minsize = 40, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 200, pad = 0)
        root.grid_columnconfigure(2, weight = 0, minsize = 136, pad = 0)
        root.grid_columnconfigure(3, weight = 0, minsize = 55, pad = 0)
        root.grid_columnconfigure(4, weight = 0, minsize = 40, pad = 0)
        self._frame_1.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_1.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_2.grid_rowconfigure(1, weight = 0, minsize = 9, pad = 0)
        self._frame_2.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_3.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_3.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_4.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._frame_4.grid_columnconfigure(1, weight = 0, minsize = 70, pad = 0)

class CustomNewuser(Newuser):
    print("New User Window Opened.")
    pass

    def close_command(self):
        print("Close Button Pressed.")
        print("New User Window Closed.")
        quit(0)
        pass

    def ok_command(self):
        print("ok Button Pressed.")
        print("New User Window Closed.")
        pass

def main():
    root = Tk()
    demo = CustomNewuser(root)
    root.title('newuser')
    root.mainloop()

if __name__ == '__main__': main()
