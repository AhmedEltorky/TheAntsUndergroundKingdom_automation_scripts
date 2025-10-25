import pyautogui
import pydirectinput
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

pangolin_x = 292
pangolin_y = 430

rally_x = 380
rally_y = 520

attack_x = 299
attack_y = 526

ProUnit_x = 185
ProUnit_y = 470

march_x = 500
march_y = 918

confirm_x = 235
confirm_y = 720

rally_count = 15
wait_rally_time = 79  # in seconds


# run the cmd as administrator to allow pydirectinput to work properly

print("1. Open the game and align the game screen to topLeft of your main screen.")
print("2. Run the cmd as administrator to allow script to work properly.")
print("3. Adjust the coordinates, wait times and rally count as necessary for your specific task.")
print("4. Click on Pangolin or Groundhog to show rally option before running the script.")
print("5. Set your ProUnit formation and the rally time manually before running the script.")
print("6. To get the x and y coordinates use pyautogui.position() API in python cmd.")
print("7. To stop the script press ctrl + C.")
time.sleep(1)

# Initial delay to allow user to switch to the game window
print("You have 5 seconds to switch to the game window...")
time.sleep(5)

# Get the current mouse position for rally button
rally_x, rally_y = pyautogui.position()

# Click on the Pangolin or Groundhog to select it before running the script
while rally_count > 0:
    pyautogui.moveTo(rally_x, rally_y, duration=1)
    time.sleep(0.5)
    pydirectinput.click()

    pyautogui.moveTo(confirm_x, confirm_y, duration=1)
    time.sleep(0.5)
    pydirectinput.click()

    pyautogui.moveTo(march_x, march_y, duration=1)
    time.sleep(0.5)
    pydirectinput.click()

    rally_count -= 1
    print(f"Rally count: {rally_count}")

    # Wait for 2 minutes before the next rally
    time.sleep(wait_rally_time)

print("Rallying completed.")
# Note: Adjust the coordinates and wait times as necessary for your specific game and setup.
