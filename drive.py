from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os 

print (os.getcwd()) # to check the current working directory, if the current working directory above is different than your folder containing the script then change the working directory to your script directory.
os.chdir('F:/Nirma/SEM-7/Minor/Minor Project/')

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = "183g4p4DM83JSooUwmQG80y7eZxeliPyB"

directory = "F:/Nirma/SEM-7/Minor/Minor Project/data"

# for f in os.listdir(directory):
#     filepath = os.path.join(directory, f)
#     gfile = drive.CreateFile({'parents': [{'id': folder}], 'title': f})
#     gfile.SetContentFile(filepath)
#     gfile.Upload()

file_list = drive.ListFile({'q': f"'{folder}' in parents and trashed=false"}).GetList()

os.chdir('F:/Nirma/SEM-7/Minor/Minor Project/Drive/')
for file in file_list:
    file.GetContentFile(file['title'])
    print(file['title'])