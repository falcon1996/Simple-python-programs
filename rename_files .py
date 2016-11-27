import os                                                            # os module has fn listdir which lists everything in directory
def rename_files():
    # get file names from folder
    file_list = os.listdir(r"C:\Users\DHRUV PARASHAR\Desktop\prank") # r stands fo raw path
    print (file_list)
    
    # for each file, rename filename
    saved_path = os.getcwd()                                          # cwd stands for current working directory
    print ("current working directory is " + saved_path)
    os.chdir(r"C:\Users\DHRUV PARASHAR\Desktop\prank")                # chdir stands for change directory
    for file_name in file_list:
        print ("old name -" + file_name)
        print ("new name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789")) # first argument is first file name and scond argument is second file name
                                                                      # in file_name.translate() first argument is a table linking 2 sets to each other and
                                                                      # second argument is string of characters we want to remove
                                                                      
    os.chdir(saved_path)                                              # to make program we need to come back to location where program is stored
rename_files()

# if we try to rename a file to a name that already exists in the folder it will throw an error
