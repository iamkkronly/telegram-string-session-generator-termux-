# telegram-string-session-generator-termux-

🔧 How to Run on Termux

1. Install Python & pip:

pkg install python -y


2. Install Telethon:

pip install telethon


3. Save the script as stringgen.py and run:

python stringgen.py


4. Enter your API ID, API Hash (from my.telegram.org), and your phone number.


5. You’ll get a string session printed in the terminal. Copy and keep it safe.




---

✅ Notes

This script uses Telethon because it’s lightweight and reliable.

Your string session is essentially a permanent login — treat it like a password.

For debugging: If you get AuthKeyUnregisteredError, make sure your phone number is correct and linked to the API ID/Hash.
