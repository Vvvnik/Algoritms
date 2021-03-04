import os


def MyReadTxtFile(NameFile):
    f = open(NameFile, 'r')
    a = f.read()
    f.close()
    return (a)



