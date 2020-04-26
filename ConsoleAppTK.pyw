from sys import exit
try:
    from tkinter import Tk, Canvas, Label, Entry, END, CENTER
except ImportError:
    exit(1)
from Interpreter import Parse

count = 0
AllOutput = ''

def Interpret(event=None):
    global AllOutput
    global count
    LenkInput = ConsoleInput.get()
    if LenkInput == 'clear' or LenkInput == 'cls':
        AllOutput = ''
        count = 0
        ConsoleInput.delete(0, END)
        ConsoleInput.focus()
        ConsoleOutput.configure(text=AllOutput)
    else:
        LenkOutput = Parse(LenkInput)
        AllOutput += f'[{count}]\n{LenkOutput}\n'
        ConsoleOutput.configure(text=AllOutput)
        count += 1
        ConsoleInput.delete(0, END)
        ConsoleInput.focus()


def quit(event=None):
    exit(0)


root = Tk()
root.title(f'Lenk {Parse("version:only")} GUI Console')
root.configure(height=800, width=800, bg='#222')
root.resizable(0,0)

window = Canvas(root, height=800, width=800, bg='#333')
window.place(x=0, y=0, height=800, width=800)

ConsoleOutput = Label(window, '', background="#000", foreground="#0f0", font="Arial 20", justify=CENTER)
ConsoleOutput.place(x=0,y=0,height=650,width=800)

ConsoleInput = Entry(window, '', background='#555', foreground='#999999', font="Arial 20 bold", justify=CENTER)
ConsoleInput.place(x=0,y=650,height=150,width=800)

ConsoleInput.focus()

ConsoleInput.bind('<Return>', Interpret)
root.bind('<Escape>', quit)

root.mainloop()
