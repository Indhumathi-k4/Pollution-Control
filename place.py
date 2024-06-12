import subprocess
import pyautogui
import pygetwindow as gw
import time
import mss
from mss import tools
import os

def open_google_earth():
    """Launches Google Earth Pro."""
    try:
        # Replace this with the actual path of your Google Earth Pro executable
        google_earth_path = r"C:\Program Files\Google\Google Earth Pro\client\googleearth.exe"
        subprocess.Popen(google_earth_path)
        time.sleep(5)  # Wait for Google Earth Pro to launch
    except Exception as e:
        print(f"Error launching Google Earth Pro: {e}")

def focus_on_google_earth():
    """Attempts to find and focus the Google Earth window."""
    windows = gw.getWindowsWithTitle('Google Earth Pro')
    if windows:
        window = windows[0]
        if not window.isActive:
            window.activate()
            time.sleep(2)  # Give some time for the window to come into focus
        if window.isMinimized:
            window.restore()
        time.sleep(2)  # Wait a bit after restoring
        return True
    else:
        print("Google Earth window not found.")
        return False
    

def close_unexpected_popups(image_path=r"C:\Users\prave\OneDrive\Desktop\final_year_project\popup_close.png"):
    """Attempts to close unexpected popups by clicking a known image."""
    try:
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        if button_location:
            pyautogui.click(button_location)
            print("Popup closed.")
            time.sleep(3)  # Wait a bit after closing the popup
    except Exception as e:
        print(f"Error closing popup: {e}")
              
def search_and_capture(place):
    open_google_earth()  # Launch Google Earth Pro
    time.sleep(3)  # Wait a bit for the application to fully load and for any popups to appear.
    close_unexpected_popups()  # Close any popups that might have appeared upon launching.
    if not focus_on_google_earth():
        return

    pyautogui.click(x=20, y=100)  # Adjust based on your Google Earth app
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write(place)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)  # Wait for search results, adjust timing as needed
    close_unexpected_popups()  # Optionally, close any popups that might appear after the search.

    # Zoom in by simulating mouse wheel scrolling
    pyautogui.moveTo(1150,550 )  # Adjust location
    for _ in range(7):
        pyautogui.scroll(2)
        time.sleep(1)
        
    time.sleep(3)
    
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)

        filename = os.path.join("C:\\Users\\prave\\OneDrive\\Desktop\\final_year_project", "Input_Image.png")
        tools.to_png(screenshot.rgb, screenshot.size, output=filename)

        print(f'Screenshot saved as {filename}')

    close_google_earth()

def close_google_earth():
    windows = gw.getWindowsWithTitle('Google Earth Pro')
    if windows:
        window = windows[0]
        window.close()
        print("Google Earth Pro has been closed.")
