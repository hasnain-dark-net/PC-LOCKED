@echo off

REM Install required packages first
python -m pip install pyautogui keyboard pillow opencv-python

REM Run script in background (CMD hidden)
start "" /B pythonw lock.py

exit
