import requests
import os
import zipfile
import subprocess
import shutil

os.system("title MadUI V5 - Toolkit")
print("Welcome to MadUI Toolkit (Basic Fixer)")
print("")
print("To ensure that this process goes smoothly, please disable your Anti-Virus.")
os.system("pause")
os.system("cls")

print("Downloading C++ Redist...")
URL = "https://cdn.discordapp.com/attachments/1050786304637546498/1092154791561535539/Visual-C-Runtimes-All-in-One-Feb-2023.zip"
response = requests.get(URL)
open("redist_mad.zip", "wb").write(response.content)

print("Downloading DX Redist...")
URL = "https://cdn.discordapp.com/attachments/1050786304637546498/1091747835474628679/dxwebsetup.exe"
response = requests.get(URL)
open("dxwebsetup.exe", "wb").write(response.content)

print("Downloading SSFCU Files...")
URL = "https://cdn.discordapp.com/attachments/1050786304637546498/1092154480067354754/SSFCU.zip"
response = requests.get(URL)
open("SSFCU.zip", "wb").write(response.content)

print("Downloading Extra Drivers...")
URL = "https://cdn.discordapp.com/attachments/1050786304637546498/1092889537384030318/ndp48-web.exe"
response = requests.get(URL)
open("ndp48-web.exe", "wb").write(response.content)

print("Extracting Files...")
with zipfile.ZipFile('redist_mad.zip', 'r') as zip_ref:
    zip_ref.extractall('redist')

with zipfile.ZipFile('SSFCU.zip', 'r') as zip_ref:
    zip_ref.extractall('SSFCU')

print("Moving SSFCU to %temp%...")
folder_path = "SSFCU"
temp_dir = os.environ.get('TEMP')

if os.path.exists(os.path.join(temp_dir, folder_path)):
    shutil.rmtree(os.path.join(temp_dir, folder_path))

shutil.move(folder_path, temp_dir)

os.system("cls")
subprocess.call(['redist\\install_all.bat'])
os.system("cls")
print("Please proceed with the installation on the new window...")
os.system("dxwebsetup.exe")
os.system("ndp48-web.exe")

os.remove("dxwebsetup.exe")
os.remove("redist_mad.zip")
os.remove("SSFCU.zip")
os.remove("ndp48-web.exe")
os.system("rmdir /s /q redist")
os.system("cls")

os.system("color 2")
print("Process Completed!")
os.system("pause")