import os 
if(not os.path.exists("data")):
    
#   DIRECTORIES BN JYEGI 99 TK
    os.mkdir("file_41.1")
for i in range(0, 100):
    os.mkdir(f"data/day{i+1}")
    # os.rename(f"data/day{i+1}" ,f"data/newFile{i+1}")
    os.mkdir(f"")


#   SAARE FOLDERS PRINT HO JAYENGE
    folders = os.listdir("data")
    for folder in folders :
        print (folder)             # folder print kr dega
        print(os.listdir(folder))  # folders ke andr ki file bhi bata dega

# KONSI DIR M HO
print(os.getcwd())
os.chdir("PATH")   # Dir ka path change krna h toh 