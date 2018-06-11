from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('title')
root['width'] = 360
root['height'] = 640
btn1 = Button(root,bg='RED')
btn1['width']=100
btn1['height']=50
btn1['border']=5

btn1['text'] = 'click me'
btn1.pack()


def show(e):
    messagebox.showinfo('msg', 'hello world')


btn1.bind('<Button-1>', show)
root.mainloop()
if __name__ == '__main__':
    pass
