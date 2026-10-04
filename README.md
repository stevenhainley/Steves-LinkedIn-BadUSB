# Steves-LinkedIn-BadUSB
Contains a payload and all the necessary files for a Raspberry-Pi Pico W to use keystroke injection to open up any LinkedIn URL, or any URL! PLEASE READ THE README FOR INSTRUCTIONS

# Steves-LinkedIn-BadUSB

A BadUSB payload built for the **Raspberry Pi Pico W**. This script acts as a virtual keyboard to rapidly open a LinkedIn profile on a target computer, bypassing the need for someone to manually type your URL. 

This is an excellent physical networking tool for career fairs, cybersecurity conferences, or quickly sharing a resume profile with recruiters. It includes payloads for both macOS and Windows.

## 🛠 Prerequisites
* **Hardware:** Raspberry Pi Pico W
* **Cable:** A Micro-USB cable capable of data transfer (not just power/charging)
* **Target OS:** macOS or Windows

## ⚙️ Setup & Flashing Guide

Follow these steps to flash your Raspberry Pi Pico W and configure your custom payload.

### 1. Install CircuitPython
1. Hold down the **BOOTSEL** button on your Raspberry Pi Pico W.
2. While holding the button, plug the Pico W into your computer's USB port. 
3. Release the button. A new removable drive called `RPI-RP2` will appear on your computer.
4. Download the latest version of [CircuitPython for the Pico W (UF2 file)](https://circuitpython.org/board/raspberry_pi_pico_w/).
5. Drag and drop the downloaded `.uf2` file onto the `RPI-RP2` drive. 
6. The drive will automatically disconnect and reconnect as a new drive named `CIRCUITPY`.

### 2. Install the Required Libraries
Because the Pico W needs to emulate a keyboard, you need the Adafruit HID library.
1. Download the [Adafruit CircuitPython Library Bundle](https://circuitpython.org/libraries).
2. Extract the downloaded zip file.
3. Open the `lib` folder inside the extracted bundle.
4. Copy the `adafruit_hid` folder.
5. Paste it into the `lib` folder on your `CIRCUITPY` drive.

### 3. Load and Configure Your Payload
In this repository, you will find two payload files: `payload(mac).` and `payload(windows).`. The periods at the end of the filenames are an intentional safety measure to prevent the code from executing automatically before you have configured it.

1. Copy `code.py` and the two payload files to the root of your `CIRCUITPY` drive.
2. Decide whether you want to target macOS or Windows machines, and open the corresponding payload file in a text editor.
3. Find the URL in the script and replace it with your own LinkedIn profile link. Save the file.
4. **CRITICAL STEP:** Rename your chosen payload file to exactly `payload` (delete the OS name and the period at the end). The `code.py` script specifically looks for a file named exactly `payload` to run.
5. You can delete the unused payload file from the `CIRCUITPY` drive. 

*Note: Once the file is renamed to `payload`, the Pico W will immediately act as a keyboard upon receiving power. To edit the files safely in the future without triggering the payload, you will need to interrupt the script or enter safe mode.*

## ⚠️ Disclaimer
This project is for educational and personal networking purposes only. Only plug this device into machines you own or have explicit permission to use.
