import pyautogui
import pyperclip
import time

# List of codes
codes = []

# List of coordinates (same for all)
coordinates = [(606, 534)] * len(codes)

# Function to simulate the click and paste process
def click_and_paste(codes, coordinates):
    for code, (x, y) in zip(codes, coordinates):
        # Move the mouse to the given coordinates and click
        pyautogui.click(x, y)

        # Copy the code to the clipboard
        pyperclip.copy(code)

        # Simulate pressing CTRL+V to paste the code
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.click(642,689)
        # Wait a moment before the next action
        time.sleep(1)

# Call the function to start the process
click_and_paste(codes, coordinates)