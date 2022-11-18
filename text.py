import time
from pyautogui import press, typewrite

cmd = ["hunt t", "chop", ""]
paused = False


def text_to_seconds(text):
    split_text = text.split()
    seconds = 0
    for x, y in enumerate(reversed(split_text)):
        if x < 3:
            seconds = seconds + (int(y[:-1]) * 60 ** x)
        else:
            seconds = seconds + int(y[:-1]) * 86400
    return seconds


def cd_cleanup(text):
    cd_time = []
    for x in text:
        split_list = x['value'].split("\n")
        for y in split_list:
            if ":clock4" in y:
                cd_time.append(text_to_seconds(y.split("**")[3]))
            else:
                cd_time.append(0)
    return cd_time


def area_check(area):
    area = int(area)
    f = ""
    h = "hunt t"
    w = "chop"
    if area < 3:
        w = "chop"
    elif area < 6:
        w = "axe"
    elif area < 8:
        w = "ladder"
    elif area == 8:
        w = "bowsaw"
    elif area >= 9:
        w = "chainsaw"
    if area >= 4:
        f = "farm"
    if area >= 13:
        h = "hunt t h"
    
    print("Set area to", area)
    return [h, w, f]


def hunt():
    typewrite("rpg " + cmd[0])
    press('enter')
    print("Hunt Executed")


def adventure():
    typewrite("rpg adventure")
    press('enter')
    print("Adventure Executed")


def buy():
    typewrite("rpg buy ed lb")
    press('enter')
    print("Buy Executed")


def work():
    typewrite("rpg " + cmd[1])
    press('enter')
    print("Work Executed")


def farm():
    typewrite("rpg " + cmd[2])
    press('enter')
    print("Farm Executed")


def daily():
    typewrite("rpg daily")
    press('enter')
    print("Daily Executed")


def parse(event):
    global cmd
    global paused
    if event['d']['guild_id'] == '1008332353686483016' and not paused:
        if event['d']['author']['username'] == "Navi":
            if "/hunt" in event['d']['content']:
                hunt()
            if "/adventure" in event['d']['content']:
                adventure()
            if cmd[1] in event['d']['content']:
                work()
            if "/farm" in event['d']['content']:
                farm()
            if "/buy" in event['d']['content']:
                buy()
            if "/daily" in event['d']['content']:
                daily()
        if event['d']['author']['username'] == "DieRandomDie":
            if "set area" in event['d']['content']:
                cmd = area_check(event['d']['content'].split()[-1])
            if "set seed" in event['d']['content']:
                cmd[2] = "farm " + event['d']['content'].split()[-1]
            if "stop auto" in event['d']['content']:
                print("Received kill command. Stopping autos.")
                typewrite("stopped")
                press('enter')
                paused = True
    if event['d']['guild_id'] == '1008332353686483016' and paused:
        if event['d']['author']['username'] == "DieRandomDie":
            if "start auto" in event['d']['content']:
                print("Received resume command. Starting autos.")
                typewrite("starting")
                press('enter')
                paused = False
