import shutil
import os
import subprocess
import pyautogui


def dir(folder_nm):
    files_list = os.listdir(folder_nm)
    print(files_list)
    return files_list

def delete(file_nm):
    try:
        os.remove(file_nm)
        return "delete Succesfuly"
    except:
        return "Error"

def copy(File_from,Folder_to):
    try:
        shutil.copy(File_from,Folder_to)
        return "copy Succesfuly"
    except:
        return "Error"

def execute(Program_nm):
    try:
        subprocess.call(Program_nm)
        return "execute Succesfuly"
    except:
        return "Error"

def screenshot():
    try:
        image6 = pyautogui.screenshot()
        image6.save(r'C:\TestFolder\image6.png')
        return "screenshot Succesfuly"
    except:
        return "Error"

def send_screenshot():
    return (r'C:\TestFolder')


#screenshot()
#msg = send_screenshot()
#execute(r'C:\Windows\System32\notepad.exe')
#copy('C:\MoveHere\IDK.txt','C:\TestFolder')
#delete('C:\MoveHere\IDK.txt')
#dir('C:\MoveHere')
#msg = copy('C:\TestFolder\IDK.txt','C:\MoveHere')
#dir('C:\TestFolder')
#delete('C:\TestFolder\IDK.txt')
#dir('C:\MoveHere')
#print(msg)
