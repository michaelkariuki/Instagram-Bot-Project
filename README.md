# Instagram Bot with InstaPy

![InstaPy Logo](https://github.com/timgrossmann/InstaPy/raw/master/assets/logo.png)

## Introduction

This Python script utilizes InstaPy, a powerful Instagram automation library, to automate interactions on the platform. The bot performs actions such as following users, liking posts, and leaving comments based on specific criteria.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.7 or later)
- [InstaPy](https://github.com/timgrossmann/InstaPy)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/michaelkariuki/Instagram-Bot-Project.git
    cd your-repo
    ```

2. Install dependencies:

    ```bash
    pip install instapy python-dotenv
    ```

3. Create a `.env` file in the project root and add your Instagram credentials:

    ```env
    USERNAME=your_instagram_username
    PASSWORD=your_instagram_password
    ```

## Usage

Run the script to automate interactions on Instagram. The bot will perform actions like following users, liking posts, and leaving comments based on the configured settings.

```bash
python instaPy.py
```

## Configuration

Customize the bot's behavior by modifying the script. Adjust parameters like hashtags, quotas, relationship bounds, skip users conditions, and more to fit your preferences.

## Disclaimer

Use this script responsibly, respecting Instagram's terms of service. Excessive automation may lead to account restrictions or bans. Adjust the script settings to ensure natural interactions.

## Contributing

Feel free to contribute to this project by creating issues, proposing new features, or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).