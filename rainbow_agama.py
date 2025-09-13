import pyautogui
import pydirectinput
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

attack_icon_x = 360
attack_icon_y = 500

ProUnit_x = 185
ProUnit_y = 470

march_x = 500
march_y = 918

rally_count = 5
wait_rally_time = 70  # in seconds

# Initial delay to allow user to switch to the game window
print("You have 5 seconds to switch to the game window...")
time.sleep(5)

# Click on the Rainbow Anagma to select it before running the script
while rally_count > 0:
    pyautogui.moveTo(attack_icon_x, attack_icon_y, duration=2)
    time.sleep(1)
    pydirectinput.click()

    pyautogui.moveTo(ProUnit_x, ProUnit_y, duration=1)
    time.sleep(1)
    pydirectinput.click()

    pyautogui.moveTo(march_x, march_y, duration=1)
    time.sleep(1)
    pydirectinput.click()

    rally_count -= 1
    print(f"Rally count: {rally_count}")

    # Wait for 2 minutes before the next rally
    time.sleep(wait_rally_time)

print("Rallying completed.")
# Note: Adjust the coordinates and wait times as necessary for your specific game and setup.
