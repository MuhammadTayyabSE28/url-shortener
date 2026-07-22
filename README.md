# URL Shortener

## Description

The URL Shortener is a web application built using Python, Flask, and SQLite. It allows users to convert long URLs into short, unique links. When a shortened URL is accessed, the application automatically redirects the user to the original website.

This project demonstrates the use of Flask routing, form handling, SQLite database integration, and URL redirection.

---

## Features

- Generate unique short URLs
- Redirect users to the original website
- Store URL mappings in an SQLite database
- Responsive and user-friendly interface
- Simple and lightweight design

---

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3

---

## Project Structure

```text
url_shortener/
│
├── app.py
├── urls.db
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/url-shortener.git
```

### 2. Navigate to the project directory

```bash
cd url-shortener
```

### 3. Install the required dependency

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

---

## Usage

1. Open your browser and visit:

```text
http://127.0.0.1:5000
```

2. Enter a valid long URL.

Example:

```text
https://www.google.com
```

3. Click **Generate Short URL**.

4. The application generates a unique short URL.

Example:

```text
http://127.0.0.1:5000/A1b2C3
```

5. Click the generated short URL to open the original website.

---
## Database

This project uses SQLite as the database.

### Table: `urls`

| Column Name  | Data Type | Description                            |
|--------------|-----------|----------------------------------------|
| id           | INTEGER   | Primary key (Auto Increment)           |
| original_url | TEXT      | Stores the original long URL           |
| short_code   | TEXT      | Stores the generated unique short code |

---

## Requirements

Create a `requirements.txt` file with the following content:

```text
Flask
```

---

## Future Improvements

- Custom short URLs
- Copy URL button
- QR code generation
- Click analytics
- User authentication
- URL expiration

---

## Screenshots

You can add screenshots of the application here.

- Home Page
- Generated Short URL
- Redirect Result

---

## Author

**Muhammad Tayyab**

Software Engineering Student  
SZABIST Islamabad

GitHub: https://github.com/your-github-username

LinkedIn: https://linkedin.com/in/your-linkedin-profile

Email: your-email@example.com

---

## License

This project is intended for educational and portfolio purposes.