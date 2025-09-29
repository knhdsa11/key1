import keyboard
import threading
import time
import pyautogui

# ==========================
# รายการปุ่มที่ต้องการบล็อก (เว้น h, q สำหรับ hotkey)
# ==========================
lock_keys = [k for k in list("qwertyuiopasdfghjklzxcvbnm")]

# ==========================
# ความเร็วเคลื่อนเมาส์
# ==========================
speedn = 10

def set_speed(z):
    global speedn
    speedn = z
    print(f"⚡ Speed = {z}")

# ==========================
# โหมดควบคุมเมาส์ (toggle)
# ==========================
mouse_mode = False  # ค่าเริ่มต้น ปิดโหมด

def toggle_mode():
    global mouse_mode
    mouse_mode = not mouse_mode
    if mouse_mode:
        print("✅ Mouse control mode ON (keys blocked)")
        for key in lock_keys:
            keyboard.block_key(key)
    else:
        print("❌ Mouse control mode OFF (keys unblocked)")
        for key in lock_keys:
            keyboard.unblock_key(key)


def mouse_control_loop():
    global mouse_mode
    while True:
        if mouse_mode:
            if keyboard.is_pressed("h"):
                pyautogui.moveRel(-speedn, 0)
            if keyboard.is_pressed("l"):
                pyautogui.moveRel(speedn, 0)
            if keyboard.is_pressed("j"):
                pyautogui.moveRel(0, speedn)
            if keyboard.is_pressed("k"):
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


# ==========================
# ปุ่มออกจากโปรแกรม
# ==========================
def exit_program():
    print("Bye 👋")
    exit()


# ==========================
# Hotkeys
# ==========================
keyboard.add_hotkey("ctrl+9", set_speed, args="10" )
keyboard.add_hotkey("ctrl+8", set_speed, args="20"  )
keyboard.add_hotkey("ctrl+7", set_speed, args="30"  )
keyboard.add_hotkey("ctrl+6", set_speed, args="40"  )
keyboard.add_hotkey("ctrl+5", set_speed, args="50"  )
keyboard.add_hotkey("ctrl+4", set_speed, args="60"  )
keyboard.add_hotkey("ctrl+3", set_speed, args="70"  )
keyboard.add_hotkey("ctrl+2", set_speed, args="80"  )
keyboard.add_hotkey("ctrl+1", set_speed, args="90"  )
keyboard.add_hotkey("ctrl+0", set_speed, args="5" )
keyboard.add_hotkey("ctrl+alt+.", toggle_mode)   # toggle โหมด
keyboard.add_hotkey("ctrl+alt+q", exit_program)  # ออกโปรแกรม

# ==========================
# Run
# ==========================
threading.Thread(target=mouse_control_loop, daemon=True).start()
keyboard.wait()  # รอ hotkeys
