from .Error import Error

# PLANNED: c   m d  :   arg / arg /// ; > cmd:arg/arg/;
try:
    from re import sub
except ImportError:
    sub = None


# Parse(Input)

def Parse(Input: str):
    Output = ''

    # For scripting
    InComSplit = Input.split('\n')
    ComSplit = []

    for Split in InComSplit:
        ComSplit.append(Split.split(';'))

    Parsed = []

    for nestcmd in ComSplit:
        for cmd in nestcmd:
            # Separate Command and Arguments, CMD ARG/ARGS
            Separated = cmd.split(':',1)
            _cmd = ''
            _args = []

            # extract full argument, ARG/ARGS
            try:
                _arg = Separated[1]
            except IndexError:
                _arg = ''

            # extract command, CMD
            try:
                _cmd = Separated[0].lower().replace(' ', '')
            except IndexError:
                _cmd = None
                Output += Error('Parser Error', f'No command given')

            #make first character of command capital
            _cmd = f'{_cmd[0].upper()}{_cmd[1:]}' if len(_cmd) > 2 else _cmd

            # extract separate arguments, ARG ARGS
            try:
                _args = Separated[1].split('/')
            except IndexError:
                _args = []

            # Add parsed command to Parsed
            Parsed.append([_cmd, _args, _arg])

    # Give Caller parsed input
    return Parsed
