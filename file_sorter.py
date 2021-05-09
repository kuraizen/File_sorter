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



def makeFileFolderList(dir):

    fileFolderList = [f for f in os.listdir(dir) if not file_is_hidden(f)]
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

#like makeFileList() except includes the whole filename
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
    
    # print(str(dirlen) + "\n")
    print(dirFilelen)
    print("\n")
    #print(next(os.walk(dir))[2])
    print("\n")
    return dirFilelen

# returns a list of the file ext's of the given directory (w/o duplicates)
def file_type_list(dir):

    
    fileList = next(os.walk(dir))[2]

    fileExtList = []
    fileNameList = []
    
    
    for i in range(fileCounter(dir)):

        splitFileElemList = os.path.splitext(fileList[i])

        ext = splitFileElemList[1].lower()
        #print(ext)
        j = 0
        has_duplicates = False

        while (j < len(fileExtList)) and has_duplicates == False:

            if len(fileExtList) > j and fileExtList[j] == ext:
                has_duplicates = True
            
            j = j + 1

        if has_duplicates == False:
            if ext != "": # dont let folders which show up as "" be counted as an ext.
                fileExtList.append(ext)
        fileNameList.append(splitFileElemList[0])
    print("\n")
    print(len(fileExtList))
    print("\n")
    print(fileExtList)
    print("\n")

    #
    # print(fileNameList)
    print("\n")
    return fileExtList

#makes a list of the extentions like file_type_list() excepts it includes duplicates
def makeExtList(dir):

    fileList = next(os.walk(dir))[2]

    fileExtList = []
    
    for i in range(fileCounter(dir)):

        splitFileElemList = os.path.splitext(fileList[i])

        ext = splitFileElemList[1].lower()

        if ext != "":
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
    extList = file_type_list(dir)
    fileList = makeFileList(dir)
    ffList = makeFileFolderList(dir)

    dirListLen = len(folderList)

    print("extlist:folderlist:  "+str(extList) +" : " +str(folderList))
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
    extlist = makeExtList(dir)

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
        file_type_list(dir)

    else:
        print("\n")

        dir = "/Users/kuraizen/Documents/Scripts/file_sorter/fs_test"
        file_type_list(dir) #temp only saved here to not have to retype
        #file_type_list("/Users/kuraizen/Downloads")
        #folderCounter("/Users/kuraizen/Downloads")
        folderCounter(dir)

        print("Managing folders...\n")
        folderManager(dir)
        print("Managing Files...\n")
        fileManager(dir)
        print("End of Program\n")
if __name__ == "__main__":
    main()