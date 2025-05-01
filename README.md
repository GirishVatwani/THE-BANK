# 💬 Telegram Bank Bot

A secure and interactive **Banking Bot** built using **Python** and the **Telegram Bot API**, designed to simulate basic banking functionalities for customers. The bot offers features like account creation, email verification, transaction history, and more — all accessible through a simple Telegram chat interface.

---

## 🚀 Features

- ✅ **Customer Account Creation**  
  Register new customers with basic details and verification.

- 📧 **Email Verification**  
  Validate email addresses before account creation.

- 🔐 **Unique Customer ID Generation**  
  Uses Regex patterns to generate and validate unique customer IDs.

- 📄 **Transaction Management**  
  Deposit and withdraw funds with real-time feedback.

- 📈 **Reports Based on Privileges**  
  Admin and user roles with different access levels to account data.

- 📜 **Last 10 Transactions View**  
  Instantly view your most recent transactions.

- 📊 **Full Transaction History in Excel**  
  Download complete account statements in `.xlsx` format.

- 🔔 **Notifications**  
  Get instant alerts on every deposit or withdrawal.

---

## 🛠️ Tech Stack

- **Language**: Python 3.13  
- **Telegram Bot Library**: python-telegram-bot v21.7  
- **Database**: SQLite / MySQL (based on your implementation)  
- **File Handling**: Excel file generation via `pandas` and `openpyxl`  
- **Email Handling**: `smtplib` or relevant email verification module  

---

## 📦 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/telegram-bank-bot.git
   cd telegram-bank-bot
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables or config**  
   Add your Telegram Bot Token, email credentials, etc., in a `.env` file or a config script.

4. **Run the bot**  
   ```bash
   python bot.py
   ```

---

## 🧪 Example Commands

- `/start` – Welcome message and options  
- `/create_account` – Starts account creation  
- `/deposit` – Add funds  
- `/withdraw` – Withdraw funds  
- `/transactions` – Shows last 10 transactions  
- `/history_excel` – Sends transaction history as Excel  
- `/admin_report` – (Admin only) Generates user-wide reports  

---

## 🔐 Security Notes

- Input validation included for user data.  
- Email and ID verification prevent duplicate or fake entries.  
- Role-based data access ensures privacy.

---

## 🤝 Contributing

Feel free to fork this repo and raise a pull request if you have suggestions or new features in mind!

---

## 📧 Contact

For feedback or issues, contact [your-email@example.com] or message [@YourTelegramUsername](https://t.me/YourTelegramUsername)
