import keyboard

def on_zero_press(event):
    print("Number '0' was pressed. Exiting...")
    keyboard.unhook_all()  # Unhook all listeners
    exit(0)

keyboard.on_press_key("0", on_zero_press)

# Keep the program running.
keyboard.wait('esc')