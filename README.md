# Password-checker
 Password Strength Analyzer with Custom Wordlist Generator

A GUI-based Python tool that analyzes password strength, generates strong suggestions, and builds custom wordlists from personal hints using smart patterns and leetspeak.

---

## Features

-  **Check Password Strength**  
  Estimate password strength using `zxcvbn` with crack time and feedback.

- 🛠 **Generate Wordlist from Personal Info**  
  Use name, date of birth, pet name to create targeted wordlists with:
  - Leetspeak variants
  - Suffixes like `123`, `2025`
  - Capitalized forms

-  **Suggest Strong Passwords**  
  Randomly generate strong 12-character passwords with symbols, digits, and mixed case.

---



---

##  Folder Structure
PasswordSecurityToolkit/
├── app.py
├── password_checker.py
├── wordlist_generator.py
├── wordlists/
│ └── custom_wordlist.txt
├── README.md
└── requirements.txt

