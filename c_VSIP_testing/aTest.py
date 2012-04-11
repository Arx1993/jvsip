#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# Line above should be changed to be compliant with the desired python
from Tkinter import *
from tkFileDialog import *
from subprocess import call, Popen
from os.path import split as osSplit
from os.path import join as osJoin
from os import getcwd

master = Tk()

mydir = getcwd()

def dirFind(aParent,anEntry):
    aDir=askdirectory(parent=aParent,initialdir=anEntry.get(),title='Please select a directory')
    anEntry.delete(0,END)
    anEntry.insert(0,aDir)

def fileFind(aParent,dirEntry,anEntry):
    aFile=osSplit(askopenfilename(parent=aParent,initialdir=dirEntry.get(),title='Please select a file'))
    if len(aFile[1]):
        dirEntry.delete(0,END)
        dirEntry.insert(0,aFile[0])
        anEntry.delete(0,END)
        anEntry.insert(0,aFile[1])
    
def pathFind(aParent,anEntry):
    """ pathFind(aParent,anEntry)
           aParent is a Tkinter frame anEntry resides in
           anEntry is a Tkinter Entry object
        Th function opens a finder object. The returned value a string containing
        the complete path to the selected file. The results are placed in
        anEntry. 
        The initial contents of anEntry are used as to get the starting directory
        for the search.
    """
    initPath=osSplit(anEntry.get())[0]
    if len(initPath):
        aPath=askopenfilename(parent=aParent,initialdir=initPath,title='Please select a file')
        if len(aPath):
            anEntry.delete(0,END)
            anEntry.insert(0,aPath)
    else:
        aPath=aksopenfilename(parent=aParent,title='Please select a file')
        if len(aPath):
            anEntry.delete(0,END)
            anEntry.insert(0,aPath)

def testOpen(dirEntry,anEntry):
    call(['open',osJoin(dirEntry.get(),anEntry.get())])

frame_aTest=Frame(master)
frame_aTestDir=Frame(master)
frame_aLibrary=Frame(master)
frame_aIncludeDir=Frame(master)
frame_aButtonPlace=Frame(master)

lbl_aTest = Label(frame_aTest, text="Test Name", width=15,anchor=E)
lbl_aTestDir = Label(frame_aTestDir, text="Test Directory",width=15,anchor=E)
lbl_aIncludeDir= Label(frame_aIncludeDir, text="Directory for vsip.h", width=15, anchor=E)
lbl_aLibrary = Label(frame_aLibrary, text="VSIPL Library",width=15, anchor=E)

aTest = Entry(frame_aTest, width=50)
aTestDir = Entry(frame_aTestDir, width=50)
aIncludeDir=Entry(frame_aIncludeDir, width=50)
aLibrary = Entry(frame_aLibrary, width=50)

aTestButton=Button(frame_aTest, text="find", width=5, command=lambda: fileFind(frame_aTest,aTestDir,aTest))
aTestDirButton=Button(frame_aTestDir,text="find", width=5, command=lambda: dirFind(frame_aTestDir,aTestDir))
aIncludeDirButton=Button(frame_aIncludeDir,text="find", width=5, command=lambda: dirFind(frame_aIncludeDir,aIncludeDir))
aLibraryButton=Button(frame_aLibrary, text="find", width=5, command=lambda: pathFind(frame_aLibrary,aLibrary))

lbl_aTest.grid(row=0,column=0)
aTest.grid(row=0,column=1)
aTestButton.grid(row=0,column=2)

lbl_aTestDir.grid(row=1,column=0)
aTestDir.grid(row=1,column=1)
aTestDirButton.grid(row=1,column=2)

lbl_aLibrary.grid(row=2,column=0)
aLibrary.grid(row=2,column=1)
aLibraryButton.grid(row=2,column=2)

lbl_aIncludeDir.grid(row=3,column=0)
aIncludeDir.grid(row=3,column=1)
aIncludeDirButton.grid(row=3,column=2)

frame_aTest.grid(row=0,column=0)
frame_aTestDir.grid(row=1,column=0)
aTestDir.insert(0,mydir)
frame_aIncludeDir.grid(row=2,column=0)
aIncludeDir.insert(0,mydir)
frame_aLibrary.grid(row=3,column=0)
aLibrary.insert(0,mydir)

def runTest():
    mytestfile=osJoin(aTestDir.get(),aTest.get())
    aFunc=aTest.get().split(".")[0]+"();"
    mytest="atest.c"
    aFile=open(mytest,"w")
    aFile.write("#define NDPTR_f ((vsip_scalar_f*)NULL)\n#define NDPTR_d ((vsip_scalar_d*)NULL)\n")
    aFile.write("#define NDPTR_i ((vsip_scalar_i*)NULL)\n#define NDPTR_si ((vsip_scalar_si*)NULL)\n")
    aFile.write("#include<vsip.h>\n#include\""+mytestfile+"\"\n")
    aFile.write("int main(){\n\tvsip_init((void*)0);\n")
    aFile.write("\t"+aFunc);
    aFile.write("\n\tvsip_finalize((void*)0); \n\treturn 0;\n} ")
    aFile.close()
    a_gcc_call=['gcc', '-o', 'atest', 'atest.c', aLibrary.get(),'-I'+aIncludeDir.get()]
    #print(a_gcc_call)
    #call(a_gcc_call)
    aProcess = Popen(a_gcc_call)
    print(aProcess.communicate())
    call(['./atest'])


testCompileButton = Button(frame_aButtonPlace, text="Run Test", width=14, command=runTest)
testCompileButton.grid(row=0,column=1)
testOpenButton=Button(frame_aButtonPlace,text="Open Test", width=14, command=lambda: testOpen(aTestDir,aTest))
testOpenButton.grid(row=0,column=0)
frame_aButtonPlace.grid(row=4,column=0)


mainloop()