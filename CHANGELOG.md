# Change report

## 2026-10-06 — Windows résumé payload

### Behavior

Replaced the Windows LinkedIn-only payload with a résumé downloader. It opens Command Prompt first, waits for it to load, downloads `Steven_Hainley_Resume.pdf` from this repository, and launches the downloaded file explicitly in Microsoft Edge. The PDF is opened only after curl succeeds. The terminal closes after the launch command succeeds.

### Supporting fixes

- Changed the Windows shortcut to `GUI R` and made the interpreter accept key names in either case, without changing `STRING` contents.
- Used `supervisor.runtime.autoreload = False`, the supported CircuitPython API, and added a startup check to prevent file-save reloads from typing a payload.
- Corrected setup instructions to use the exact filename `payload.dd`.
- Added instructions for another person's hosted résumé, Windows requirements, timing adjustments, and the distinction between ejecting the drive and physically disconnecting the keyboard.

### Validation and limits

Checked Python syntax, interpreted the Windows payload with mocked HID devices, and checked the hosted résumé response. No end-to-end Windows hardware test was performed for this repository update. Edge must be installed with its PDF viewer enabled; this does not guarantee compatibility with every Windows or managed browser configuration.

### Revert

The update is recorded in a Git commit. Revert that commit to restore the previous Windows LinkedIn payload, interpreter, and README. Reverting also restores the earlier filename documentation and lowercase-key limitation.
