# Steve's LinkedIn & Resume USB

I built this Raspberry Pi Pico W project to share my LinkedIn profile or résumé with a short keyboard sequence. The Pico acts as a USB keyboard and runs a selected payload when it starts up.

The Windows payloads either download my résumé and open it in Microsoft Edge, or open my LinkedIn profile in the computer's default browser. The macOS payloads open either LinkedIn or a downloaded résumé.

## What you need

- A Raspberry Pi Pico W and a data-capable Micro-USB cable.
- CircuitPython 8 or newer, with an Adafruit HID library bundle matching your CircuitPython major version.
- A US keyboard layout on the receiving computer; the script uses `KeyboardLayoutUS`.
- An unlocked computer with permission to use it and an internet connection.
- For the Windows résumé payload: Windows 10 or 11 with `curl.exe` and Microsoft Edge installed, and Edge's built-in PDF viewer enabled. No Adobe app or Adobe sign-in is needed for this workflow. Custom browser policies can prevent inline PDF viewing, so this is not guaranteed on every Windows configuration.

## Set up the Pico

1. Hold **BOOTSEL** while connecting the Pico. Release it when the `RPI-RP2` drive appears.
2. Download the [CircuitPython UF2 for Raspberry Pi Pico W](https://circuitpython.org/board/raspberry_pi_pico_w/) and copy it to `RPI-RP2`. The board restarts and mounts as `CIRCUITPY`.
3. Download the matching [Adafruit CircuitPython Library Bundle](https://circuitpython.org/libraries). Copy its `lib/adafruit_hid` folder into `CIRCUITPY/lib/`.
4. Copy this repository's `code.py` to the root of `CIRCUITPY`.
5. Choose a payload, customize it, and copy it to that drive as **`payload.dd`**. Keep the `.dd` extension; the script looks for that exact filename. Enable file extensions in your file manager if necessary.
6. Eject the drive and physically unplug the Pico. Connect it to the intended computer to run the payload.

| Repository file | Behavior |
| --- | --- |
| `payload(linkedin-windows).dd` | Opens my LinkedIn profile in the default browser |
| `payload(windows).dd` | Downloads the résumé to `%TEMP%\Steven_Hainley_Resume.pdf` and opens it in Edge |
| `payload(resume-mac).dd` | Downloads the résumé to `/tmp/resume.pdf` and opens the default PDF viewer |
| `payload(mac).dd` | Opens LinkedIn in the default browser |

Only the selected file should be named `payload.dd`. Leave the other payloads with their descriptive names.

## Open LinkedIn on Windows

Use `payload(linkedin-windows).dd` to open [my LinkedIn profile](https://www.linkedin.com/in/steven-hainley-836262268/) in the computer's default browser. You can customize it to share your own profile.

1. Open that file in a text editor.
2. Replace `https://www.linkedin.com/in/steven-hainley-836262268/` on the `STRING` line with your own full LinkedIn profile URL, including `https://`. Keep it on one line.
3. Copy the customized file to `CIRCUITPY` as **`payload.dd`**, replacing the previously selected payload if needed.
4. Physically unplug the Pico and reconnect it to the intended Windows computer.

For example:

```text
STRING https://www.linkedin.com/in/YOUR_PROFILE/
```

This payload waits five seconds, opens **Win + R**, waits one second, types the URL, and presses Enter. Windows opens the configured default browser; the payload does not choose Edge or launch Command Prompt. It requires a configured default browser and an available Run dialog. Adjust `DELAY 1000` if Run needs longer to appear. LinkedIn sign-in requirements still apply. You can also substitute another HTTP or HTTPS web link if needed.

## Use your own résumé

1. Upload a PDF to your own GitHub repository, or another host providing a public, direct HTTPS download link. Remember that anyone with access to the public link can read the PDF.
2. On GitHub, open the PDF and copy its raw download URL. A typical URL looks like:

   ```text
   https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPOSITORY/main/Your_Resume.pdf
   ```

3. In `payload(windows).dd`, replace the quoted `https://raw.githubusercontent.com/stevenhainley/...` URL on the `STRING curl.exe` line with your own URL. Keep the surrounding quotes. Use a direct PDF link rather than the GitHub `blob` preview page. Keep the repository's actual branch name and URL-encode spaces in filenames as `%20`.
4. Optionally change `Steven_Hainley_Resume.pdf` to your preferred local filename. Change **both** occurrences: the curl output path and the Edge opening path.
5. Copy your customized file to the Pico as `payload.dd`.

The Windows command has this structure:

```bat
curl.exe -fL -o "%TEMP%\Your_Resume.pdf" "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPOSITORY/main/Your_Resume.pdf" && start "" msedge.exe --new-window "%TEMP%\Your_Resume.pdf" && exit
```

`curl.exe` downloads the file, follows redirects, and reports HTTP errors. `&&` opens the PDF only if the download succeeds. Edge is launched explicitly instead of using the system's default PDF application. Command Prompt closes after the launch command succeeds.

For macOS, replace the résumé URL in `payload(resume-mac).dd`; its `/tmp/resume.pdf` destination can stay as it is. For LinkedIn, replace the profile URL in `payload(mac).dd`.

## Timing and editing

The Windows résumé payload waits five seconds after startup, opens Command Prompt, then waits four seconds before typing the download command. Increase the relevant `DELAY` if a slower computer needs more time.

`code.py` disables automatic reloads and skips payload execution on a file-save reload. Reconnecting or resetting the board runs the payload again. **Ejecting CIRCUITPY does not disconnect the USB keyboard or stop an already-running payload; physically unplug it to stop typing.** A startup can still begin typing while you are trying to edit, so interrupt the script through the CircuitPython serial console before editing an armed device, or connect in CircuitPython safe mode.

Key names are case-insensitive, so `GUI R` and `GUI r` both work. Text after `STRING` keeps its original case.

## Troubleshooting

- **Windows search opens instead of Run:** use this repository's updated `code.py`; the earlier parser ignored lowercase key names.
- **An empty terminal opens:** increase the delay after `STRING cmd` / `ENTER` before the curl command is typed.
- **Nothing happens:** check that the selected file is exactly `payload.dd`, the cable supports data, and the required HID library is installed. Inspect the serial console for Python errors.
- **The PDF does not open:** check the raw URL, connectivity, and Edge installation/settings. A failed download leaves Command Prompt open so its error is visible.
- **Commands appear in the wrong application:** unplug the Pico. Confirm the operating system, keyboard layout, and timing before reconnecting.

## A quick transparency note

Parts of this README were written with AI help to save time. This is a personal project, and I'd rather spend more of that time building and tinkering than writing documentation. The setup instructions and testing limits are included so you can see what the project does and what still needs checking.

## Changes and contributions

See [CHANGELOG.md](CHANGELOG.md) for payload updates and validation notes. To contribute, open a pull request describing your change, the OS and CircuitPython version you used, and what you tested. Hardware tests are especially useful; do not mark a payload as tested on Windows based only on reading its commands.

Only use the device on computers you own or have explicit permission to use.
