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

def set_speed_fast():
    global speedn
    speedn = 50
    print("⚡ Speed = 50")

def set_speed_normal():
    global speedn
    speedn = 10
    print("🐢 Speed = 10")


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
                pyautogui.moveRel(0, -speedn)
            if keyboard.is_pressed("k"):
                pyautogui.moveRel(0, speedn)
            if keyboard.is_pressed("c"):
                pyautogui.click()
            if keyboard.is_pressed("r"):
                pyautogui.rightClick()
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
keyboard.add_hotkey("ctrl+1", set_speed_fast)
keyboard.add_hotkey("ctrl+2", set_speed_normal)
keyboard.add_hotkey("ctrl+alt+.", toggle_mode)   # toggle โหมด
keyboard.add_hotkey("ctrl+alt+q", exit_program)  # ออกโปรแกรม

# ==========================
# Run
# ==========================
threading.Thread(target=mouse_control_loop, daemon=True).start()
keyboard.wait()  # รอ hotkeys
