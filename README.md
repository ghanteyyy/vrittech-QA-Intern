# QA Automation – Signup Flow

## Overview
This repository contains a QA automation script for validating the **end-to-end signup process** of the Authorized Partner web application.
The automation covers UI interactions, OTP-based email verification, dynamic form handling, dropdown/combobox selection, and document uploads using **Selenium WebDriver** and the **mail.tm API**.

This README documents **all steps required to set up the environment** in the company People/Internal system and run the automation successfully.

---

## Prerequisites
Make sure the following are installed on your system:

- **Python:** 3.9 or higher
- **Google Chrome:** Latest stable version
- **Git:** Optional (for cloning repository)
- **Internet Connection:** Required for OTP email service

---

## Step 1: Clone the Repository
```bash
git clone https://github.com/ghanteyyy/vrittech-QA-Intern.git
cd vrittech-QA-Intern
```

Alternatively, download the ZIP file and extract it.

---

## Step 2: Create a Virtual Environment (Recommended)

### Windows
```bash
python -m venv env
env\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv env
source env/bin/activate
```

---

## Step 3: Install Required Dependencies
Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

## Step 4: Set Up ChromeDriver (Windows)
1. Download chrome for testing version: <br>
   https://storage.googleapis.com/chrome-for-testing-public/143.0.7499.169/win64/chrome-win64.zip

2. Download chrome driver: <br> https://storage.googleapis.com/chrome-for-testing-public/143.0.7499.169/win64/chromedriver-win64.zip


---

## Step 5: Run the Automation Script
From the project root directory:

```bash
python main.py
```

---

## What the Script Does
1. Launches Chrome browser
2. Navigates to the signup page
3. Accepts required terms
4. Generates a temporary email address
5. Fills personal and agency details
6. Retrieves OTP from email inbox
7. Verifies OTP automatically
8. Selects dropdown/combobox options
9. Uploads required documents
10. Submits the final signup form

---

## Execution Notes
- Do not close the browser manually during execution
- OTP delivery may take a few seconds
- Stable internet connection is required
- The browser may remain open briefly for observation

---

## Troubleshooting

### Chrome Not Found
Ensure that Google Chrome is installed and place it in the project directory.

### ChromeDriver Version Mismatch
Download a ChromeDriver version that matches your installed Google Chrome version and place it in the project directory.


### OTP Not Received
Retry execution; mail.tm inbox polling may take a few seconds.

### Element Not Clickable / Stale Element Errors
Handled internally using explicit waits and retry logic.

---

## Best Practices
- Always use a virtual environment
- Run only one instance at a time
- Avoid hardcoding sensitive credentials
- Update locators if UI changes
- Keep Chrome and ChromeDriver versions in sync

---

## Future Improvements
- Add assertions and validations
- Screenshot capture on failure
- Structured logging and reporting
- PyTest integration with Page Object Model (POM)
- CI/CD pipeline execution

---
