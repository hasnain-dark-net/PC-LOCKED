@echo off
title Lock Script Starter

echo Checking & installing required modules...
python -m pip install --quiet pyautogui keyboard pillow opencv-python

echo Starting script...
start "" /B pythonw lock.py
exit
