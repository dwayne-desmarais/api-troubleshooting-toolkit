# API Troubleshooting Toolkit

A Python command-line utility designed to help Technical Support Engineers and Application Support professionals quickly test REST API endpoints, inspect responses, and gather troubleshooting information.

---

## Overview

The API Troubleshooting Toolkit was built to simulate the types of diagnostics performed by support engineers when investigating API-related issues. The tool sends HTTP requests, measures response times, inspects response headers, formats JSON responses, and records request details for troubleshooting.

This project demonstrates practical Python programming, REST API troubleshooting, and technical documentation skills that are directly applicable to enterprise SaaS support environments.

---

## Features

Current Version (v1.0)

- Send HTTP GET requests
- Display HTTP status codes and response messages
- Measure API response times
- Display response headers
- Pretty-print JSON responses
- Handle common connection and request errors
- Generate timestamped log files

Planned Features

- POST, PUT, PATCH, and DELETE requests
- Bearer Token authentication
- API Key authentication
- Basic Authentication
- Custom request headers
- Retry logic
- Export results to JSON and CSV
- Command-line arguments using argparse

---

## Technologies

- Python 3
- Requests
- JSON
- REST APIs
- Logging
- Git
- GitHub

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/api-troubleshooting-toolkit.git
```

Move into the project folder

```bash
cd api-troubleshooting-toolkit
```

Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Usage

Interactive Mode

```bash
python main.py
```

Example URL

```text
https://jsonplaceholder.typicode.com/posts/1
```

Future Command-Line Mode

```bash
python main.py --url https://jsonplaceholder.typicode.com/posts/1
```

---

## Example Output

```text
==================================================
        API Troubleshooting Toolkit v1.0
==================================================

Target URL
--------------------------------------------------
https://jsonplaceholder.typicode.com/posts/1

Sending request...

Request completed successfully.

Request Summary
--------------------------------------------------
Status Code     : 200 OK
Response Time   : 142.31 ms
Content Type    : application/json
Response Size   : 292 bytes
```

---

## Project Structure

```
api-troubleshooting-toolkit/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── main.py
│
├── logs/
│
├── docs/
│   └── screenshots/
│
└── examples/
```

---

## Skills Demonstrated

- Technical troubleshooting
- REST API testing
- HTTP response analysis
- Python development
- JSON parsing
- Error handling
- Logging
- Technical documentation
- Git version control

---

## Lessons Learned

This project has provided hands-on experience building a reusable troubleshooting utility while reinforcing best practices for writing maintainable Python code, documenting technical projects, and working with REST APIs.

Future enhancements will focus on authentication, additional HTTP methods, and improved reporting to more closely reflect tools used in enterprise support environments.

---

## Roadmap

### Version 1.1

- Command-line arguments
- Improved logging
- Better console formatting

### Version 2.0

- POST requests
- PUT requests
- DELETE requests
- Authentication
- Retry logic

### Version 3.0

- HTML reports
- CSV export
- Configuration file
- Automated testing

---

## Author

**Dwayne Desmarais**

Bachelor of Science, Computer Science

Technical Support Specialist

Interested in Technical Support Engineer, Application Support, and SaaS Support roles.

GitHub Portfolio:
https://dwayne-desmarais.github.io/
