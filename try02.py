from pynput.keyboard import Key, Listener

def on_press(key):
    # Check if the key has a char attribute
    if hasattr(key, 'char'):
        # Check if the pressed key is '0'
        if key.char == '0':
            # Stop listener
            return False

# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()
    # break
