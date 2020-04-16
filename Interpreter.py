def Parse(command: str):
    from os import system, name
    from sys import exit
    from re import sub

    LenkVersion = '0.1.1'
    CurrentError = None
    SplitCommands = command.split(';')
    AllCommands = []
    for cmd in SplitCommands:
        AllCommands.append(cmd.split('~'))

    # print(SplitCommands)
    # print(AllCommands)

    try:
        global Variables
        if not Variables:
            Variables = {}
    except Exception:
        Variables = {}

    Output = ''

    def Error(*errors):
        fullerr = ''
        start = ''
        if len(errors) > 1:
            start = f'Multiple errors! '
        for error in errors:
            line = error[2]
            fullerr += f'Line {line}:({error[1]}: {error[0]}); '
        return f"\n{start}{fullerr[0:-2]}\n"
    
    line = 1
    for nestedcmd in AllCommands:
        for cmd in nestedcmd:
            _ = cmd.split(':', 1)
            Command = sub(r'[ ]',' ',sub(r'[;]', ';', _[0].replace(' ', '')))

            try:
                Argument = sub(r'^[ ]*','',_[1])
                Arguments = Argument.split('/')
            except IndexError:
                Argument = ''
                Arguments = []

                CurrentError = ["Not enough arguments!","Argument Error",line]

            Command = Command.lower()

            if not Command:
                continue

            try:
                #help
                if Command == 'help':
                    with open('Help.log') as helpfile:
                        Output += helpfile.read()

                #strings/text
                elif Command == 'text':
                    if len(Arguments) > 1:
                        Arguments = ""
                        for arg in Arguments:
                            Arguments.join(f"{arg},")
                        Argument = Argument.replace('/','\n')
                    Output += Argument

                #whitespace
                elif Command == 'blank':
                    Output += "\n"

                #numbers/numeric
                elif Command == 'numeric':
                    default = 0
                    Output += str(eval(Argument.replace('/',','))) if Arguments else str(default)

                #version
                elif Command == 'version':
                    if 'only' in Arguments:
                        Output += LenkVersion
                    else:
                        Output += f"Lenk Version: {LenkVersion}"

                #quit/exit
                elif Command == 'exit' or Command == 'quit':
                    exit(0)
                
                elif Command == 'clear' or Command == 'cls' or Command == 'erase':
                    system('cls' if name == 'nt' else 'clear')
                
                elif Command == 'set':
                    try:
                        VarName = Arguments[0]
                    except IndexError:
                        Output += Error(['No variable name given', 'Argument Error',line])
                    try:
                        VarValue = Arguments[1]
                    except IndexError:
                        Output += Error(['No variable value given', 'Argument Error', line])
                    
                    if not VarName in Variables:
                        Variables.update({VarName: VarValue})
                    else:
                        Variables[VarName] = VarValue

                elif Command == 'get':
                    try:
                        ReferenceName = Arguments[0]
                    except IndexError:
                        Output += Error(['No reference given', 'Argument Error', line])
                    try:
                        Variable = Variables[ReferenceName]
                        Output += Variable
                    except KeyError:
                        Output += Error([f'{ReferenceName} is not a variable!', 'Variable Error', line])                  

                #Planned
                elif Command == 'if':
                    Output += 'This command is coming soon!\n'

                elif Command == 'for':
                    Output += 'This command is coming soon!\n'
                
                elif Command == 'while':
                    Output += 'This command is coming soon!\n'

                #If command doesnt exist
                else:
                    Output += Error([f'The command "{Command}" does not exist!','Command Error',line])

            except IndexError:
                if CurrentError:
                    if CurrentError[1] == 'Argument Error':
                        Output += Error([f'The command "{Command}" does not exist!', 'Command Error',line])
                    else:
                        Output += Error([f'The command "{Command}" does not exist!', 'Command Error',line], CurrentError)
                else:
                    Output += Error([f'The command "{Command}" does not exist!', 'Command Error',line])
            
            line += 1
            
    return Output