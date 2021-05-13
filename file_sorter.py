import os,shutil
from posix import listdir
from os.path import isdir

if os.name == 'nt':
    import win32api, win32con

TEMPDIRLIST = [] #not meant to be used its purpose it to help check if there are any folders and files to work with
#ie if everything has bean sorted already.

FILEFOLDERLIST = [] #global list of file names with ext ie. ["myImg.jpg",...,"myPdf.pdf"] no dir
#designed to be used as a main ref to extract the fileName and extLists

FILELIST = []
FOLDERLIST = []

#lists extracted from FILELIST
FILENAMELIST = [] # list of the file names TODO
FILEEXTLIST = [] #list of the ext, with duplicates
FILECompEXTLIST = [] #list of ext, without duplicates


#checks if a file p is hidden
def file_is_hidden(p):
    if os.name== 'nt':
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux-osx
# checks if we have flags
def has_flags(args):

    argList = args.split(" ")

    if len(argList)>1:
        return True
    return False

# checks if i have arguments
def has_args(args):

    if args == "":
        return False
    return True


# parses the arguments from console
def parser(args):

    argList = args.split(" ")
    #print(str(argList)+"\n")
    return argList

def isfileValid(file):

    ext = os.path.splitext(file)[1]

    if ext == ".app" or ext == ".exe" or ext == ".DS_Store":
        return False
    return True


# creates the global FILELIST
def initiateFileFolderList(dir):

    global FILEFOLDERLIST
    
    if TEMPDIRLIST == []:
        print("WOW such empty")
        exit(0)

    FILEFOLDERLIST = [f for f in os.listdir(dir) if not file_is_hidden(f) and isfileValid(f)]

    if FILEFOLDERLIST != []:
        return True
    return False

def initiateFileList(dir):

    global FILEFOLDERLIST
    global FILELIST
    FILELIST = [f for f in FILEFOLDERLIST if not os.path.isdir(os.path.join(dir,f))]

    if FILELIST != [] and TEMPDIRLIST:
        return True
    return False

def initiateFolderList(dir):

    global FOLDERLIST
    global FILEFOLDERLIST
    FOLDERLIST = [f for f in FILEFOLDERLIST if os.path.isdir(os.path.join(dir,f))]

    if FOLDERLIST != []:
        return True
    return False

def makeFileFolderList(dir):

    fileFolderList = [f for f in os.listdir(dir) if not file_is_hidden(f) and isfileValid(f)]
    
    return fileFolderList

# list of [name] of files does not include directories
def makeFileNameList(dir):

    global FILELIST
    list = []
    for file in FILELIST:
        if not os.path.isdir(os.path.join(dir,file)):
            list.append(os.path.splitext(file)[0])

    return list

def makeFolderList(dir):

    fflist = makeFileFolderList(dir)
    list = []
    for file in fflist:
        if os.path.isdir(os.path.join(dir,file)):
            list.append(os.path.splitext(file)[0])
            
    return list

#like makeFileList() except includes the whole filename does not include dir
def makeFilePathList(dir):
    fflist = makeFileFolderList(dir)
    list = []
    for file in fflist:
        if not os.path.isdir(os.path.join(dir,file)):
            list.append(file)

    return list
# counts the num of folders
def folderCounter(dir):

    dirlen = 0

    fileFolderList = os.listdir(dir)

    for f in fileFolderList:
        #print(str(os.path.isdir(os.path.join(dir,f)))+" : " +str(f))
        if os.path.isdir(os.path.join(dir,f)): # we cannot do just do if f becuase isDir need an aboslute $path ie /Home/Users/folderName

            dirlen += 1
    

    #print("listing dir: "+str(os.listdir(dir)))
    
    print("folder count: " + str(dirlen)+"\n\n")
    return dirlen

# counts the number of files (directories counted) in the given directory
def fileCounter(dir):

    dirFilelen = len(next(os.walk(dir))[2])
    
    ##check for .app and .exe

    fileFolderList = next(os.walk(dir))[1]
    
    incompCount = 0
    for i in range(0,len(fileFolderList)):

        ext = os.path.splitext(fileFolderList[i])[1]
        #print("\next from fileCount: " +str(ext))
        if ext == ".app" or ext == ".exe":
            incompCount += 1
    
    dirFilelen = dirFilelen - incompCount

    # print(str(dirlen) + "\n")
    print(dirFilelen)
    print("\n")
    #print(next(os.walk(dir))[2])
    print("\n")
    return dirFilelen


