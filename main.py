import os
import shutil

path = "C:/Users/david/downloads/"
files = os.listdir(path)

for file in files:
    if os.path.isdir(path+file):
        continue
    print(file)
    filename, extension =  os.path.splitext(file)
    extension = extension[1:]

    folderType = "none"
    if extension == "pdf" or extension == "doc" or extension == "docx" or extension == "ppt" or extension == "pptx" or extension == "txt":
        folderType = "documents"
    elif extension == "img" or extension == "jpeg" or extension == "jpg" or extension == "png" or extension == "gif":
        folderType = "images"
    elif extension == "mp3":
        folderType = "audio"
    elif extension == "mp4":
        folderType = "video"
    elif extension == "exe" or extension == "msi" or extension == "apk" or extension == "app" or extension == "bat" or extension == "sh":
        folderType = "executables"
    else:
        folderType = "misc"

    if(folderType == "documents"):
        if(os.path.exists(path+'Documents')):
            shutil.move(path+file, path+'Documents/'+file)
        else:
            os.makedirs(path+'Documents')
            shutil.move(path+file, path+'Documents/'+file)
    elif(folderType == "images"):
        if(os.path.exists(path+'Images')):
            shutil.move(path+file, path+'Images/'+file)
        else:
            os.makedirs(path+'Images')
            shutil.move(path+file, path+'Images/'+file)
    elif(folderType == "audio"):
        if(os.path.exists(path+'Audio')):
            shutil.move(path+file, path+'Audio/'+file)
        else:
            os.makedirs(path+'Audio')
            shutil.move(path+file, path+'Audio/'+file)
    elif(folderType == "video"):
        if(os.path.exists(path+'Video')):
            shutil.move(path+file, path+'Video/'+file)
        else:
            os.makedirs(path+'Video')
            shutil.move(path+file, path+'Video/'+file)
    elif(folderType == "executables"):
        if(os.path.exists(path+'Executables')):
            shutil.move(path+file, path+'Executables/'+file)
        else:
            os.makedirs(path+'Executables')
            shutil.move(path+file, path+'Executables/'+file)
    elif(folderType == "misc"):
        if(os.path.exists(path+'Misc')):
            shutil.move(path+file, path+'Misc/'+file)
        else:
            os.makedirs(path+'Misc')
            shutil.move(path+file, path+'Misc/'+file)