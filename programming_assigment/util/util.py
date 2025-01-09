import time
import threading


class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    DARK_ORANGE = "\033[38;2;170;85;0m"
    RESET = "\033[0m"


def print_colored(text, color=Color.BLUE):
    print(f"{color}{text}{Color.RESET}", end="")


def println_colored(text, color=Color.BLUE):
    print(f"{color}{text}{Color.RESET}")


def display_loading_animation(message, color):
    loading_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    counter = 0

    def loading():
        nonlocal counter
        try:
            while not stop_event.is_set():
                print_colored(f"\r{loading_chars[counter % len(loading_chars)]} {message}", color)
                counter += 1
                time.sleep(0.1)  # Adjust the delay as needed
        except KeyboardInterrupt:
            pass

    stop_event = threading.Event()
    loading_thread = threading.Thread(target=loading)
    loading_thread.start()

    # Run the loading animation for a few seconds
    time.sleep(1)  # Adjust the duration as needed
    stop_event.set()
    loading_thread.join()

    # Clear the loading line
    print("\r" + " " * len(message) + "\r")
