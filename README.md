# Neon Space Dash - Pygame Zero Setup Guide

## 1. Project Overview

This project is a simple Python game built with:

* Python 3.12
* Pygame
* Pygame Zero
* Local image/audio assets

The game should be run with:

```bash
python demoGame.py
```

Do not rely on the global `pgzrun` command, because it may not be available in `PATH` on every machine.

---

## 2. Required Project Structure

Make sure the project folder has the following structure:

```text
Be_tap_lam_game/
│
├─ demoGame.py
├─ requirements.txt
│
├─ images/
│  ├─ player.png
│  ├─ crystal.png
│  ├─ meteor.png
│  └─ background.png
│
├─ sounds/
│  ├─ collect.wav
│  ├─ hit.wav
│  └─ gameover.wav
│
└─ music/
   └─ bgm.wav
```

Important notes:

* Image files used by `Actor("player")`, `Actor("crystal")`, and `Actor("meteor")` must be inside the `images/` folder.
* The background image must be named `background.png`.
* Sound effects must be inside the `sounds/` folder.
* Background music must be inside the `music/` folder.
* File names are case-sensitive on Linux environments such as GitHub Codespaces.

---

## 3. Required Code Format

Because this game is run using:

```bash
python demoGame.py
```

the file must import `pgzrun` at the top and call `pgzrun.go()` at the bottom.

At the top of `demoGame.py`:

```python
import random
import pygame
import pgzrun
```

At the bottom of `demoGame.py`:

```python
pgzrun.go()
```

Do not place `import pgzrun` only at the bottom.
If `Actor("player")` is created before `pgzrun` is imported, Python may raise this error:

```text
NameError: name 'Actor' is not defined
```

---

## 4. requirements.txt

Create a file named `requirements.txt`:

```txt
pygame
pgzero
```

---

# Local Setup - Windows PowerShell

## 1. Open project folder

```powershell
cd "D:\Private\_Lam viec\Teach\Lap_Trinh_Game\Be_tap_lam_game"
```

## 2. Remove old virtual environment

If a virtual environment is currently active, run:

```powershell
deactivate
```

Then delete the old `.venv` folder:

```powershell
Remove-Item -Recurse -Force .venv
```

If `deactivate` shows an error, ignore it. It only means the virtual environment was not active.

---

## 3. Create new virtual environment with Python 3.12

```powershell
py -3.12 -m venv .venv
```

---

## 4. Activate virtual environment

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```powershell
(.venv) PS ...
```

---

## 5. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 6. Run the game

```powershell
python demoGame.py
```

---

# GitHub Codespaces Setup

## 1. Open repository in GitHub Codespaces

Open the repository on GitHub, then choose:

```text
Code → Codespaces → Create codespace
```

---

## 2. Install dependencies

Inside the Codespaces terminal, run:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 3. Run the game

```bash
python demoGame.py
```

---

## 4. Important Codespaces GUI Note

This project is a Pygame Zero GUI game.

In a normal local environment, the game window opens directly.

In GitHub Codespaces, the terminal runs in a remote Linux container, so a graphical game window may not appear automatically. To visually play the game inside Codespaces, the codespace needs a virtual display setup such as:

* Xvfb
* VNC
* noVNC
* or a Dev Container desktop/VNC feature

Without a virtual display, the code may run but the game window may not be visible.

---

# Optional Dev Container Setup for Codespaces

Create this folder:

```text
.devcontainer/
```

Inside it, create:

```text
devcontainer.json
```

Example `.devcontainer/devcontainer.json`:

```json
{
  "name": "Pygame Zero Codespace",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "features": {},
  "postCreateCommand": "python -m pip install --upgrade pip && python -m pip install -r requirements.txt",
  "forwardPorts": [6080],
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python"
      ]
    }
  }
}
```

This installs Python 3.12 and project dependencies automatically when the codespace is created.

For full GUI support, the dev container may need an additional desktop/VNC/noVNC configuration.

---

# Common Errors and Fixes

## Error 1: `pgzrun` is not recognized

Example:

```text
pgzrun : The term 'pgzrun' is not recognized
```

Cause:

The `pgzrun.exe` script is not available in the system `PATH`.

Fix:

Use this command instead:

```bash
python demoGame.py
```

Make sure `demoGame.py` has:

```python
import pgzrun
```

at the top and:

```python
pgzrun.go()
```

at the bottom.

---

## Error 2: `ModuleNotFoundError: No module named 'pgzero'`

Cause:

The current Python environment does not have `pgzero` installed.

Fix:

```bash
python -m pip install pgzero pygame
```

Then run:

```bash
python demoGame.py
```

---

## Error 3: Wrong Python version is being used

Example:

```text
Python314\python.exe: ModuleNotFoundError: No module named 'pgzero'
```

Cause:

Dependencies were installed in Python 3.12, but the command is running Python 3.14.

Fix on Windows:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python demoGame.py
```

---

## Error 4: `NameError: name 'Actor' is not defined`

Cause:

The file is being run with normal Python, but `pgzrun` was not imported before using Pygame Zero objects.

Fix:

At the top of `demoGame.py`, add:

```python
import pgzrun
```

At the bottom of `demoGame.py`, add:

```python
pgzrun.go()
```

Then run:

```bash
python demoGame.py
```

---

## Error 5: Missing image asset

Example:

```text
KeyError: "No image found like 'player'"
```

Cause:

Pygame Zero cannot find the required image.

Fix:

Check that this file exists:

```text
images/player.png
```

Also check the other required images:

```text
images/crystal.png
images/meteor.png
images/background.png
```

File names must match exactly.

---

## Error 6: Missing sound or music file

If sound effects or background music do not play, check:

```text
sounds/collect.wav
sounds/hit.wav
sounds/gameover.wav
music/bgm.wav
```

The game uses:

```python
pygame.mixer.music.load("music/bgm.wav")
```

So the `music/bgm.wav` path must be correct.

---

# Recommended Run Commands

## Windows

```powershell
cd "D:\Private\_Lam viec\Teach\Lap_Trinh_Game\Be_tap_lam_game"
.\.venv\Scripts\Activate.ps1
python demoGame.py
```

## GitHub Codespaces / Linux

```bash
python -m pip install -r requirements.txt
python demoGame.py
```

---

# Final Notes for Developers

* Use Python 3.12 for best compatibility.
* Do not depend on the global `pgzrun` command.
* Run the game using `python demoGame.py`.
* Keep all assets in the correct folders.
* On GitHub Codespaces, configure a virtual display if you need to visually play the GUI game.


INFO FOR IMAGES:
* background.png : 960 x 540 px 
* crystal.png : 52 x 52 px 
* meteor.png : 88 x 64 px 
* player.png : 72 x 72 px


UPDATE SIZE FOR IMAGE:
<!-- player -->
player._orig_surf = pygame.transform.scale(player._orig_surf, (72, 72))
player._surf = pygame.transform.scale(player._surf, (72, 72))
player._update_pos()
