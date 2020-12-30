import pyautogui
import time
import random


# Used to start the game.
def start_game():
    pyautogui.click(22, 1060)
    pyautogui.typewrite("bluestacks")
    pyautogui.typewrite(["enter"])
    time.sleep(5)
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/maximize.png")))
    time.sleep(15)
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/brownDust.png")))
    time.sleep(90)


# Collect daily rewards after login.
def collect_daily():
    for i in range(5):
        pyautogui.click(1625, 701)
        time.sleep(1 + random.randint(0, 1000) / 1000)
    pyautogui.click(1500, 976)
    time.sleep(3 + random.randint(0, 1000) / 1000)


# Used to farm gear.
def farm_gear(loop_count):
    # enter from menu
    pyautogui.click(random.randint(1481, 1530), random.randint(869, 954))
    time.sleep(3 + random.randint(0, 1000)/1000)
    pyautogui.click(random.randint(648, 867), random.randint(629, 879))
    time.sleep(3 + random.randint(0, 1000) / 1000)
    # repeat the stage
    for gear_loop_var1 in range(loop_count):
        pyautogui.click(random.randint(1028, 1373), random.randint(904, 961))
        time.sleep(3 + random.randint(0, 1000) / 1000)
        pyautogui.click(random.randint(699, 1167), random.randint(887, 939))
        time.sleep(3 + random.randint(0, 1000) / 1000)
        pyautogui.click(random.randint(986, 1310), random.randint(869, 905))
        time.sleep(8 + random.randint(0, 1000) / 1000)
        pyautogui.click(random.randint(1342, 1661), random.randint(936, 981))
        time.sleep(50 + random.randint(0, 1000) / 150)
        pyautogui.click(random.randint(1456, 1637), random.randint(927, 964))
        time.sleep(7 + random.randint(0, 1000) / 1000)
    pyautogui.click(random.randint(1493, 1594), random.randint(179, 192))
    # repeat gear collect
    for gear_loop_var2 in range(loop_count):
        time.sleep(4 + random.randint(0, 1000) / 1000)
        pyautogui.click(random.randint(1640, 1745), random.randint(335, 396))
        time.sleep(4 + random.randint(0, 1000) / 1000)
        pyautogui.click(random.randint(623, 818), random.randint(899, 948))
        time.sleep(4 + random.randint(0, 1000) / 1000)
        pyautogui.click(random.randint(822, 1063), random.randint(918, 952))
    # exit to menu
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(random.randint(172, 203), random.randint(70, 100))
    time.sleep(15 + random.randint(0, 1000) / 1000)


def recruit():
    pyautogui.click(1030, 928)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(820, 350)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1665, 900)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1300, 621)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1092, 662)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1605, 956)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1634, 190)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1619, 908)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    # legend pull
    pyautogui.click(1089, 892)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1666, 845)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1087, 679)
    time.sleep(1 + random.randint(0, 1000) / 1000)
    pyautogui.click(1634, 956)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1624, 907)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(172, 83)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    # normal pull
    pyautogui.click(824, 916)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1465, 428)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1666, 845)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1087, 679)
    time.sleep(1 + random.randint(0, 1000) / 1000)
    pyautogui.click(1634, 956)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1624, 907)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(172, 83)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    # exit
    pyautogui.click(169, 88)
    time.sleep(15 + random.randint(0, 1000) / 1000)


def send_gift():
    pyautogui.click(616, 935)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(827, 549)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1560, 174)
    time.sleep(1 + random.randint(0, 1000) / 1000)
    pyautogui.click(1560, 174)
    time.sleep(1 + random.randint(0, 1000) / 1000)
    pyautogui.click(165, 79)
    time.sleep(3 + random.randint(0, 1000) / 1000)


def guild():
    pyautogui.click(616, 935)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1053, 538)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(820, 650)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(473, 932)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1632, 316)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1403, 946)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1085, 661)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(165, 79)
    time.sleep(6 + random.randint(0, 1000) / 1000)
    pyautogui.click(165, 79)
    time.sleep(15 + random.randint(0, 1000) / 1000)


def crystal_dungeon():
    # enter from menu
    pyautogui.click(random.randint(1481, 1530), random.randint(869, 954))
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(807, 358)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1715, 489)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(909, 886)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1091, 678)
    time.sleep(15 + random.randint(0, 1000) / 1000)


def world_boss(count):
    # enter from menu
    pyautogui.click(random.randint(1481, 1530), random.randint(869, 954))
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(409, 815)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1680, 122)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    for world_loop_var in range(count):
        pyautogui.click(1592, 912)
        time.sleep(1 + random.randint(0, 1000) / 1000)
    for world_loop_var2 in range(count):
        pyautogui.click(939, 819)
        time.sleep(3 + random.randint(0, 1000) / 1000)
        pyautogui.click(1551, 962)
        time.sleep(3 + random.randint(0, 1000) / 1000)
        pyautogui.click(939, 819)
        time.sleep(6 + random.randint(0, 1000) / 1000)
        pyautogui.click(1542, 951)
        time.sleep(60 + random.randint(0, 1000) / 150)
        pyautogui.click(1553, 943)
        time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(173, 79)
    time.sleep(15 + random.randint(0, 1000) / 1000)


def collect_rewards():
    # enter from menu
    pyautogui.click(random.randint(1481, 1530), random.randint(869, 954))
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(807, 358)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1057, 882)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1057, 882)
    time.sleep(1 + random.randint(0, 1000) / 1000)
    pyautogui.click(1576, 140)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1540, 404)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1606, 882)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1653, 883)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1385, 919)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1288, 776)
    time.sleep(5 + random.randint(0, 1000) / 1000)
    # dust island thingy
    pyautogui.click(1405, 347)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(648, 859)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    for i in range(3):
        pyautogui.click(1639, 935)
        time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1087, 516)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(648, 859)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    for i in range(3):
        pyautogui.click(1639, 935)
        time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(812, 576)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1467, 844)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    for i in range(3):
        pyautogui.click(1639, 935)
        time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(475, 735)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1467, 844)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    for i in range(3):
        pyautogui.click(1639, 935, 844)
        time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(502, 392)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(1467, 844)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    for i in range(3):
        pyautogui.click(1639, 935)
        time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(175, 87)
    time.sleep(12 + random.randint(0, 1000) / 1000)
    pyautogui.click(476, 937)
    time.sleep(3 + random.randint(0, 1000) / 1000)
    for i in range(8):
        pyautogui.click(1602, 409)
        time.sleep(3 + random.randint(0, 1000) / 1000)


time.sleep(3)
start_game()
collect_daily()
crystal_dungeon()
farm_gear(4)
recruit()
send_gift()
guild()

