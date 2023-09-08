# SSKBrute: Web Directory Discovery Tool

`ShBrute` is a custom web directory discovery tool. Its purpose is to uncover potential web directories by iterating through a list of provided base URLs and potential endpoints.

## Features

- **Multi-threaded scanning**: Leveraging concurrent processing for faster results.
- **Clear and concise output**: Designed for easy reading and interpretation.
- **Automatic logging**: Captures all processed URLs, complete with their status codes, for subsequent analysis.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

 **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/SSKBrute.git
   cd SSKBrute

## Make the script executable (Linux):
```bash
   chmod +x PersonalDir.py

## Usage
```bash
   python3 PersonalDir.py [BASE_URLS_FILE] [ENDPOINTS_FILE]

   Replace [BASE_URLS_FILE] with your list of base URLs and [ENDPOINTS_FILE] with your list of endpoints to test.

   For example:
   python3 PersonalDir.py base_urls.txt endpoints.txt

## Output

The tool offers a continuous display of the URLs being processed and will prominently display any discovered directories with their corresponding status codes. Additionally, all results are persistently stored to a log file.

## ⚠️ Warning

Please be cautious when using this tool, as it can generate a large log file depending on the number of base URLs and endpoints provided.