def getFileCount():

    return len(FILELIST)

def getFolderCount():

    return len(FOLDERLIST)

def getFileFolderCount():

    return len(FILEFOLDERLIST)

def getExtCount():
    return len(FILEEXTLIST)

def getCompExtCount():
    return len(FILECompEXTLIST)


#makes 2 lists of the extentions for both the ext list as present from the foler or just the types of ext ie
# with duplicates and without
def initiateExtLists():

    

    print("file count: "+str(getFileCount()))
    for i in range(0,getFileCount()):
        j = 0
        has_duplicates = False
        ext = os.path.splitext(FILELIST[i])[1].lower()

        FILEEXTLIST.append(ext)

        while (j < getCompExtCount()) and has_duplicates == False:

            if ext == FILECompEXTLIST[j]:
                has_duplicates = True
            j += 1
        if not has_duplicates:
            FILECompEXTLIST.append(ext)

        #print("makextPre: " +str(ext))
        
        
        
    if FILEEXTLIST != [] and FILECompEXTLIST != []:

        if getFileCount() != getExtCount():
            print("\nfile count not equal to ext count\n")
            print("fileCount: "+str(getFileCount())+" extCount: "+str(getExtCount())+"\n")
            return False
        if getExtCount()>0 and getCompExtCount() == 0:
            print("\next >0 but comp ext = 0\n")
            return False
        return True
        
    return False

# checks if a directory(folder) is of a certain type(ext) in order to be of type iS all of its files must be of the same type 
# hence a meethod must be made that fixes folders which include wrong file types TODO
def dir_isType(dir,type):

    isType = True

    return isType

# makes the Ext name of the folder ie "[pdf]""
def makeExtName(ext):

    name = "[" + str(ext)[1:] + "]" # takes the ext name ".myExt" and removes "." result "myExt"

    return name

# makes the full "[myExt] Folder" name
def makeFolderName(ext):

    name = makeExtName(ext) + " Folder"

    return name

# Moves a file from one directory to another
def fileMove(filePath,dir):

    return shutil.move(filePath,dir)

#makes a folder at the specified path and with the given name ie "users/Myuser/Documents/[pdf] folder"
def makeFolder(dir,name):

    path = os.path.join(dir,name)

    os.mkdir(path)

    return None


#main method for managing the creation or verification of folders
# creation procedure 
# sees ext type call it .myExt
# checks if it exists if so do nothing
# if not make it
# folder name: "[myext] Folder" w/o quotes
# returns true if a folder was created false otherwise
def folderManager(dir):

    global FILECompEXTLIST

    print("\ncompactextlist:  "+str(FILECompEXTLIST) +" \n\n folderList: " +str(FOLDERLIST)+"\n")
    folderCreated = False
    folderCreatedCount = 0
    preExistingFolderCount = 0
    for i in range(0,getCompExtCount()):

        folderExists = False

        j = 0
        while  (folderExists == False) and (j < getFolderCount()):
        
            if makeFolderName(FILECompEXTLIST[i]) == FOLDERLIST[j]:

                folderExists = True
                preExistingFolderCount += 1

            j += 1

        if folderExists == False: # folder creation

            makeFolder(dir, makeFolderName(FILECompEXTLIST[i]))
            folderCreated = True
            folderCreatedCount += 1

    if folderCreatedCount != getCompExtCount()-preExistingFolderCount:
        print(folderCreatedCount)
        print("\nerror in folder creation, folders made: "+str(folderCreatedCount)+" ,ext list size needed: "+str(getCompExtCount())+"\n")
        return False
    return True


