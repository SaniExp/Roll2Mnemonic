Table Of Contents
=================
1. [Roll2Mnemonic](#roll2mnemonic)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Online Usage](#online-usage)
6. [Offline Usage](#offline-usage)
7. [Demo Video](#demo-video)
8. [Support and Feedback](#support-and-feedback)
9. [Donations](#donations)
10. [Disclaimer](#disclaimer)
11. [License](#license)

# Roll2Mnemonic

Roll2Mnemonic is an educational tool for studying BIP39 mnemonic generation, Bitcoin derivation paths, addresses, and BIP85 child mnemonics. It can generate corresponding private keys and public addresses for supported Bitcoin script types.

The application opens with an embedded terminal on the left and controls on the right. It starts maximized, requires an explicit security acknowledgement, and currently exposes 12-word and 24-word choices in the UI. Other supported word-count controls remain in the code for future use.

## Features

- **Dice Roll:**
    1. Physical Dice or Coin Toss: You have the flexibility to roll physical dice or conduct a coin toss and input the resulting data as either binary (1 or 0) or numbers (1 to 6). This method ensures absolute randomness for generating your mnemonic seed phrase.
    2. Generate From Entropy: The application uses Python's OS-backed `secrets` CSPRNG for this educational mode. This mode is not recommended for real funds; use your own physical dice or coin flips for highest assurance.
    3. Mnemonic Seed Generation: After collecting the dice roll data, the program seamlessly proceeds to generate a valid checksum and creates a BIP39 mnemonic seed phrase. This seed phrase forms the cornerstone for generating Bitcoin private keys and public addresses.
    4. Mnemonic Code Converter: The generated mnemonic seed phrase is then processed through the Mnemonic Code Converter, capable of generating BIP39 private keys and public addresses for all script types: Legacy (P2PKH), Nested SegWit (P2SH-P2WPKH), Native SegWit (P2WPKH), and Taproot (P2TR).
- **Mnemonic Converter:**
    1. Generate From Entropy: The application can generate entropy with the OS-backed CSPRNG for educational testing. This mode is explicitly not recommended for real funds.
    2. Mnemonic Seed Generation: After collecting the Hex seed, the program seamlessly proceeds to generate a valid checksum and creates a BIP39 mnemonic seed phrase.
    3. Own Mnemonic Seed Phrase: You have the option to enter your own mnemonic seed phrase into the program.
    4. Mnemonic Code Converter: The generated mnemonic seed phrase is then processed through the Mnemonic Code Converter, capable of generating BIP39 private keys and public addresses for all script types: Legacy (P2PKH), Nested SegWit (P2SH-P2WPKH), Native SegWit (P2WPKH), and Taproot (P2TR).
- **BIP85 Generator:** Generate BIP85 Child Keys from your own Mnemonic Seed Phrase or using seeds generated with the tools above, then specify the numbers of words and number of Child Keys using the index number.
- **QR Code Generator:** A built-in QR code generator from text.

## Security warning

This project is educational and has not been independently audited. Do not use it to generate or handle real Bitcoin funds without independently reviewing and verifying the complete code, dependencies, operating system, and device.

A seed phrase and passphrase control the wallet. If they are exposed, an attacker can spend the funds, and Bitcoin transactions are generally irreversible. A valid BIP39 checksum does not prove that the original entropy was secure; weak, predictable, reused, or manipulated entropy can produce a phrase an attacker can reproduce.

For the highest assurance, use a trusted offline device and create entropy by rolling your own fair dice or performing your own fair coin flips. Never enter a seed or passphrase into a website, online verifier, screenshot, cloud service, or untrusted computer. Before funding a wallet, independently verify its addresses and test restoration from an offline backup.


## Prerequisites

Before using the Mnemonic Code Converter, ensure you have the following prerequisites installed on your system:

- Python 3.11 or newer (the current development environment uses Python 3.13)
- Tkinter (included with the standard Windows Python installer)
- Python packages listed in `requirements.txt`


## Installation

You can clone this repository to your local machine using the following method:

### HTTPS

To clone the repository using HTTPS, open your terminal or command prompt and run the following command:

```bash
git clone https://github.com/SaniExp/Roll2Mnemonic.git
```

### Direct Download 

Download and extract the following file:

```bash
https://github.com/SaniExp/Roll2Mnemonic/archive/refs/heads/main.zip
```


## Usage

Follow these steps to use the Roll2Mnemonic:

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3.11 or above installed.
3. Install the necessary Python libraries listed in requirements.txt
4. Launch main.py to initiate the code.


## Offline Usage

To set up Python in an offline environment you must download the packages by using an internet-enabled computer, and then transfer the files to the offline computer.
Ensure target machine is the same architecture, OS, and Python version as the original device.

1. Download latest version of python from:

```bash
https://www.python.org/downloads/
```

2. Download latest version of pip, if you don't have it on ur current computer or offline computer and follow instructions from:

```bash
https://pip.pypa.io/en/stable/installation/
```

3. Clone or download the repository (Make sure you have the latest release), and extract it.

4. Cloning dependencies, same method for all operating systems:

   a. In a terminal, navigate to the Roll2Mnemonic directory:

     ```bash
     cd C:\Roll2Mnemonic
     ```

   b. Create a subdirectory named wheelhouse:

     ```bash
     mkdir wheelhouse
     ```

   c. Run the following command to download the required dependencies to the subdirectory:

     ```bash
     pip download -r requirements.txt -d wheelhouse
     ```

   d. Copy the Python and pip packages you downloaded earlier and the folder Roll2Mnemonic, which contains the repository and the sub-folder Wheelhouse, into a USB stick and transfer them to your offline computer.

   e. Install the Python and pip packages then, in a terminal, navigate to the Roll2Mnemonic folder:

     ```bash
     cd C:\Roll2Mnemonic
     ```

   f. Run the following to install the dependencies:

     ```bash
     pip install -r requirements.txt --no-index --find-links wheelhouse
     ```

   g. If you encounter installation errors you can try this alternative method to install the dependencies. Otherwise, you need to retrieve the failed dependencies manually:

     - Windows (Command Prompt):

       ```bash
       for %i in ("C:\path\to\folder with spaces\*") do pip install "%i"
       ```

     - Linux/Mac (Command Prompt):

       ```bash
       for package in "/path/to/folder with spaces"/*; do
           pip install "$package"
       done
       ```

Now your offline device should have the required dependencies to run offline. Do not use the online clone/download machine to enter or generate wallet secrets.

## Support and Feedback

If you have any questions, encounter issues, or want to provide feedback, please open an issue in this repository or provide feedback through twitter @SaniExp.

## Donations

If you find this project useful and would like to support its development, you can make a donation to help keep it going. Your contributions are greatly appreciated!

- Bitcoin lightning address (Wallet Of Satoshi): sani@walletofsatoshi.com
- Bitcoin lightning address (Blink): sani@blink.sv

## Disclaimer

The application displays a security disclaimer and requires the user to type `I UNDERSTAND` before use. This acknowledgement is not a security guarantee. If the device, operating system, dependencies, display, terminal output, logs, or application is compromised, assume every displayed seed, passphrase, private key, and extended private key is compromised and abandon the wallet.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
