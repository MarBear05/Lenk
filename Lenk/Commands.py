# from . import Extensions
from .Controller import Controller
from .Error import Error

# for set, get, help, and version:
Controller = Controller()

# text:Hello, world!


def Text(args, arg):
    ReturnString = ''
    ReturnString += arg.replace('/', '\n')
    return ReturnString

# numeric:23*3


def Numeric(args, arg):
    ReturnString = ''
    try:
        ReturnString += eval(arg)
    except SyntaxError:
        ReturnString += str(Error('Command Error',
                                  'During evaluation an error occured'))

    return ReturnString

# openfile:File.txt


def Openfile(args, arg):
    ReturnString = r''
    FileStream = None
    try:
        FileStream = open(arg, 'r')
    except IOError:
        ReturnString = str(Error(
            'File Error', f'The file "{arg}" could not be opened.'))
    except UnicodeError:
        ReturnString = str(Error(
            'File Error', f'The file "{arg}" could not be opened.'))

    try:
        if FileStream:
            ReturnString += FileStream.read()
    except IOError:
        ReturnString += str(Error(
            'File Error', f'The file "{arg}" could not be read.'))

    return ReturnString

# set:Lenk/0.1.3


def Set(args, arg):
    ReturnString = ''
    try:
        Controller.Set(args[0], args[1])
    except IndexError:
        ReturnString = str(Error('Argument Error',
                                 'No variable name/value supplied'))

    return ReturnString

# get:Lenk


def Get(args, arg):
    ReturnString = ''
    try:
        ReturnString = Controller.Get(args[0])
    except IndexError:
        ReturnString = str(Error('Argument Error',
                                 'No variable name supplied'))

    return ReturnString

# version


def Version(args, arg):
    ReturnString = ''
    if "only" in arg.lower():
        ReturnString = Controller.Version
    else:
        ReturnString = f'Lenk Version {Controller.Version}'

    return ReturnString

# help


def Help(args, arg):
    ReturnString = Controller.HelpText

    return ReturnString

# clear/cls


def Clear(args, arg):
    ReturnString = ''
    print("\033[2J" + '\n'*(500))

    return ReturnString


def Cls(args, arg):
    return Clear(args, arg)

# quit/exit


def Exit(args, arg):
    exit(0 if not arg else arg)
    return None


def Quit(args, arg):
    Exit(args, arg)
    return None


#PLANNED: SCRIPTING
# openscript:CoolScript.ls


def openscript(args, arg):
    ReturnString = 'This feature is currently disabled!\nThis feature is most likely going to be re-enabled in 0.1.4 or 0.1.5.'

    return ReturnString

    # FileRead = openfile(args, arg)
    # if FileRead is Error:
    #     ReturnString += FileRead
    # else:
    #     ReturnString += Run(FileRead)


#PLANNED: EXTENSIONS
# ext:extension/arg/arg
def ext(args, arg):
    ReturnString = 'This feature is curently being developed.\nExpected release version: 0.1.4 or 0.1.5.'

    return ReturnString

    # try:
    #     Command = args[0]
    # except IndexError:
    #     Command = None
    #     ReturnString = str(Error('Arguments Error', 'No Extension supplied'))

    # try:
    #     Arguments = args[1:]
    #     Argument = arg.replace(f'{Command}/', '')
    # except IndexError:
    #     Arguments = []
    #     Argument = ''
