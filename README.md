## Budget Telegram Bot (in developing)

### About
A telegram bot for an automation of financial transaction records and budget control. Powered by Aiogram library and Sqlite3 DB. Allows to avoid routine actions when managing own budget by authomatization and decreasing manual touch. Works together only with Apple Shortcut on ios.

#### About shortcut:
The shortcut tracks SMSes from banks and send them to telegram bot via TelegramBot API.
[Download the shortcut.](https://www.icloud.com/shortcuts/e5d3a6c244e7403eb7fa56cabb0fd2ac)

### TODOs:
- [ ] Incoming bank messages handle
- [ ] Bank messages parser
- [ ] Storage transactions in DB
- [ ] Manual handle of unparsed messages
- [ ] Manual expenses and incomes adding 
- [ ] Adding expenses and incomes in Google Sheets 
- [ ] Financial statistics (day, week, month, year, custom period)
- [ ] Debts or payments reminder
- [ ] Tests covering
- [ ] Docker container
- [ ] CI/CD