# Python Email Sender with Encrypted Passwords

This project is a Python script for sending an email with an attachment using Gmail's SMTP server. It is configured to securely handle sensitive information by separating and encrypting both the app password and user password.

## Features

- Sends an email with a custom subject and body
- Allows attaching a file (in this case, `bird.jpg`)
- Secures the user and app passwords by storing them in separate files
- Uses `base64` encoding to store an encrypted user password

## Prerequisites

- **Python 3.x** installed
- **Gmail Account**: The sender's Gmail account should have an [App Password](https://support.google.com/mail/answer/185833?hl=en) if 2-Step Verification is enabled.

## Setup

1. **Clone this Repository:**
   git clone https://github.com/Sachin-Tharaka/Automated-Mail-Sende.git
   cd python-email-sender
  

2. **Set Up Encrypted Password and App Password Files:**
   - **app_password.txt**: Create this file and paste your Gmail App Password inside. **Ensure this file is kept secure.**
   - **password.txt**: Create this file to store the `base64` encoded version of your Gmail password.
     - Encode your Gmail password to base64 with:
       
       import base64
       encoded_password = base64.b64encode(b"your_password").decode("utf-8")
       with open("password.txt", "w") as file:
           file.write(encoded_password)
       
     - Replace `"your_password"` with your actual Gmail password.

3. **Edit the Script**: Replace placeholders for email addresses.
   - `your_email`: Your Gmail address
   - `receiver_mail`: Recipient's email address (can also be your own for testing purposes)

## Usage

Run the script as follows:
python send_email.py

Upon execution, the script will:

1. Load and decrypt the `base64` encoded password.
2. Log in to Gmail's SMTP server using the `app_password`.
3. Create and send an email with the custom message, subject, and any attachments.

## Code Overview

The code imports necessary modules (`smtplib`, `base64`, `MIMEText`, `MIMEBase`, and `MIMEMultipart`), establishes an SMTP connection, and securely reads the app password and encoded user password from separate files.

### Key Sections

- **Base64 Decoding**: Ensures the Gmail user password is decrypted securely.
- **Attachment Handling**: Allows you to attach files, encoded and sent along with the email body.
- **Error Handling**: Detects decoding errors, file errors, and other issues, with meaningful output for troubleshooting.

### Example `message.txt`

This file contains the body of the email message. For example:
```
Hello,

This is a test email sent from Python!

Best regards,
Your Python Script
```

## File Structure

The directory should look as follows:

```
python-email-sender/
├── app_password.txt  # Contains the Gmail app password in plain text
├── password.txt      # Contains the base64 encoded user password
├── message.txt       # Contains the email body text
├── bird.jpg          # File attachment (optional, can be any file)
└── send_email.py     # The main script file
```

## Important Security Note

Never store or share sensitive information like app passwords and user passwords directly in code. Use a secure method for storing credentials in production, such as environment variables or secret management tools.
