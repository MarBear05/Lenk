def Parse(command: str):
    import os,sys,re

    LenkVersion = '0.0.9'
    CurrentError = None
    AllCommands = command.split(';')
    
    Output = ''

    def Error(*errors):
        fullerr = ''
        start = ''
        if len(errors) > 1:
            start = f'Multiple errors! '
        for error in errors:
            line = error[2]
            fullerr += f'Line {line}:({error[1]}: {error[0]}); '
        return f"{start}{fullerr[0:-2]}\n"
    
    line = 1

    for cmd in AllCommands:
        _ = cmd.split(':', 1)
        Command = re.sub(r'[ ]',' ',re.sub(r'[;]', ';', _[0].replace(' ', '')))
        
        try:
            Argument = re.sub(r'^[ ]*','',_[1])
            Arguments = Argument.split('/')
        except IndexError:
            Argument = ''
            Arguments = []

            CurrentError = ["Not enough arguments!","Argument Error",line]

        Command = Command.lower()

        if not Command:
            continue

        try:
            #strings/text
            if Command == 'text':
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
                sys.exit(0)
            
            elif Command == 'clear' or Command == 'cls' or Command == 'erase':
                os.system('cls' if os.name == 'nt' else 'clear')

            #Planned
            elif 'if' in Command:
                Output += 'This command is coming soon!\n'

            elif 'for' in Command:
                Output += 'This command is coming soon!\n'
            
            elif 'set' in Command:
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