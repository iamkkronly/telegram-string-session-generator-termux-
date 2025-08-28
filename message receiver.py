# © 2025 Kaustav Ray. All rights reserved.
# Licensed under the MIT License.
#
# Description:
#   Script to capture the first 20 incoming messages from Telegram system (ID 777000), then stop automatically.
#
# Note:
#   - Never share your string session.
#   - Only use this for your own account.

from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

# -------------------------------
# Hardcoded Credentials
# -------------------------------
API_ID = 123456  # replace with your API_ID (integer)
API_HASH = "your_api_hash_here"  # replace with your API_HASH
STRING_SESSION = "your_string_session_here"  # replace with your STRING_SESSION

# -------------------------------
# Initialize Telegram Client
# -------------------------------
client = TelegramClient(
    session=StringSession(STRING_SESSION),
    api_id=API_ID,
    api_hash=API_HASH
)

# -------------------------------
# Globals
# -------------------------------
message_count = 0
MAX_MESSAGES = 20
TARGET_ID = 777000  # Telegram system account

# -------------------------------
# Event Listener: Capture messages only from ID 777000
# -------------------------------
@client.on(events.NewMessage(incoming=True, from_users=TARGET_ID))
async def message_handler(event):
    """
    Capture and print incoming messages from Telegram system (ID 777000) until MAX_MESSAGES is reached.
    """
    global message_count
    try:
        sender = await event.get_sender()
        sender_name = getattr(sender, "first_name", "TelegramSystem")
        print(f"\n📩 Message #{message_count+1} from {sender_name}:\n{event.raw_text}\n")

        message_count += 1
        if message_count >= MAX_MESSAGES:
            print("\n✅ Reached 20 messages. Stopping client...\n")
            await client.disconnect()
    except Exception as e:
        print(f"[ERROR] Failed to process message: {e}")

# -------------------------------
# Main Entrypoint
# -------------------------------
async def main():
    print(f"🚀 Telegram client started. Capturing first {MAX_MESSAGES} messages from ID {TARGET_ID}...\n")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        with client:
            client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n🛑 Script stopped by user.")
    except Exception as e:
        print(f"[FATAL ERROR] {e}")
