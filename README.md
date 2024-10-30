for Russian-speaking users [Документация на русском](README_RU.md)

# Auto-Clicker Script with Lock File Control

This Python script is an auto-clicker that prevents multiple instances from running simultaneously by creating a lock file on the desktop. When launched, the script checks for an existing lock file. If found, it terminates the previous instance of the script, moves the lock file to the recycle bin, and then creates a new lock file for the current instance. 

## Features

- **Lock File Control**: Prevents multiple instances by creating a lock file on your desktop.
- **Auto Clicker**: Auto-clicks using the left mouse button when the side button (Mouse4, or X1 button) is pressed.
- **Process Cleanup**: Moves the previous instance’s lock file to the recycle bin and terminates the previous process if running.
- **Visual Feedback**: Displays an "ON" or "OFF" window for a brief period to indicate the current state.

## Requirements

- **Python 3.x**: Make sure Python is installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Required libraries**: These can be installed via `pip`. (Instructions below)

## Installation

1. **Download the Script**:

   - Go to the GitHub repository where this script is hosted.
   - Click on the green "Code" button.
   - Choose "Download ZIP" and save the ZIP file to your computer.
   - Extract the ZIP file to a folder of your choice.

2. **Install Dependencies**:

   - Open the extracted folder.
   - Hold the `Shift` key and right-click inside the folder, then select "Open PowerShell window here" (or "Open Command Prompt here" depending on your system).
   - Type the following command to install the necessary Python libraries:

     ```bash
     pip install -r requirements.txt
     ```

   If you encounter any issues with `pip`, make sure Python and `pip` are correctly installed and added to your system's PATH.

## Setup

1. **Modify the Lock File Path**: Open the script file (usually a `.py` file) in a text editor (like Notepad). Replace `path_to_your_desktop` with the path to your actual desktop. This lock file ensures only one instance runs at a time.

    ```python
    lock_file = "path_to_your_desktop\\program_lock.lock"
    ```

2. **Change the Activation Button**: By default, the script is set to activate with the side mouse button `Mouse4` (also known as `X1 button`). If you want to change the button, open the script file and find this line in the `on_click` function:

    ```python
    if button == Button.x1:
    ```

    Replace `Button.x1` with any of the following options:
    
    - `Button.left` for the left mouse button
    - `Button.right` for the right mouse button
    - `Button.middle` for the middle mouse button
    - `Button.x1` for the `Mouse4` (X1 button)
    - `Button.x2` for the `Mouse5` (X2 button)

    Example of using the mouse4 as an activation button:

    ```python
    if button == Button.x1:
    ```

## Usage

1. **Run the Script**: 

    - Double-click the Python script file (usually with a `.py` extension) to start the auto-clicker.

2. **How to Use the Auto-Clicker**:
    - Press the side mouse button (Mouse4 or X1 button) to start auto-clicking.
    - Release the button to stop auto-clicking.

3. **Visual Indicators**:
    - The "ON" window will briefly display when the script starts.
    - The "OFF" window will display if the script finds an existing instance and terminates it.

## Important Notes

- **Lock File Control**: The lock file (`program_lock.lock`) is created and deleted automatically. If you manually delete it, ensure no other instance of the script is running.
- **Termination**: When a new instance starts, it terminates the previous instance to ensure only one is active.

## Example

If you set `lock_file` as `"C:\\Users\\YourUsername\\Desktop\\program_lock.lock"`, the script will use this path to control the instance locking.

## License

This project is licensed under the MIT License.
