# labelimg-gui-automator
A Python‑based automation toolkit featuring a clean, Tkinter‑powered GUI that streamlines your LabelImg workflow. It automatically detects and brings the LabelImg window into focus, provides a configurable three‑second visual countdown before execution, and includes a dedicated emergency “Stop” button 


Here’s a professional, GitHub‑ready `README.md` for your Python + PyAutoGUI LabelImg automation script. You can copy this into your repo’s root as `README.md`.

```markdown
# LabelImg Automation Macro

![PyPI](https://img.shields.io/pypi/v/pyautogui) ![License](https://img.shields.io/github/license/yourusername/labelimg-macro)

A lightweight Python script to automate repetitive LabelImg annotation tasks using [PyAutoGUI](https://pyautogui.readthedocs.io/). Simply specify how many times the key‑sequence should repeat, and let the script do the rest.

---

## 🚀 Features

- **Cross‑platform**: Works on Linux and Windows (with Python3 & PyAutoGUI).
- **Configurable loops**: Prompt for the number of repetitions.
- **Minimal dependencies**: Only requires `pyautogui` (and its standard dependencies).
- **Easy to extend**: Customize key‑sequences or add window‑activation logic.

---

## 📦 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/labelimg-macro.git
   cd labelimg-macro
   ```

2. **Create & activate a virtual environment (optional but recommended)**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install pyautogui
   sudo apt-get install scrot xclip   # Linux only: for screenshot & clipboard support
   ```

---

## ⚙️ Usage

1. **Open LabelImg** and bring its window into focus.
2. **Run the script**:  
   ```bash
   python labelimg_macro.py
   ```
3. **Enter repetition count** when prompted:  
   ```
   Kaç kere tekrarlansın? 5
   ```
4. **Sit back** as the script executes your annotation steps 5 times.

---

## 🛠️ Customization

- **Adjust delays**  
  Modify `time.sleep(...)` values for longer/shorter pauses between actions.
- **Activate window programmatically**  
  Uncomment and adapt the `pyautogui.getWindowsWithTitle("labelImg")` block to auto‑focus the LabelImg window.
- **Change key‑sequence**  
  Edit the sequence of `pyautogui.press()` and `pyautogui.hotkey()` calls to suit your workflow.

---

## 📂 Project Structure

```
.
├── labelimg_macro.py    # Main automation script
├── LICENSE              # MIT License
└── README.md            # This file
```

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## ✉️ Contact

Created by **Your Name** – feel free to open an issue or submit a PR!

- GitHub: [@yourusername](https://github.com/yourusername)  
- Email: your.email@example.com  
```

**Next Steps:**

1. Rename placeholders (`yourusername`, **Your Name**, email) to your own.
2. Commit to GitHub:
   ```bash
   git add README.md
   git commit -m "Add professional README"
   git push origin main
   ```
3. Enjoy a polished project landing page!