#handles the movement of the files from the dir to the corresponding folders existing from the folderManager method
def fileManager(dir):

    #folderList = makeFolderList(dir) 
    #fileList = makeFilePathList(dir)
    #ffList = makeFileFolderList(dir)
    #extlist = makeExtList(dir)#has duplicates

    error = None

    #print("extList: "+str(extlist)+" : "+str(folderList)+" : "+str(fileList))

    for i in range(0,getFileCount()):

        foundFolder = False
        j = 0
        while not foundFolder:
            #print("i/j " +str(i)+" : "+str(j))
            if makeFolderName(FILEEXTLIST[i]) == FOLDERLIST[j]:

                error = fileMove(os.path.join(dir,FILELIST[i]), os.path.join(dir,FOLDERLIST[j]))
                print("match? "+str(makeFolderName(FILEEXTLIST[i])) + " 'to' "+(FOLDERLIST [j])+" is? "+str(makeFolderName(FILEEXTLIST [i]) == FOLDERLIST[j]))
                print("moving: "+str(os.path.join(dir,FILELIST[i])) +" 'to' " +str(os.path.join(dir,FOLDERLIST[j]))+"\n")
                foundFolder = True
            j += 1
        
    return None

def statusToEng(status):

    if str(status) == "True":
        return "OK"
    elif str(status) == "False":
        return "Not Ok"
    elif str(status) == "None":
        return "None,status: OK"
    else:
        print("CAUTION status code: "+str(status))
        return "Error_status"

def listInitializer(dir):

    global TEMPDIRLIST
    TEMPDIRLIST = os.listdir(dir) # do not use in production only used for debug purposes

    ffStatus = initiateFileFolderList(dir)
    print("ff status: " + statusToEng(ffStatus))
    if not ffStatus: exit(1)

    fileStatus = initiateFileList(dir)
    print("file status: "+statusToEng(fileStatus))
    
    folderStatus = initiateFolderList(dir)
    print("folder status: "+ statusToEng(folderStatus))
    if ((not folderStatus) and (not fileStatus)) and ffStatus: exit(1)

    extListStatus = initiateExtLists()
    print("extList status: "+ statusToEng(extListStatus))
    if not extListStatus and fileStatus: exit(1)

    if ffStatus and fileStatus and folderStatus and extListStatus:
        print("Program Status Normal\n\n")
        return True

    print("Program has done some work\n\n")
    return False
    
def managerInitalizer(dir):

    print("Managing folders...\n")
    folderManagerStatus = folderManager(dir)
    print("folderManagerStatus: "+statusToEng(folderManagerStatus))
    if not folderManagerStatus: exit(1)

    ######

    print("Managing Files...\n")
    fileManagerStatus = fileManager(dir)
    print("fileManagerStatus: "+statusToEng(fileManagerStatus))
    if fileManagerStatus != None: exit(1)

    if folderManagerStatus and fileManagerStatus == None:
        print("Manager Status: OK\n\n")
        return True
    print("Manager has at least 1 error\n\n")
    return False


def main():

    args = input("enter folder name and flags\n")
    print(has_args(args))

    if has_args(args):

        argFlagList = parser(args)
        print("argflaglist: "+str(argFlagList))
        dir = argFlagList[0]
        print("dir: "+str(dir))
        if has_flags(args):
            
            flags = []
            for i in range(1,len(argFlagList)):
                flags.append(argFlagList[i])  

            #flags = [f for f in argFlagList] 
            #flags.pop(0) # pop the dir of the flag list to get only the flag list since we copied the dir as well
            # how can i copy from the 0th+1 index to prevent this?
            print("flags: "+str(flags)) 
        print("\n")
        #makeCompactExtList(dir)(dir)

    else:
        print("\n")


        # initiation of lists

        #dir = "/Users/kuraizen/Documents/Scripts/file_sorter/fs_test"
        dir = "/Users/kuraizen/Downloads"

        print(listInitializer(dir))

        #makeCompactExtList(dir) #temp only saved here to not have to retype
        #file_type_list("/Users/kuraizen/Downloads")
        #folderCounter("/Users/kuraizen/Downloads")
        #folderCounter(dir)

        print("folder count: "+str(getFolderCount()))

        managerInitalizer(dir)

        print("count: "+str(getFileCount()))
        #print("\nfilepathList: "+str(makeFilePathList(dir)))
        #print("\nmakefileFolder: "+str(makeFolderList(dir)))
        #print("\nwalk: "+str(next(os.walk(dir))[1]))
        print("End of Program\n")
if __name__ == "__main__":
    main()