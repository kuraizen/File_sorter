import os,shutil

if os.name == 'nt':
    import win32api, win32con

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

def makeFileFolderList(dir):

    fileFolderList = [f for f in os.listdir(dir) if not file_is_hidden(f) and isfileValid(f)]
    
    return fileFolderList

# list of [name] of files does not include directories
def makeFileList(dir):

    fflist = makeFileFolderList(dir)
    list = []
    for file in fflist:
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


def makeCompactExtList(dir):

    filelist = makeFilePathList(dir)
    extList = []

    for i in range(0,len(filelist)):
        j = 0 
        has_duplicates = False
        ext = os.path.splitext(filelist[i])[1].lower()

        while (j < len(extList)) and has_duplicates == False:

            if ext == extList[j]:
                has_duplicates = True
            j += 1
        if not has_duplicates and ext != "" and ext != ".DS_Store":
            extList.append(ext)

    return extList
# returns a list of the file ext's of the given directory (w/o duplicates)
# def file_type_list(dir):
 
#     #fileList = next(os.walk(dir))[2]
#     fileList = makeFileFolderList(dir)

#     fileExtList = []
#     fileNameList = []
    
    
#     for i in range(0,fileCounter(dir)):

#         splitFileElemList = os.path.splitext(fileList[i])
#         print("typelist,filelist: "+str(fileList[i]))
#         ext = splitFileElemList[1].lower()
#         print("filetypepre: "+str(ext))
#         #print(ext)
#         j = 0
#         has_duplicates = False

#         while (j < len(fileExtList)) and has_duplicates == False:

#             if len(fileExtList) > j and fileExtList[j] == ext:
#                 has_duplicates = True
            
#             j = j + 1

#         if has_duplicates == False:
#             if ext != "": # dont let folders which show up as "" be counted as an ext.
#                 fileExtList.append(ext)
#         fileNameList.append(splitFileElemList[0])
#     print("\n")
#     print("filetypelen: " +str(len(fileExtList)))
#     print("\n")
#     print("fileextlist,typelist: "+str(fileExtList))
#     print("\n")

#     #
#     # print(fileNameList)
#     print("\n")
#     return fileExtList

#makes a list of the extentions like file_type_list() excepts it includes duplicates
def makeExtList(dir):

    fileList = makeFilePathList(dir)

    fileExtList = []
    #print("makeextfilecount: "+str(fileCounter(dir)))
    for i in range(0,len(fileList)):

        splitFileElemList = os.path.splitext(fileList[i])

        ext = splitFileElemList[1].lower()
        #print("makextPre: " +str(ext))
        if ext != "" and ext != ".DS_Store":
            fileExtList.append(ext)
        
    return fileExtList

# checks if a directory(folder) is of a certain type(ext) in order to be of type iS all of its files must be of the same type 
# hence a meethod must be made that fixes folders which include wrong file types TODO
def dir_isType(dir,type):

    isType = True

    return isType

# makes the Ext name of the folder
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

#makes a folder at the specified path and with the given name
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

    folderList = makeFolderList(dir)
    extList = makeCompactExtList(dir) #no duplicates
    fileList = makeFileList(dir)
    ffList = makeFileFolderList(dir)

    dirListLen = len(folderList)

    print("\nextlist:folderlist:  "+str(extList) +" : " +str(folderList))
    folderCreated = False

    for i in range(0,len(extList)):

        folderExists = False

        j = 0
        while  (folderExists == False) and (j < len(folderList)):
        
            if makeFolderName(extList[i]) == folderList[j]:

                folderExists = True

            j += 1

        if folderExists == False: # folder creation

            makeFolder(dir, makeFolderName(extList[i]))
            folderCreated = True


    return folderCreated


#handles the movement of the files from the dir to the corresponding folders existing from the folderManager method
def fileManager(dir):

    folderList = makeFolderList(dir) 
    fileList = makeFilePathList(dir)
    #ffList = makeFileFolderList(dir)
    extlist = makeExtList(dir)#has duplicates

    error = None

    print("extList: "+str(extlist)+" : "+str(folderList)+" : "+str(fileList))
    for i in range(0,len(fileList)):

        foundFolder = False
        j = 0
        while not foundFolder:
            print("i/j " +str(i)+" : "+str(j))
            if makeFolderName(extlist[i]) == folderList[j]:

                error = fileMove(os.path.join(dir,fileList[i]), os.path.join(dir,folderList[j]))
                foundFolder = True
            j += 1
        
    return error

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
        makeCompactExtList(dir)(dir)

    else:
        print("\n")

        #dir = "/Users/kuraizen/Documents/Scripts/file_sorter/fs_test"
        dir = "/Users/kuraizen/Downloads"
        makeCompactExtList(dir) #temp only saved here to not have to retype
        #file_type_list("/Users/kuraizen/Downloads")
        #folderCounter("/Users/kuraizen/Downloads")
        folderCounter(dir)

        print("Managing folders...\n")
        folderManager(dir)
        print("Managing Files...\n")
        fileManager(dir)
        print("count: "+str(fileCounter(dir)))
        print("\nfilepathList: "+str(makeFilePathList(dir)))
        print("\nmakefileFolder: "+str(makeFolderList(dir)))
        print("\nwalk: "+str(next(os.walk(dir))[1]))
        print("End of Program\n")
if __name__ == "__main__":
    main()