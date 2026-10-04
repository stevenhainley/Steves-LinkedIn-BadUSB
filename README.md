# Steves-LinkedIn-BadUSB

Contains payloads and all the necessary files for a Raspberry Pi Pico W to use keystroke injection to open a LinkedIn profile or instantly download and display a hosted resume PDF. 

This is an excellent physical networking tool for career fairs, cybersecurity conferences, or quickly sharing a profile with recruiters. It includes payloads for macOS (LinkedIn or Resume PDF) and Windows (LinkedIn).

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
In this repository, you will find three payload files: `payload(mac)`, `payload(windows)`, and `payload(resume-mac)`. The (...) at the end of the filenames are an intentional safety measure to prevent the code from executing automatically before you have configured it. Please choose a file you wish to use as a payload, and rename that one to payload.

1. Copy `code.py` and your chosen payload file(s) to the root of your `CIRCUITPY` drive.
2. **For LinkedIn Payloads (`mac` or `windows`):** Open the file in a text editor, find the URL in the script, and replace it with your own LinkedIn profile link.
3. **For the Resume Payload (`resume-mac`):** 
    * Upload your resume PDF directly to this GitHub repository.
    * Click on your PDF file in GitHub, then click the **Download raw file** button (the tray icon with a downward arrow) to open the raw file in your browser.
    * Copy that specific URL from the address bar (it should start with `raw.githubusercontent.com`).
    * Open `payload(resume-mac).` in a text editor and replace `YOUR_RAW_GITHUB_LINK_HERE` with your copied URL.
4. **CRITICAL STEP:** Rename your chosen payload file to exactly `payload` (delete the OS name and the period at the end). The `code.py` script specifically looks for a file named exactly `payload` to run.
5. You can delete the unused payload files from the `CIRCUITPY` drive. 

*Note: Once the file is renamed to `payload`, the Pico W will immediately act as a keyboard upon receiving power. To edit the files safely in the future without triggering the payload, you will need to interrupt the script or enter safe mode.*

## ⚠️ Disclaimer
This project is for educational and personal networking purposes only. Only plug this device into machines you own or have explicit permission to use.
