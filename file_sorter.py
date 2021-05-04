import os

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

# counts the num of folders
def folderCounter(dir):

    dirlen = 0

    fileFolderList = os.listdir(dir)

    for f in fileFolderList:
        #print(str(os.path.isdir(os.path.join(dir,f)))+" : " +str(f))
        if os.path.isdir(os.path.join(dir,f)): # we cannot do just do if f becuase isDir need an aboslute $path ie /Home/Users/folderName

            dirlen += 1
    

    #print("listing dir: "+str(os.listdir(dir)))
    
    print("folder count: " + str(dirlen))
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





# returns a list of the file ext's of the given directory
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


# checks if a directory is of a certain type(ext) 
def dir_isType(dir,type):

    isType = True




    return isType

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
        file_type_list("/Users/kuraizen/Documents/Scripts/file_sorter/fs_test")
        #file_type_list("/Users/kuraizen/Downloads")
        #folderCounter("/Users/kuraizen/Downloads")
        folderCounter("/Users/kuraizen/Documents/Scripts/file_sorter/fs_test")



if __name__ == "__main__":
    main()