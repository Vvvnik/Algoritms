import os

def MyReadTxtFile(NameFile):
    f=open(NameFile,'r')
    #print(f.read(len(NameFile)))
    a=f.read(len(NameFile))
    f.close()
    return(a)

print(MyReadTxtFile('TestStr.txt'))
