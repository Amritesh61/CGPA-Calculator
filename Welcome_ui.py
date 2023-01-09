import tkinter

class Welcome(object):
    _images = []
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('lpu.gif', file = 'lpu.gif'))
        self._images.append(tkinter.PhotoImage('lpu-cgpa-calc.gif', file = 'lpu-cgpa-calc.gif'))

        # Widget Initialization
        self._frame_1 = tkinter.Frame(root,background = "#ffffff",)
        self._label_1 = tkinter.Label(root,
            activebackground = "#ffffff",
            background = "#ffffff",
            borderwidth = 1,
            cursor = "arrow",
            font = "{MS Sans Serif} 24 bold",
            image = "lpu-cgpa-calc.gif",
            text = "CGPA Calculator",)
        
        self._label_4 = tkinter.Label(root,
            activebackground = "#feebcd",
            activeforeground = "#ff0033",
            background = "#feebcd",
            font = "{MS Sans Serif} 13 bold italic",
            foreground = "#ff0033",
            )
        self.login = tkinter.Button(root,
            activebackground = "#8E44AD",
            background = "#8E44AD",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Agency FB} 10 bold",
            text = "Login",)
        self.newuser = tkinter.Button(root,
            activebackground = "#8E44AD",
            background = "#8E44AD",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Agency FB} 10 bold",
            text = "New User",)
        self._label_2 = tkinter.Label(root,
            activebackground = "#F4D03F",
            background = "#F4D03F",
            borderwidth = 0,
            font = "{Agency FB} 14 bold",
            text = """This is the Grading/Cgpa calculator for LPU that uses fuzzy logic to calculate the CGPA of the students. This project is based on ten point scale. 
Academic excellence is measured using the Grade Point Average (GPA) and Cumulative Grade Point Average (CGPA).
""",)
        
        self.exit = tkinter.Button(root,
            activebackground = "#C0392B",
            background = "#C0392B",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Agency FB} 10 bold",
            text = "Exit",)
        self._label_5 = tkinter.Label(root,
            activebackground = "#fff4d2",
            activeforeground = "#fb001a",
            background = "#fff4d2",
            font = "{MS Sans Serif} 14 bold italic",
            foreground = "#fb001a",
            text = """ Submitted by :- Uday Tripathi (12018460) And Amritesh Raj (12016485)
            """,)

        # widget commands
        self.login.configure(command = self.login_command)
        self.newuser.configure(command = self.newuser_command)
        self.exit.configure(command = self.exit_command)

        # Geometry Management
        self._frame_1.grid(in_ = root,column = 5,row = 2,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._label_1.grid(in_ = root,column = 1,row = 1,columnspan = 5,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 2,sticky = "nsew")
        self._label_4.grid(in_ = root,column = 5,row = 5,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.login.grid(in_ = root,column = 1,row = 4,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.newuser.grid(in_ = root,column = 3,row = 4,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_2.grid(in_ = root,column = 1,row = 3,columnspan = 5,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew") 
        self.exit.grid(in_ = root,column = 5,row = 4,columnspan = 1,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_5.grid(in_ = root,column = 1,row = 5,columnspan = 5,ipadx = 0,ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "nsew")

        # Resize Behavior
        root.grid_rowconfigure(1, weight = 0, minsize = 42, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 82, pad = 0)
        root.grid_rowconfigure(3, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(4, weight = 0, minsize = 36, pad = 0)
        root.grid_rowconfigure(5, weight = 1, minsize = 39, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 145, pad = 0)
        root.grid_columnconfigure(2, weight = 0, minsize = 145, pad = 0)
        root.grid_columnconfigure(3, weight = 0, minsize = 145, pad = 0)
        root.grid_columnconfigure(4, weight = 0, minsize = 145, pad = 0)
        root.grid_columnconfigure(5, weight = 0, minsize = 145, pad = 0)