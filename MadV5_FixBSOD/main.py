import wmi
import datetime
import os

os.system("title MadUI V5 - FixBSOD")
print("Welcome to BSOD Fixer.")
print("")
print("To ensure that this process goes smoothly, please disable your Anti-Virus.")
os.system("pause")
os.system("cls")

wmi_service = wmi.WMI()

hotfixes = [hotfix for hotfix in wmi_service.Win32_QuickFixEngineering() if datetime.datetime.strptime(hotfix.InstalledOn, '%m/%d/%Y').date() >= datetime.date(2023, 1, 1)]

commands = [f'wusa /uninstall /kb:{hotfix.HotFixID.replace("KB", "")} /norestart' for hotfix in hotfixes]

for command in commands:
    print(command)
    os.system(command)

os.system("cls")
os.system("color 2")
print("Process Completed!")
print("")
print("Please restart your System.")
os.system("pause")
