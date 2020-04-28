from . import Commands
from .Error import Error
from .Parse import Parse


def Run(Input):

    Output = ''
    # parse input into commands
    cmds = Parse(Input)

    # run every command
    for cmd in cmds:
        # if the command isnt just ""
        if cmd[0]:
            try:
                Function = getattr(Commands, cmd[0])
                Output += Function(cmd[1], cmd[2])
            # if the command doesnt exist getattr() raises an AttributeError
            except AttributeError:
                Output += str(Error('Command Error',
                                    f'The command "{cmd[0]}" does not exist\n'))

    # Give all commands output to caller
    return Output
