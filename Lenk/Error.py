class Error:
    #when an error is first created
    def __init__(self, Type=None, Desc=None):

        if Type:
            self.ErrorType = Type

        if Desc:
            self.ErrorDesc = Desc

    # print(Error())
    def __str__(self):
        ReturnString = f"{self.ErrorType}: {self.ErrorDesc}"
        return ReturnString

    # repr(Error())
    def __repr__(self):
        ReturnString = f"Error({self.ErrorType}, {self.ErrorDesc})"
        return ReturnString

    # adding an error to a normal string
    def __add__(self, ToAdd):
        ReturnString = f"{ToAdd}{self.__str__()}"
        return ReturnString