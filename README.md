# Asset Miner

![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

An asset miner and secret scanner for web reconnaissance. This tool scrapes a target URL to find linked JavaScript files, downloads them for manual review, and scans them for hardcoded secrets like API keys and tokens.

### Created by: nashedi_x_coder

***

## 📜 Description

As a penetration tester or bug bounty hunter, reconnaissance is a critical phase. `asset_minner` automates a part of this process by discovering and analyzing JavaScript files associated with a target domain. Developers often accidentally leave sensitive information like API keys, hidden endpoints, or other secrets in their client-side code. This tool helps you find them quickly.

## ✨ Features

-   **JS File Discovery:** Automatically finds all linked JavaScript files from a given URL.
-   **Local Caching:** Saves a local copy of every discovered JS file into a directory named after the target domain for manual inspection.
-   **Secret Scanning:** Scans the content of each file for common patterns of secrets using regular expressions.
-   **Extensible:** Easily add new secret patterns to the script to expand its capabilities.
-   **Aesthetic UI:** A clean and stylish command-line interface.

## 🚀 Getting Started

### Prerequisites

-   Python 3.6+
-   pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/NASHEDIxCODER/asset_minner.git
    cd asset_minner
    ```

2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the tool from your terminal by providing a target URL with the `-u` or `--url` flag.

```bash
python scanner.py -u [https://example.com](https://example.com)


## 🤝 Contributing

Contributions are welcome and greatly appreciated! This project is open source, and I encourage the community to help make it even better.

You can contribute in several ways:
-   **Reporting Bugs:** If you find a bug, please open an issue on the GitHub repository.
-   **Suggesting Enhancements:** Have an idea to make this tool better? Feel free to open an issue to discuss it.
-   **Adding Secret Patterns:** The easiest way to contribute is by adding more regex patterns to the `SECRET_PATTERNS` dictionary in `scanner.py`.
-   **Pull Requests:** If you want to add a new feature or fix a bug yourself, please follow the standard fork and pull request workflow.

### Pull Request Process
1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

Don't forget to add your name to a list of contributors if you'd like!
