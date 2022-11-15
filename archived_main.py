from tkinter import *
from tkinter.ttk import *
from time import strftime, sleep, time
from threading import Timer
from pyautogui import press, typewrite

next_hunt_time = 40
next_work_time = 196
next_farm_time = 391

huntcd = 40
workcd = 196
farmcd = 391

huntcmd = "rpg hunt t"

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

farmcmd = "rpg farm"


def time_check(cmdtype):
    global next_hunt_time
    global next_work_time
    global next_farm_time

    total = 0

    if cmdtype == "hunt":
        if abs(time()+huntcd-next_work_time) < 1.2:
            total = total + 1.2
            print("hunt +1")
        if abs(time()+huntcd-next_farm_time) < 1.2:
            total = total + 1.2
            print("hunt +1")
    elif cmdtype == "work":
        if abs(time()+workcd-next_hunt_time) < 1.2:
            total = total + 1.2
            print("work +1")
        if abs(time()+workcd-next_farm_time) < 1.2:
            total = total + 1.2
            print("work +1")
    elif cmdtype == "farm":
        if abs(time()+farmcd-next_hunt_time) < 1.2:
            total = total + 1.2
            print("farm +1")
        if abs(time()+farmcd-next_work_time) < 1.2:
            total = total + 1.2
            print("farm +1")
    print(cmdtype, ": ", total)
    return total


# commands
def hunt(cmd, cd):
    typewrite(cmd)
    press('enter')
    global next_hunt_time
    cd = cd + time_check("hunt")
    next_hunt_time = time() + cd
    hunt_timer = Timer(cd, hunt, [huntcmd, huntcd])
    hunt_timer.start()


def work(cmd, cd):
    typewrite(cmd)
    press('enter')
    global next_work_time
    cd = cd + time_check("work")
    next_work_time = time() + cd
    work_timer = Timer(cd, work, [workcmd, workcd])
    work_timer.start()


def farm(cmd, cd):
    typewrite(cmd)
    press('enter')
    global next_farm_time
    cd = cd + time_check("farm")
    next_farm_time = time() + cd
    farm_timer = Timer(cd, farm, [farmcmd, farmcd])
    farm_timer.start()


root = Tk()
root.title('Discord Bot Botter')


hunt_label = Label(root, font=('calibri', 40, 'bold'),background='black',foreground='white')
work_label = Label(root, font=('calibri', 40, 'bold'),background='black',foreground='white')
farm_label = Label(root, font=('calibri', 40, 'bold'),background='black',foreground='white')

# Placing clock at the centre
# of the tkinter window
hunt_label.pack(anchor='center')
work_label.pack(anchor='center')
farm_label.pack(anchor='center')


sleep(3)
hunt(huntcmd, huntcd)
sleep(1.2)
work(workcmd, workcd)
sleep(1.2)
if area >= 4:
    farm(farmcmd, farmcd)


def update_hunt():
    hunt_string = '%.1f'%(next_hunt_time - time())
    hunt_label.config(text="Hunt: "+hunt_string)
    hunt_label.after(90, update_hunt)


def update_work():
    work_string = '%.1f'%(next_work_time - time())
    work_label.config(text="Work: "+work_string)
    work_label.after(90, update_work)


def update_farm():
    if area >= 4:
        farm_string = '%.1f'%(next_farm_time - time())
    else:
        farm_string = "Not Farming"
    farm_label.config(text="Farm: "+farm_string)
    farm_label.after(90, update_farm)


hunt_label.pack(anchor='center')
work_label.pack(anchor='center')
farm_label.pack(anchor='center')
update_hunt()
update_work()
update_farm()
mainloop()
