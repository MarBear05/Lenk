from sys import exit
try:
    from tkinter import Tk, Canvas, Label, Entry, END, CENTER
except ImportError:
    exit(1)
from Lenk import Run

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
        LenkOutput = Run(LenkInput)
        AllOutput += f'[{count}]\n{LenkOutput}\n'
        ConsoleOutput.configure(text=AllOutput)
        count += 1
        ConsoleInput.delete(0, END)
        ConsoleInput.focus()


def quit(event=None):
    exit(0)

#Root app
root = Tk()
root.title(f'Lenk {Run("version:only")} GUI Console')
root.configure(height=800, width=800, bg='#222')
#make window resizable
root.resizable(0,0)

#create window
window = Canvas(root, height=800, width=800, bg='#333')
window.place(x=0, y=0, height=800, width=800)

#make label
VersionText = Label(window, '',text=f'Lenk {Run("version:only")} Console Output',background="#333",foreground="#aaa")
VersionText.place(x=25,y=20,height=30,width=230 )

#Console output
ConsoleOutput = Label(window, '', background="#000", foreground="#0f0", font="Arial 20", justify=CENTER)
ConsoleOutput.place(x=25,y=60,height=600,width=750)

#Console Input
ConsoleInput = Entry(window, '', background='#555', foreground='#aaa', font="Arial 20 bold", justify=CENTER)
ConsoleInput.place(x=25,y=675,height=100,width=750)

ConsoleInput.focus()

#when Enter is pressed while ConsoleInput is focused
ConsoleInput.bind('<Return>', Interpret)
#if Escape is pressed
root.bind('<Escape>', quit)

#make window visible
root.mainloop()
