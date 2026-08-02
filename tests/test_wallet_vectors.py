import contextlib
import io
import unittest
import warnings

# bip32utils still calls two deprecated compatibility functions in ecdsa 0.19.
# This narrowly suppresses that known third-party warning without hiding other
# deprecations or runtime errors from the application and tests.
warnings.filterwarnings(
    "ignore",
    message=r"Function is unused in library code\..*",
    category=DeprecationWarning,
)

from mnemonic import Mnemonic

from Roll2Mnemonic.diceroll_auto import dr_auto, roll_dice
from Roll2Mnemonic.mccmainnet import generate_mainnet_addresses
from Roll2Mnemonic.bip85 import derive_child_key


class EntropyTests(unittest.TestCase):
    def test_secure_dice_range(self):
        rolls = roll_dice(6, 1000)
        self.assertEqual(len(rolls), 1000)
        self.assertTrue(all(1 <= roll <= 6 for roll in rolls))

    def test_automatic_mnemonic_is_valid(self):
        # dr_auto prints an educational trace; keep the test output clean.
        with contextlib.redirect_stdout(io.StringIO()):
            words = dr_auto(12)
        self.assertEqual(len(words), 12)
        self.assertTrue(Mnemonic("english").check(" ".join(words)))


class BitcoinVectorTests(unittest.TestCase):
    mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"

    def test_bip84_and_bip86_addresses(self):
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message=r"Function is unused in library code\..*",
                category=DeprecationWarning,
            )
            addresses, _ = generate_mainnet_addresses(self.mnemonic, 1, "")
        self.assertEqual(
            addresses["Native SegWit (P2WPKH)R"][0][4],
            "bc1qcr8te4kr609gcawutmrza0j4xv80jy8z306fyu",
        )
        self.assertEqual(
            addresses["Taproot (P2TR)R"][0][4],
            "bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr",
        )

    def test_bip85_12_word_vector(self):
        # Official BIP85 test vector master xprv, m/83696968'/39'/0'/12'/0'.
        master_xprv = (
            "xprv9s21ZrQH143K2LBWUUQRFXhucrQqBpKdRRxNVq2zBqsx8HVqFk2uYo8kmbaLLHRdqtQpUm98uKfu3vca1LqdGhUtyoFnCNkfmXRyPXLjbKb"
        )
        self.assertEqual(
            derive_child_key(master_xprv, 12, 0),
            "girl mad pet galaxy egg matter matrix prison refuse sense ordinary nose",
        )


if __name__ == "__main__":
    unittest.main()
