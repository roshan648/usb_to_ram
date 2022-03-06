import os
import signal
os.system("clear")
text = 'TYech5_term'
os.system("cfonts "+text+" -f slick -c blue")
print("""\033[3;35;47m<<>>
Website:www.tyech5-ty.blogspot.com
GitHub :www.github/roshan648.com
Code Author:G.A.ROSHAN MELVIN
>><<

| 0.Exit
| 1.Shell
| 2.USB to RAM
""")#Edit this row for your identification
inp = input("Enter your option:")
if inp == "0":
   os.kill(os.getppid(), signal.SIGHUP)
elif inp == "1":
  username = "rockroshan" #Edit this user name
  os.system("su - "+username) 
elif inp == "2":
  os.system("clear")
  print("|  0.New setup")
  print("|  1.USB start")
  print("|  2.USB end")
  inp = input("Enter your option:")
  if inp == "0":
    print("")#
    cmd1 = 'sudo fdisk -l'
    os.system(cmd1)
    print("")#
    inp = input("Enter Disk Name (eg:sdc):")
    print("")#
    cmd2 = "sudo umount /dev/"+ inp
    os.system(cmd2)
    print("")#
    cmd3 = "sudo mkswap /dev/"+ inp
    os.system(cmd3)
    print("")#
    cmd4 = "sudo swapon -p 32767 /dev/"+ inp
    os.system(cmd4)
    print("")#
    cmd5 = "cat /proc/swaps"
    os.system(cmd5)
    print("")#
    inp = input("Enter to continue...")
    if inp == "":
      os.system("python3 usbtoram.py")    
  elif inp == "1":
    print("")#
    cmd1 = 'sudo fdisk -l'
    os.system(cmd1)
    print("")#
    inp = input("Enter Disk Name (eg:sdc):")
    print("")#
    cmd2 = "sudo swapon -p 32767 /dev/"+ inp
    os.system(cmd2)
    print("")#
    cmd3 = "cat /proc/swaps"
    os.system(cmd3)
    print("")#
    inp = input("Enter to continue...")
    if inp == "":
      os.system("python3 usbtoram.py")
  elif inp == "2":
    print("")#
    cmd1 = 'sudo fdisk -l'
    os.system(cmd1)
    print("")#
    inp = input("Enter Disk Name (eg:sdc):")
    print("")#
    cmd2 = "sudo swapoff /dev/"+inp
    os.system(cmd2)
    print("")#
    cmd3 = "cat /proc/swaps"
    os.system(cmd3)
    print("")#
    inp = input("Enter to continue...")
    if inp == "":
      os.system("python3 usbtoram.py")     
  else:
    os.system("python3 usbtoram.py") 
#add your extra functions here
#Dont edit the else at the down
else:
  os.system("python3 usbtoram.py")
