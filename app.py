from tkinter import *
import pyautogui as pa
import random
import time

class Screenshot:
    def __init__(self,root):
        self.root=root
        self.root.title("ScreenShot")
        self.root.geometry("300x200")
        self.root.iconbitmap("logo1029.ico")
        self.root.resizable(0,0)


        def take():
            r=random.randint(1,100)
            p=pa.screenshot()
            p.save('screen{}.png'.format(r))
            lab.config(text="ScreenShot has been taken as "+'screen{}.png'.format(r))




#=====================frame============================#
        
        mainframe=Frame(self.root,width=300,height=200,relief="ridge",bd=3,bg="gray")
        mainframe.place(x=0,y=0)


        but_screen=Button(mainframe,width=19,text="ScreenShot",font=('times new roman',13),cursor="hand2",command=take)
        but_screen.place(x=55,y=80)

        lab=Label(mainframe,text="",font=('times new roman',12),bg="gray",fg="white")
        lab.place(x=10,y=10)





if __name__ == "__main__":
    root=Tk()
    Screenshot(root)
    root.mainloop()