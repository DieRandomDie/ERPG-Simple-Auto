import time
import tkinter as tk
from threading import Timer
from pyautogui import press, typewrite

next_hunt_time = 0
next_work_time = 0
next_farm_time = 0
huntcmd = "rpg hunt t"
huntcd = 40

area = int(input("Area?\n> "))
if area < 3:
    workcmd = "rpg chop"
elif area < 6:
    workcmd = "rpg axe"
elif area < 8:
    workcmd = "rpg ladder"
elif area == 8:
    workcmd = "rpg bowsaw"
elif area >= 9:
    workcmd = "rpg chainsaw"

workcd = 196
farmcmd = "rpg farm"
farmcd = 391


def hunt(cmd, cd):
    typewrite(cmd)
    press('enter')
    global next_hunt_time
    next_hunt_time = time.time()+cd
    hunt_timer = Timer(cd, hunt, [huntcmd, huntcd])
    hunt_timer.start()


def work(cmd, cd):
    typewrite(cmd)
    press('enter')
    global next_work_time
    next_work_time = time.time()+cd
    work_timer = Timer(cd, work, [workcmd, workcd])
    work_timer.start()


def farm(cmd, cd):
    typewrite(cmd)
    press('enter')
    global next_farm_time
    next_farm_time = time.time()+cd
    farm_timer = Timer(cd, farm, [farmcmd, farmcd])
    farm_timer.start()


window = tk.Tk()
time.sleep(3)
hunt(huntcmd, huntcd)
time.sleep(1.2)
work(workcmd, workcd)
time.sleep(1.2)
if area >= 3:
    farm(farmcmd, farmcd)


#while True:
#    hunt_time_remaining = '%.2f'%(next_hunt_time - time.time())
#    work_time_remaining = '%.2f'%(next_work_time - time.time())
#    if area >= 3:
#        farm_time_remaining = '%.2f'%(next_farm_time - time.time())
#    else
#        farm_time_remaining = "Not Farming"
#    time.sleep(.05)


