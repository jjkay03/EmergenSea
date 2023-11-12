# EmergenSea codded by jjkay03 - Started on 11/12/2023

import keyboard
import webbrowser
import pygetwindow as gw


# -- Variables ------------------------------------------------------

hotkey_1 = 'ctrl+1'
url_to_open = "https://www.youtube.com/jjkay03"
minimize = True  # Set to True if you want to minimize instead of closing


# -- Functions -------------------------------------------------------

def test_hotkey():
    print("Hotkey is working!")

def emergensea():
    # Get the currently focused window
    current_window = gw.getActiveWindow()

    if minimize:
        # Minimize the currently focused window
        current_window.minimize()
        print(f"[FUNC:emergency] Minimizing window: {current_window.title}")
    else:
        # Close the currently focused window
        current_window.close()
        print(f"[FUNC:emergency] Closing window: {current_window.title}")

    # Open the specified URL
    webbrowser.open_new_tab(url_to_open)
    print(f"[FUNC:emergency] Opening new tab in browser")


# -- Main -----------------------------------------------------------

print("EmergenSea is running!")

# Hotkeys - listen for the hotkeys and call the right function for them
keyboard.add_hotkey(hotkey_1, emergensea)
keyboard.wait()
