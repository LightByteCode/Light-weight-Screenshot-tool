import tkinter as tk

class Button:
    def __init__(self,parent,pos,size,text,command,text_color="black",bg="white",fg="#bcc4cd"):
        self.text_color=text_color
        self.bg=bg
        self.fg=fg
        self.x,self.y=pos
        self.width,self.height=size
        self.text=text

        self.btn=tk.Label(parent,text=self.text,fg=self.text_color,bg=self.bg)
        self.btn.place(x=self.x,y=self.y,width=self.width,height=self.height)

        self.btn.bind("<Enter>",self._change_enter)
        self.btn.bind("<Leave>",self._change_leave)
        self.btn.bind("<Button-1>",lambda event:command())

    def _change_enter(self,event):
        self.btn["bg"]=self.fg
    def _change_leave(self,event):
        self.btn["bg"]=self.bg

class Drag_Window(tk.Toplevel):
    def __init__(self,parent):
        tk.Toplevel.__init__(self,parent)
        self.x = self.y = 0
        self.attributes("-topmost",True)
        self.attributes("-alpha",0.4)
        self.attributes("-fullscreen",True)
        self.canvas = tk.Canvas(self,cursor="cross",bg="white")
        self.canvas.place(x=0,y=0,width=self.winfo_screenwidth(),height=self.winfo_screenheight())
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.rect = None

        self.start_x = None
        self.start_y = None
        self.end_x=None
        self.end_y=None

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle if not yet exist
        #if not self.rect:
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, fill="black")

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)

        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_button_release(self, event):
        self.end_x=event.x
        self.end_y=event.y

        if not((self.end_x-self.start_x==0)and(self.end_y-self.start_y==0)):
            if self.end_x<self.start_x:
                self.start_x,self.end_x=self.end_x,self.start_x
            if self.end_y<self.start_y:
                self.start_y,self.end_y=self.end_y,self.start_y

