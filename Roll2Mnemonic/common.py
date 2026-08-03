from mnemonic import Mnemonic
from mnemonic import Mnemonic as bip39
import os
import locale
from bip32utils import BIP32Key
import hashlib
import binascii
import base58
from bitcoinutils.setup import setup
from bitcoinutils.keys import PrivateKey, PublicKey
from art import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont
import qrcode
from PIL import Image, ImageTk
from pycoin.symbols.btc import network as BTC
import hmac
from pycoin.encoding.bytes32 import to_bytes_32

terminal_widget = None

def set_terminal_widget(widget):
    global terminal_widget
    terminal_widget = widget

# Use grouped number formatting where the platform provides the requested
# locale, while keeping startup portable across Windows, Linux, and macOS.
try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '')

def disclaimer():
    # Clear terminal
    clear_terminal()

    # Print a centered disclaimer notice
    text1 = "* DISCLAIMER *"
    print_centered_art_text(text1, 6, "Standard")

    # Print disclaimer details
    print_red(f"""

    \n THIS IS AN EDUCATIONAL TOOL — DO NOT TRUST IT WITH REAL FUNDS WITHOUT INDEPENDENT VERIFICATION.
    \n A Bitcoin seed phrase and passphrase control the funds. If either is exposed, an attacker can take the funds.
    \n Bitcoin transactions are generally irreversible. A compromised seed can result in permanent, unrecoverable loss.
    \n A valid BIP39 checksum does NOT prove that the entropy was secure. Weak, predictable, reused, or manipulated entropy can allow an attacker to reproduce the seed.
    \n For the highest assurance, use a trusted offline device and create entropy by rolling your own fair dice or performing your own fair coin flips.
    \n Never use automatically generated entropy for real funds unless you have independently reviewed and trust the complete implementation and environment.
    \n Never enter a seed phrase or passphrase into a website, online verifier, screenshot, cloud service, or untrusted computer.
    \n Before funding any wallet, independently verify the seed, passphrase, derivation path, addresses, and an offline backup restoration.
    \n If this device, display, terminal, logs, or application is compromised, assume every displayed secret is compromised and abandon the wallet.
    """)

def foot_note():
    print(f"\n To confirm binary to decimal conversion, visit: https://www.rapidtables.com/convert/number/binary-to-decimal.html")
    print(" To cross-check decimal to index/word conversion, visit: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt")
    print(" To confirm your mnemonic seed phrase, visit: https://iancoleman.io/bip39/")
    print(" Note that binary numbers start from 0, while the BIP39 wordlist starts from 1, so remember to add 1 to the decimal result to match the word.")

def main():
    # Clear terminal
    clear_terminal()
    
    # Print title
    text2 = "* ROLL   TO   MNEMONIC *"
    print_centered_art_text(text2, 5, "Standard")

    # Information box
    creator_info = f"Created By          : SaniExp"
    twitter_info = f"Twitter             : @SaniExp"
    github_info = f"GitHub              : https://github.com/SaniExp"
    lightning_info = f"Lightning Donations : sani@walletofsatoshi.com"
    max_info_length = max(len(creator_info), len(twitter_info), len(github_info), len(lightning_info))
    box_width = max_info_length + 4
    info_box = " " + "+" + "-" * (box_width - 2) + "+"
    info_box += f"\n | {creator_info.ljust(max_info_length)} |"
    info_box += f"\n | {twitter_info.ljust(max_info_length)} |"
    info_box += f"\n | {github_info.ljust(max_info_length)} |"
    info_box += f"\n | {lightning_info.ljust(max_info_length)} |"
    info_box += "\n +" + "-" * (box_width - 2) + "+"
    print_bright_orange(info_box)

# Functions to print text in color
def print_red(*args):
    text = ' '.join(map(str, args))
    print("\033[91m" + text + "\033[0m")  # '\033[91m' is the ANSI escape code for red color

def print_blue(*args):
    text = ' '.join(map(str, args))
    print("\033[94m" + text + "\033[0m")  # '\033[94m' is the ANSI escape code for blue color

def print_green(*args):
    text = ' '.join(map(str, args))
    print("\033[92m" + text + "\033[0m")  # '\033[92m' is the ANSI escape code for green color

def print_cyan(*args):
    text = ' '.join(map(str, args))
    print("\033[96m" + text + "\033[0m")  # '\033[93m' is the ANSI escape code for orange color

def print_purple(*args):
    text = ' '.join(map(str, args))
    print("\033[95m" + text + "\033[0m")  # '\033[95m' is the ANSI escape code for purple color

def print_bright_orange(*args):
    text = ' '.join(map(str, args))
    print("\033[38;5;208m" + text + "\033[0m")  # '\033[38;5;208m' is the ANSI escape code for bright orange color

# Clear terminal
def clear_terminal():
    if terminal_widget is not None and terminal_widget.winfo_exists():
        terminal_widget.config(state=tk.NORMAL)
        terminal_widget.delete("1.0", tk.END)
        terminal_widget.config(state=tk.DISABLED)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
    
# Display a centered art text
def print_centered_art_text(text, convert, fonttype):
    if terminal_widget is not None and terminal_widget.winfo_exists():
        output_font = tkfont.Font(font=terminal_widget.cget("font"))
        character_width = max(1, output_font.measure("0"))
        terminal_width = max(1, (terminal_widget.winfo_width() - 20) // character_width)
    else:
        terminal_width = 166

    rendered_art = text2art(text, font=fonttype).rstrip("\n")
    for line in rendered_art.splitlines():
        padding = " " * max(0, (terminal_width - len(line)) // 2)
        print(padding + line)

# Function to check if a seed phrase is valid
def is_valid_seed(seed_phrase):
    try:
        mnemo = Mnemonic("english")
        return mnemo.check(seed_phrase)
    except ValueError:
        return False
