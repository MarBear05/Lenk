from .Error import Error

# Main controller for version, help, get, and set


class Controller:
    def __init__(self):
        # help
        self.HelpText = """Lenk Help\n\nHelp\nResponds with this\nArgs: none\n\nVersion\nResponds with the current version with 'Lenk Version' following it. With the 'only' argument set it will only respond with the current version.\nArgs: [only]\n\nText\nMirrors input\nArgs: {string}\n\nNumeric\nEvaluates math expressions\nArgs: {expression}\n\nClear/Cls\nClears the terminal\nArgs: none\n\nQuit/Exit\nExits process\nArgs: none\n\nSet\nCreates a variable\nArgs: {name, value}\n\nGet\nResponds with variables content\nArgs: {variable}\n\nOpenFile\nGets the content of a file\nArgs: {filepath}"""
        # version
        self.Version = "0.1.3"
        #set and get
        self.__Variables = {}

    # set
    def Set(self, Name, Value):
        if not Name:
            return Error('Argument Error', 'No variable name is supplied')

        self.__Variables.update({Name: Value})
        return True
    # get

    def Get(self, Name):
        if not Name:
            return Error('Argument Error', 'No variable name is supplied')

        if not Name in self.__Variables:
            return Error('Variable Error', f'The variable "{Name}" does not exist')

        return self.__Variables[Name]
