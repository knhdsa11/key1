import keyboard
import threading
import time
import pyautogui


"""
List of keys to block (except h, q reserved for hotkeys).
"""
lock_keys = [k for k in list("qwertyuiopasdfghjklzxcvbnm")]


"""
Mouse movement speed (default).
"""
speedn = 5
speeda = 1

def set_loop(z):
    global speeda
    speeda = z
    print(f"[loop] = {z}")
        
"""
Mouse control mode (toggle). Default: OFF.
"""
mouse_mode = False


def toggle_mode():
    """
    Toggle the mouse control mode.

    When ON:
        - Blocks predefined keyboard keys.
        - Allows using custom keys (h, j, k, l, c, r, w, s)\
              to control the mouse.

    When OFF:
        - Unblocks all previously blocked keys.
    """
    global mouse_mode
    mouse_mode = not mouse_mode
    if mouse_mode:
        print("[ON] Mouse control mode ON (keys blocked)")
        for key in lock_keys:
            keyboard.block_key(key)
    else:
        print("[OFF] Mouse control mode OFF (keys unblocked)")
        for key in lock_keys:
            keyboard.unblock_key(key)


def mouse_control_loop():
    """
    Continuously check for key presses and control the mouse accordingly.

    Controls:
        h = move left
        l = move right
        j = move down
        k = move up
        c = left click
        r = right click
        w = scroll up
        s = scroll down

    This function runs in a background thread.
    """
    global mouse_mode
    while True:
        if mouse_mode:
            
            if keyboard.is_pressed("h"):
                for _ in range(speeda):
                    pyautogui.moveRel(-speedn, 0)

            if keyboard.is_pressed("l"):
                for _ in range(speeda):
                    pyautogui.moveRel(speedn, 0)

            if keyboard.is_pressed("j"):
                for _ in range(speeda):
                    pyautogui.moveRel(0, speedn)

            if keyboard.is_pressed("k"):
                for _ in range(speeda):
                    pyautogui.moveRel(0, -speedn)



            if keyboard.is_pressed("c"):
                pyautogui.click()
            if keyboard.is_pressed("r"):
                pyautogui.rightClick()
            if keyboard.is_pressed("w"):
                pyautogui.scroll(100)
            if keyboard.is_pressed("s"):
                pyautogui.scroll(-100)
        time.sleep(0.01)


def exit_program():
    """
    Exit the program safely.
    """
    print("[Bye] Program terminated")
    exit()


def main():
    """
    Setup hotkeys, start mouse control thread, and wait for hotkey events.
    """
    # Toggle mouse control mode
    keyboard.add_hotkey("ctrl+alt+.", toggle_mode)

    # Exit program
    keyboard.add_hotkey("ctrl+alt+q", exit_program)

    # Hotkeys to adjust mouse speed
    keyboard.add_hotkey("0", lambda: set_loop(10))
    keyboard.add_hotkey("1", lambda: set_loop(1))
    keyboard.add_hotkey("2", lambda: set_loop(2))
    keyboard.add_hotkey("3", lambda: set_loop(3))
    keyboard.add_hotkey("4", lambda: set_loop(4))
    keyboard.add_hotkey("5", lambda: set_loop(5))
    keyboard.add_hotkey("6", lambda: set_loop(6))
    keyboard.add_hotkey("7", lambda: set_loop(7))
    keyboard.add_hotkey("8", lambda: set_loop(8))
    keyboard.add_hotkey("9", lambda: set_loop(9))

    # Run background thread
    threading.Thread(target=mouse_control_loop, daemon=True).start()

    # Wait for hotkeys
    keyboard.wait()


if __name__ == "__main__":
    main()
