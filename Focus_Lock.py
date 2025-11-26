import tkinter as tk
from tkinter import ttk
import threading
import time
import sys

# Attempt to import required libraries
# If user doesn't have them, show a message
try:
    import pyautogui
    import keyboard
except ImportError:
    print("Error: Please install 'pyautogui' and 'keyboard' libraries.")
    print("Command: pip install pyautogui keyboard")
    sys.exit()


# Project: Focus Lock (Study Timer)
# Author: Mozahid
# Purpose: To block distractions during study time.

class HardLock:
    def __init__(self, duration_sec):
        self.duration = duration_sec
        self.remaining = duration_sec

        print(f"DEBUG: Lock started for {duration_sec} seconds.")

        # Setting up the main window
        self.root = tk.Tk()
        self.root.title("Focus Mode Active")

        # Making it fullscreen so no one can click outside
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="black")
        self.root.attributes("-topmost", True)  # Keep window on top

        # Disable the close button (X)
        self.root.protocol("WM_DELETE_WINDOW", self.block_event)

        # Label to show timer
        self.label = tk.Label(self.root, text="Starting...", fg="white", bg="black", font=("Arial", 30))
        self.label.pack(expand=True)

        # Using threads to run blocking logic in background
        # Otherwise the GUI will freeze
        t1 = threading.Thread(target=self.block_keys)
        t1.daemon = True  # This thread dies when main program exits
        t1.start()

        t2 = threading.Thread(target=self.mouse_control)
        t2.daemon = True
        t2.start()

        self.update_timer()
        self.root.mainloop()

    def block_event(self, event=None):
        # This function prevents closing the window
        return "break"

    def update_timer(self):
        # Determine minutes and seconds
        if self.remaining > 0:
            mins, secs = divmod(self.remaining, 60)
            self.label.config(text=f"🔒 FOCUS MODE ON\nTime Remaining: {mins:02d}:{secs:02d}")
            self.remaining -= 1
            # Call this function again after 1000ms (1 second)
            self.root.after(1000, self.update_timer)
        else:
            print("Timer finished. Unlocking screen.")
            self.root.destroy()

    def block_keys(self):
        # List of keys to block to prevent switching windows
        # Note: I used AI help to understand how to block keys safely
        block_list = ['alt', 'tab', 'ctrl', 'esc', 'windows']

        while self.remaining > 0:
            for key in block_list:
                try:
                    keyboard.block_key(key)
                except Exception as e:
                    # Sometimes permission error occurs if not Admin
                    pass
            time.sleep(0.1)  # Small delay to reduce CPU usage

    def mouse_control(self):
        # Logic to keep mouse in the center
        screen_width, screen_height = pyautogui.size()
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        while self.remaining > 0:
            pyautogui.moveTo(center_x, center_y)
            time.sleep(0.1)


# Main GUI for selecting time
def time_selector_gui():
    def start_lock():
        selection = time_var.get()

        # Mapping selection to seconds
        duration_map = {
            "5 Minutes": 5 * 60,
            "15 Minutes": 15 * 60,
            "30 Minutes": 30 * 60,
            "1 Hour": 60 * 60,
            "2 Hours": 2 * 60 * 60,
            "3 Hours": 3 * 60 * 60
        }

        # Default to 5 minutes if something goes wrong
        selected_duration = duration_map.get(selection, 300)

        selector.destroy()  # Close the selector window
        HardLock(selected_duration)  # Start the lock

    selector = tk.Tk()
    selector.title("Focus Timer Setup")
    selector.geometry("350x250")
    selector.configure(bg="#2C3E50")  # Dark blue-grey background

    label = tk.Label(selector, text="Select Focus Duration:", fg="white", bg="#2C3E50", font=("Arial", 14))
    label.pack(pady=20)

    time_var = tk.StringVar()
    combo = ttk.Combobox(selector, textvariable=time_var, font=("Arial", 12), state="readonly")
    combo["values"] = [
        "5 Minutes", "15 Minutes", "30 Minutes",
        "1 Hour", "2 Hours", "3 Hours"
    ]
    combo.current(0)
    combo.pack(pady=10)

    btn = tk.Button(selector, text="Start Locking", command=start_lock, font=("Arial", 12), bg="#27AE60", fg="white")
    btn.pack(pady=20)

    selector.mainloop()


if __name__ == "__main__":
    time_selector_gui()