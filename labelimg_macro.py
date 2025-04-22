#!/usr/bin/env python3
import time
import threading
import tkinter as tk
from tkinter import messagebox
import pyautogui
import pygetwindow as gw

# Global kontrol flag’i
stop_flag = False

def focus_labelimg():
    """LabelImg penceresini bulup aktif eder."""
    windows = [w for w in gw.getAllTitles() if "labelImg" in w]
    if not windows:
        return False
    win = gw.getWindowsWithTitle(windows[0])[0]
    win.activate()
    time.sleep(0.5)
    return True

def countdown_and_alert():
    """3 saniyelik geri sayım ve uyarı penceresi gösterir."""
    global stop_flag
    # Başlatıldıktan sonra Stop basılırsa iptal edilecek
    stop_flag = False
    root.withdraw()

    for i in range(3, 0, -1):
        if stop_flag:
            cleanup("Durduruldu.")
            return
        label.config(text=f"Başlıyor in {i}...")
        root.update()
        time.sleep(1)

    if stop_flag:
        cleanup("Durduruldu.")
        return

    # LabelImg’e odaklan
    if not focus_labelimg():
        messagebox.showerror("Hata", "LabelImg penceresi bulunamadı!")
        cleanup()
        return

    if stop_flag:
        cleanup("Durduruldu.")
        return

    # Uyarı mesajı
    messagebox.showinfo("Uyarı", "Lütfen LabelImg dosyasını döndürün.")
    cleanup()

    # Burada otomasyon kodunu çağırabilirsin:
    # if not stop_flag:
    #     import labelimg_macro
    #     labelimg_macro.run_macro()

def cleanup(final_msg=None):
    """Arayüzü kapat ve gerekirse mesaj göster."""
    if final_msg:
        # Ana pencereyi geri getirip mesaj göster
        root.deiconify()
        messagebox.showinfo("Bilgi", final_msg)
    root.destroy()

def on_start():
    """Başlat butonuna basılınca çalışan fonksiyon."""
    threading.Thread(target=countdown_and_alert, daemon=True).start()

def on_stop():
    """Durdur butonuna basılınca çalışan fonksiyon."""
    global stop_flag
    stop_flag = True

if __name__ == "__main__":
    root = tk.Tk()
    root.title("LabelImg Macro Başlatıcı")
    root.geometry("300x140")
    root.resizable(False, False)

    label = tk.Label(root, text="Başlamak için Başlat'a bas", font=("Arial", 14))
    label.pack(pady=(20, 10))

    btn_frame = tk.Frame(root)
    btn_frame.pack()

    start_btn = tk.Button(btn_frame, text="Başlat", width=10, command=on_start)
    start_btn.grid(row=0, column=0, padx=5)

    stop_btn = tk.Button(btn_frame, text="Durdur", width=10, command=on_stop)
    stop_btn.grid(row=0, column=1, padx=5)

    root.mainloop()


if not focus_labelimg():
        exit(1)

    count = int(input("Kaç kere tekrarlansın? "))
    for i in range(1, count+1):
        # (no need to re‑focus on every iteration unless you lose focus)
        pyautogui.press('a')
        pyautogui.hotkey('ctrl', 'e')
        pyautogui.press('s')
        pyautogui.press('o')
        pyautogui.press('down', presses=2, interval=0.05)
        pyautogui.press('enter', presses=2, interval=0.05)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.press('d')
        time.sleep(0.2)
