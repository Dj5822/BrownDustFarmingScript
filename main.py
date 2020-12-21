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
    time.sleep(15)


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
        time.sleep(6 + random.randint(0, 1000) / 1000)
        pyautogui.click(random.randint(1342, 1661), random.randint(936, 981))
        time.sleep(40 + random.randint(0, 1000) / 150)
        pyautogui.click(random.randint(1456, 1637), random.randint(927, 964))
        time.sleep(6 + random.randint(0, 1000) / 1000)
    pyautogui.click(random.randint(1493, 1594), random.randint(179, 192))
    # repeat gear collect
    for gear_loop_var2 in range(loop_count):
        time.sleep(3 + random.randint(0, 1000) / 1000)
        pyautogui.click(random.randint(1640, 1745), random.randint(335, 396))
        time.sleep(3 + random.randint(0, 1000) / 1000)
        pyautogui.click(random.randint(623, 818), random.randint(899, 948))
        time.sleep(3 + random.randint(0, 1000) / 1000)
        pyautogui.click(random.randint(822, 1063), random.randint(918, 952))
    # exit to menu
    time.sleep(3 + random.randint(0, 1000) / 1000)
    pyautogui.click(random.randint(172, 203), random.randint(70, 100))


start_game()
farm_gear()
