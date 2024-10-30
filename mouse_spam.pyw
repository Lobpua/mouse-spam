import os
import sys
import time
import threading
import psutil
from pynput.mouse import Button, Controller as MouseController
from pynput import mouse
from tkinter import Tk, Label
from send2trash import send2trash

# Set this to the path of your desktop to check if the script is active
lock_file = "path_to_your_desktop\\program_lock.lock"

def move_to_recycle_bin(file_path):
    try:
        send2trash(file_path)
        print("Lock file successfully moved to recycle bin.")
    except Exception as e:
        print(f"Error moving file to recycle bin: {e}")

def kill_previous_process():
    if os.path.exists(lock_file):
        with open(lock_file, 'r') as f:
            pid = int(f.read())
        try:
            p = psutil.Process(pid)
            p.terminate()
            p.wait()
            print(f"Process with PID {pid} terminated.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Error terminating process: {e}")

if os.path.exists(lock_file):
    kill_previous_process()

    root = Tk()
    root.title("OFF")
    label = Label(root, text="OFF", font=("Arial", 30))
    label.pack(padx=20, pady=20)
    
    root.after(500, root.destroy)
    root.mainloop()

    move_to_recycle_bin(lock_file)
    os._exit(0)

with open(lock_file, "w") as f:
    f.write(str(os.getpid()))

root = Tk()
root.title("ON")
label = Label(root, text="ON", font=("Arial", 30))
label.pack(padx=20, pady=20)

def close_on():
    root.destroy()

root.after(500, close_on)
root.mainloop()

mouse_controller = MouseController()
clicking = False

def click_mouse():
    while clicking:
        mouse_controller.click(Button.left)
        time.sleep(0.06)

def on_click(x, y, button, pressed):
    global clicking
    if button == Button.x1: # ← Here is the current button specified (Mouse4 or X1 button)
        if pressed:
            clicking = True
            thread = threading.Thread(target=click_mouse)
            thread.start()
        else:
            clicking = False

def start_listener():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

listener_thread = threading.Thread(target=start_listener)
listener_thread.start()

try:
    listener_thread.join()
finally:
    if os.path.exists(lock_file):
        os.remove(lock_file)
