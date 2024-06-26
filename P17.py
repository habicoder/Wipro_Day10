# Creating a Singleton class in Python
# A singleton class allows the creation of only one instance of itself.

class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self

s = Singleton.getInstance()
print(s)