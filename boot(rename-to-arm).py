import supervisor
import usb_hid
import storage
import usb_cdc

# Overrides the USB Device Descriptor parameters (Spoofing a Logitech Keyboard)
# Passwords/strings must be plain text, VID/PID are hex numbers

supervisor.set_usb_identification(
    manufacturer="Logitech, Inc.",
    product="Logitech USB Keyboard",
    vid=0x046D,  # Logitech Vendor ID
    pid=0xC31C   # Logitech Keyboard Product ID
)

# Disables Drive pop ups when renamed boot.py

storage.disable_usb_drive()  # Hides the CIRCUITPY drive
usb_cdc.disable()            # Hides the serial COM port

# Enables only the HID device (Keyboard) and sets it as the boot device
usb_hid.enable((usb_hid.Device.KEYBOARD,), boot_device=1)
