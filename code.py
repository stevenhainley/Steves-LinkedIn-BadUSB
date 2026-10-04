import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

ducky_keys = {
    'GUI': Keycode.GUI,
    'WINDOWS': Keycode.GUI,
    'ENTER': Keycode.ENTER,
    'SPACE': Keycode.SPACE,
    'TAB': Keycode.TAB,
    'SHIFT': Keycode.SHIFT,
    'ALT': Keycode.ALT,
    'CONTROL': Keycode.CONTROL,
    'CTRL': Keycode.CONTROL,
    'DELETE': Keycode.DELETE,
    'ESC': Keycode.ESCAPE,
    'UPARROW': Keycode.UP_ARROW,
    'DOWNARROW': Keycode.DOWN_ARROW,
    'LEFTARROW': Keycode.LEFT_ARROW,
    'RIGHTARROW': Keycode.RIGHT_ARROW
}

try:
    with open("payload.dd", "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("REM"):
                continue
            
            parts = line.split(" ", 1)
            command = parts[0]
            args = parts[1] if len(parts) > 1 else ""

            if command == "STRING":
                layout.write(args)
            elif command == "DELAY":
                time.sleep(int(args) / 1000)
            else:
                keys_to_press = []
                for key in line.split():
                    if key in ducky_keys:
                        keys_to_press.append(ducky_keys[key])
                    elif hasattr(Keycode, key):
                        keys_to_press.append(getattr(Keycode, key))
                
                if keys_to_press:
                    kbd.press(*keys_to_press)
                    kbd.release_all()
except OSError:
    pass