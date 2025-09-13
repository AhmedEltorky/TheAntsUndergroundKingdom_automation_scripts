import pyautogui
import pydirectinput
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

watering_count = 24  # number of plants to water

start_x = 510
start_y = 283

water_icon_x = 40
water_icon_y = 847

water_dot_x = 318
water_dot_y = 508

back_icon_x = 170
back_icon_y = 915

delta_y = 32

# Initial delay to allow user to switch to the game window
print("You have 5 seconds to switch to the game window...")
time.sleep(5)
print("Starting watering...")

# pyautogui.moveTo(start_x, start_y, duration=1)
# pyautogui.moveTo(start_x, start_y + (watering_count - 1) * delta_y, duration=1)


while watering_count > 0:
    pyautogui.moveTo(start_x, start_y, duration=1)
    time.sleep(1)
    pydirectinput.click()
    pyautogui.moveTo(water_icon_x, water_icon_y, duration=1)
    time.sleep(1)
    pydirectinput.click()
    pyautogui.moveTo(water_dot_x, water_dot_y, duration=1)
    time.sleep(1)
    pydirectinput.click()
    pyautogui.moveTo(back_icon_x, back_icon_y, duration=1)
    time.sleep(1)
    pydirectinput.click()

    pyautogui.moveTo(start_x, start_y + delta_y, duration=1)
    time.sleep(1)
    pyautogui.dragTo(start_x, start_y - delta_y, duration=1)
    time.sleep(1)

    watering_count -= 1

# TODO: handle the remaining waterings
