import shutil
import os
import subprocess


def dir(folder_nm):
    files_list = os.listdir(folder_nm)
    print(files_list)
    return files_list

def delete(file_nm):
    os.remove(file_nm)

def copy(File_from,File_to):
    shutil.copy(File_from,File_to)

def execute(Program_nm):
    subprocess.call(Program_nm)

execute(r'C:\Windows\System32\notepad.exe')
copy('C:\MoveHere\IDK.txt','C:\TestFolder')
delete('C:\MoveHere\IDK.txt')
dir('C:\MoveHere')
copy('C:\TestFolder\IDK.txt','C:\MoveHere')
dir('C:\TestFolder')
delete('C:\TestFolder\IDK.txt')
dir('C:\MoveHere')

