# FocusLock - Student Study Timer 🔒

Hi, I am **Mozahid**, a student from Bangladesh. This is a Python project I created to help myself and other students focus on their studies by locking the computer screen for a specific duration.

## 📖 Project Description
Distractions are a big problem while studying. This tool creates a "python Focus_Lock.py" on your computer. Once the timer starts, you cannot minimize the window, switch tabs, or use the mouse until the time is over.

It forces the user to leave the computer alone and focus on books or offline study.

## 🛠 Features
- **Fullscreen Lock:** Covers the entire screen with a black background.
- **Key Blocking:** Blocks `Alt+Tab`, `Windows Key`, and `Esc` so you cannot exit easily.
- **Mouse Trap:** Keeps the mouse cursor stuck in the center of the screen.
- **Timer:** Shows a countdown timer on the screen.

## 💻 Libraries Used
I used Python with the following libraries:
- `tkinter` (Built-in) - For the User Interface.
- `threading` (Built-in) - To run the timer and blocking logic at the same time.
- `pyautogui` - To control the mouse cursor.
- `keyboard` - To block system keys.

## 🚀 How to Run
1. Install the required libraries:
   ```bash
   pip install pyautogui keyboard
 ## 🤖 Acknowledgement & AI Usage
I am a beginner in Python and currently learning Computer Science concepts. 
...
- I used **AI assistance to help me understand how to use `threading` (so the app doesn't freeze) and how to use the `keyboard` library to block system keys safely.
- The AI helped me debug the code when the loop was crashing.
