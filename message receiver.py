# © 2025 Kaustav Ray. All rights reserved.
# Licensed under the MIT License.
#
# Description:
#   Extended script: captures ALL messages (incoming + outgoing).
#   Useful for monitoring everything your account sees or sends.
#
# Note:
#   - Never share your string session.
#   - Only use this for your own account.

from telethon import TelegramClient, events
import asyncio
import os

# -------------------------------
# Configuration
# -------------------------------
API_ID = int(os.getenv("TG_API_ID", "123456"))         
API_HASH = os.getenv("TG_API_HASH", "your_api_hash")   
STRING_SESSION = os.getenv("TG_STRING_SESSION", "your_string_session_here")

# -------------------------------
# Initialize Telegram Client
# -------------------------------
client = TelegramClient(
    session=STRING_SESSION,
    api_id=API_ID,
    api_hash=API_HASH
)

# -------------------------------
# Event Listener for ALL Messages
# -------------------------------
@client.on(events.NewMessage(incoming=True, outgoing=True))  # include outgoing too
async def message_handler(event):
    """
    Handle all new messages (incoming + outgoing).
    Prints sender info and message text.
    """
    try:
        sender = await event.get_sender()
        sender_name = getattr(sender, "first_name", "Unknown")
        direction = "⬅️ Incoming" if event.is_private and event.is_incoming else "➡️ Outgoing"
        print(f"\n{direction} message from {sender_name} (@{sender.username}):\n{event.raw_text}\n")
    except Exception as e:
        print(f"[ERROR] Failed to process message: {e}")

# -------------------------------
# Main Entrypoint
# -------------------------------
async def main():
    print("🚀 Telegram client started. Listening for ALL messages...\n")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        with client:
            client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n🛑 Script stopped by user.")
    except Exception as e:
        print(f"[FATAL ERROR] {e}")
