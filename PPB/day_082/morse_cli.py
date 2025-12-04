#!/usr/bin/env python3
import argparse

GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

MORSE_CODE_MAP = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",

    ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--",

    " ": "/"  # common convention for space between words
}

MORSE_REVERSE_MAP = {morse: char for char, morse in MORSE_CODE_MAP.items()}


def colorize_morse(symbol: str) -> str:
    """Apply colors to Morse symbols."""
    colored = ""
    for ch in symbol:
        if ch == ".":
            colored += f"{GREEN}.{RESET}"
        elif ch == "-":
            colored += f"{YELLOW}-{RESET}"
        elif ch == "/":
            colored += f"{BLUE}/{RESET}"
        else:
            colored += ch
    return colored


def colorize_text(text: str) -> str:
    """Colorize decoded plaintext."""
    return "".join(f"{RED}{c}{RESET}" for c in text)


def encode_to_morse(text: str) -> str:
    encoded = " ".join(MORSE_CODE_MAP.get(ch.upper(), "?") for ch in text)
    return " ".join(colorize_morse(token) for token in encoded.split())


def decode_from_morse(morse: str) -> str:
    decoded = "".join(MORSE_REVERSE_MAP.get(code, "?") for code in morse.split())
    return colorize_text(decoded)


def main():
    parser = argparse.ArgumentParser(description="Morse code encoder/decoder CLI tool.")
    parser.add_argument("mode", choices=["encode", "decode"], help="Choose encode or decode mode.")
    parser.add_argument("message", help="Message to encode or decode.")

    args = parser.parse_args()

    if args.mode == "encode":
        print(encode_to_morse(args.message))
    elif args.mode == "decode":
        print(decode_from_morse(args.message))


if __name__ == "__main__":
    main()
