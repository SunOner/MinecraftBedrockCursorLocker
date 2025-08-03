# MinecraftBedrockCursorLocker

This repository contains a Python script to lock the mouse cursor within the Minecraft Bedrock Edition window on Windows. It prevents the cursor from escaping during gameplay, which is a common issue with UWP apps like Bedrock.

## Features
- Automatically detects the Minecraft window.
- Locks the cursor by monitoring and resetting its position if it escapes.
- Hotkeys: Alt+1 to pause/resume the lock, Alt+2 to stop the script.
- Ctrl+C for emergency stop.

## Requirements
- Windows 10/11.
- Python 3.12+ (will be installed automatically if missing).
- pywin32 library (will be installed automatically).

## Installation
1. Go to the repository page on GitHub: https://github.com/sunoner/MinecraftBedrockCursorLocker.
2. Click the green "Code" button and select "Download ZIP".
3. Extract the ZIP file to a folder on your computer (e.g., using right-click > Extract All).
4. Open the extracted folder.

No manual installation needed—the `start.bat` script handles everything, including Python and dependencies.

## Usage
1. Launch Minecraft Bedrock and enter a world.
2. Double-click `start.bat` (run as administrator if needed).
   - It will check and install Python/pywin32 if missing.
   - Then, it automatically runs `script.py` to start locking the cursor.
3. Use the hotkeys as needed.
4. To stop, press Alt+2 or Ctrl+C in the console window.

## Notes
- Run the script after opening Minecraft.
- If the window title differs (e.g., due to language), adjust the "Minecraft" string in `script.py`.