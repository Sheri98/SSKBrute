# SSKBrute: Web Directory Discovery Tool

![Badge indicating Python 3.x compatibility](https://img.shields.io/badge/python-3.x-blue.svg)

`SSKBrute` is an efficient and user-friendly web directory discovery tool. Its primary function is to identify potential web directories by iterating through a set of given base URLs combined with potential endpoints.

---

## 🌟 Features

- 🚀 **Multi-threaded Scanning**: Harness the power of concurrent processing for accelerated results.
- 📘 **Intuitive Output**: Crafted for straightforward reading and comprehension.
- 📂 **Automatic Logging**: Seamlessly logs every processed URL along with its corresponding status code.

---

## 📋 Prerequisites

- Python 3.x
- The `requests` library

---

## 🛠 Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/YourUsername/SSKBrute.git
cd SSKBrute


chmod +x PersonalDir.py

    Make the Script Executable (For Linux Users):

bash

chmod +x PersonalDir.py

🚀 Usage

bash

python3 PersonalDir.py [BASE_URLS_FILE] [ENDPOINTS_FILE]

Substitute [BASE_URLS_FILE] with your collection of base URLs and [ENDPOINTS_FILE] with your assortment of endpoints.

Example:

bash

python3 PersonalDir.py base_urls.txt endpoints.txt

📄 Output

SSKBrute continuously updates you on the URLs being processed. It highlights any directories discovered and pairs them with their respective status codes. What's more, all the findings are conveniently saved to a log file for in-depth analysis.
⚠️ Warning

🔴 Caution: If you're inputting a vast list of base URLs and endpoints, be prepared for a significantly large log file. Always keep track of your storage while using the tool.


