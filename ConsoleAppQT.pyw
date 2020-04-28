import sys
try:
    from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QLineEdit,QGridLayout,QGroupBox,QVBoxLayout
    from PyQt5.QtCore import QSize
except ImportError:
    try:
        from tkinter import messagebox
        messagebox.showerror('Please install PyQt5', 'You need to install PyQt5 to run this script.')
        sys.exit(1)
    except ImportError:
        sys.exit(1)
from Lenk import Run

App = QApplication([])
AppWindow = QWidget(size=QSize(800,800))
AppLayout = QGridLayout(AppWindow)

AppWindow.setWindowTitle(f'Lenk <{Run("version:only")}> GUI')
App.setStyle("Fusion")
App.setStyleSheet("""
QWidget { background:#222; color:#999; padding:12px; }
QTextEdit { background:#000; color:green; padding:10px; font-size:15px; }
QLineEdit { background:#555; padding:15px; font-size:25px; color:white; }
QGroupBox { margin:20px 0 20px 0; padding:0; background:transparent; border:none; }
QTextEdit,
QLineEdit { border-radius:20px; }
""")

ConsoleOGroup = QGroupBox(f'\t\tLenk {Run("version:only")} Console Output')
CGOLayout = QVBoxLayout(ConsoleOGroup)

ConsoleOutput = QTextEdit()
CGOLayout.addWidget(ConsoleOutput)
AppLayout.addWidget(ConsoleOGroup, 0, 0, 3, 0)
ConsoleOutput.setReadOnly(True)

ConsoleInput = QLineEdit()
AppLayout.addWidget(ConsoleInput, 4, 0)

count = 1

def InterpretCommand():
    global count
    LenkInput = ConsoleInput.text()
    if LenkInput == 'clear' or LenkInput == 'cls':
        ConsoleOutput.clear()
        count = 1
    else:
        LenkOutput = Run(LenkInput)
        ConsoleOutput.append(f'[{count}] {LenkOutput}')
        count +=1
    ConsoleInput.clear()

ConsoleInput.returnPressed.connect(InterpretCommand)

AppWindow.show()

sys.exit(App.exec_())
