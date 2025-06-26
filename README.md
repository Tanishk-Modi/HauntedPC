# corrupted.py

⚠️ **WARNING:**

Running this program will invite a malevolent entity into your machine. Proceed with caution. 

Users have reported numerous unusual phenomena, including;

- **Erratic Cursor Movement** 
- **Possessed Typing** 
- **Visual Distortions** 
- **Unsettling Audio Playback**
- **Phantom Error Prompts**

---

# Preparation Ritual: 

Before the haunting can begin, certain preparations must be made.

## 1. Clone the Repository

```bash
git clone <repository_url_here>
cd HauntedPC
```
## 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# For Windows PowerShell/CMD:
.\venv\Scripts\activate
# For Git Bash/WSL:
source venv/bin/activate
```

## 3. Install Dependencies

```
pip install pyautogui pygame pycaw comtypes
```
## 4. Configure Windows Colors Filters (For visual glitch)

- Go to Windows Settings > Accessibility > Color filters.
- Ensure the main "Color filters" toggle is OFF.
- Under "Choose a color filter," select "Inverted". This enables the ```Win + Ctrl + C``` shortcut, which the program uses.

## Usage

To summon the entity:

- Open an Integrated Terminal in VS Code with your virtual environment activated.
- Ensure your current directory is the root of the HauntedPC project.
- Execute the main script:
```
python main.py
```

---

## Technical Overview

**Language:** Python 3  
**Operating System:** Windows 11  

**Core Libraries:**

- `pyautogui` — simulating mouse and keyboard inputs.
- `pygame` — audio playback via its `mixer` module.
- `pycaw` — direct control over Windows audio volume.
- `subprocess` — launching applications.
- `tkinter.messagebox` — displaying custom dialog pop-ups.

