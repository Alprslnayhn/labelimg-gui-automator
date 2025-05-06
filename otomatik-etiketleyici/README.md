

---

### 🗂️ Repository Name:

```
keyboard-triggered-python-action
```

### 📝 Description:

> Execute custom Python scripts with a specific keyboard key using `xbindkeys` on Linux. Automate GUI actions seamlessly with PyAutoGUI.

---

### 📄 README.md

````markdown
# Keyboard-Triggered Python Action 🎯

A simple Linux setup to execute a Python script upon pressing a specific keyboard key using `xbindkeys`. Useful for GUI automation, repetitive tasks, and workflow shortcuts.

---

## 💡 Overview

This repository demonstrates how to:

- Write a Python script that performs a series of GUI actions using [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/).
- Bind the execution of that script to a keyboard key (e.g., F12) using [`xbindkeys`](https://wiki.archlinux.org/title/Xbindkeys).
- Automate tasks like saving a file, writing text, and pasting clipboard content — all triggered by a single keystroke.

---

## 🧩 Example Script

```python
import pyautogui
import time

time.sleep(1)
pyautogui.hotkey('ctrl', 's')
time.sleep(0.3)
pyautogui.write('d')
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'v')
````

---

## ⚙️ Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/YOUR_USERNAME/keyboard-triggered-python-action.git
cd keyboard-triggered-python-action
```

### 2. Install Requirements

```bash
pip install pyautogui
sudo apt install xbindkeys
```

### 3. Create a Script File

You may use the included `otomatik_etiket.py` or create your own. Example:

```bash
nano ~/otomatik_etiket.py
```

Paste your Python code and save.

### 4. Configure xbindkeys

#### a. Generate default config if not present:

```bash
xbindkeys --defaults > ~/.xbindkeysrc
```

#### b. Edit the config:

```bash
nano ~/.xbindkeysrc
```

Append the following to bind the script to the **F12** key:

```bash
"python3 /home/YOUR_USERNAME/otomatik_etiket.py"
    m:0x10 + c:88
```

✅ Replace `/home/YOUR_USERNAME/otomatik_etiket.py` with the full path to your Python script.

### 5. Find Key Codes (Optional)

To bind a different key:

```bash
xbindkeys -k
```

Press the desired key to get its `m:` and `c:` values.

### 6. Launch xbindkeys

```bash
xbindkeys
```

Now, pressing the defined key (e.g., **F12**) will run the Python script.

---

## 🚀 Usage

Open any GUI application and press the defined hotkey to automate your defined actions (e.g., saving files, writing text, pasting clipboard contents).

---

## 📎 Notes

* Ensure the script has executable permissions: `chmod +x otomatik_etiket.py`
* `xbindkeys` must be restarted after editing the config.
* Use responsibly. PyAutoGUI controls your keyboard and mouse.

---

## 🧠 Author

Made with ❤️ by \[Your Name]

---

## 📄 License

This project is licensed under the MIT License.

```

---

If you provide your GitHub username or intended customizations (script name, key to bind, etc.), I can personalize the README further.
```

