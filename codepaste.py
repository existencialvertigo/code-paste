import pyautogui
import pyperclip
import time

# List of codes
codes = [] #EDITAR CONFORME README

# List of coordinates (same for all)
coordinates = [(606, 534)] * len(codes) #EDITAR CONFORME README, localização do Campo de colar o código

# Function to simulate the click and paste process
def click_and_paste(codes, coordinates):
    for code, (x, y) in zip(codes, coordinates):
        # Move the mouse to the given coordinates and click
        pyautogui.click(x, y)

        # Copy the code to the clipboard
        pyperclip.copy(code)

        # Simulate pressing CTRL+V to paste the code
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0)
        pyautogui.click(642,689) # EDITAR CONFORME README, localização do Receber Códigos
        # Wait a moment before the next action
        time.sleep(0)

# Call the function to start the process
click_and_paste(codes, coordinates)
