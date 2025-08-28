# © 2025 Kaustav Ray. All rights reserved.
# Licensed under the MIT License.

"""
Telegram String Session Generator for Termux
--------------------------------------------
This script generates a string session for a Telegram account using Telethon.
It will prompt the user for their API ID, API Hash, and phone number.

Author: Kaustav Ray
"""

from telethon import TelegramClient
from telethon.sessions import StringSession

def main():
    """
    Main function to initialize the Telegram client and generate a string session.
    """
    print("\n=== Telegram String Session Generator ===\n")

    try:
        api_id = int(input("Enter your API ID: ").strip())
        api_hash = input("Enter your API Hash: ").strip()
        phone = input("Enter your phone number (with country code): ").strip()

        with TelegramClient(StringSession(), api_id, api_hash) as client:
            client.start(phone=phone)
            print("\n✅ Successfully logged in!")
            print("\nYour String Session:\n")
            print(client.session.save())
            print("\n⚠️ Save this string safely. Do NOT share it with anyone.\n")

    except ValueError:
        print("❌ Invalid API ID. Please enter a numeric value.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
