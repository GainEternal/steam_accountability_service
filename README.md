# steam_accountability_service
Automatically notify a friend (or simply yourself!) when a steam game has started, and notify them of the total time played when finished. 


## Setup
This service is intended to run on a local computer.  It requires 3 environment variables:
- GMAIL_SENDER_EMAIL:     The email address of the sender
- GMAIL_SENDER_PASSWORD:  The password required to sign-in to the sender's email (instructions below)
- EMAIL_RECEIVER_EMAIL:   A single recipient, or a list of recipients, having the form "john@mail.com, cass@mail.com"

## Gmail Password

In order for smtplib to send an email through a gmail account, an app-specific gmail password must be generated.  A furture version of this code may allow Oauth2 for greater security.

In order to generate an app password for your gmail account, complete the following steps (accurate on 04/01/2024):
1. Enable 2-step verification (if not currently enabled).
2. Select "2-Step Verification"
3. Under "App passwords", select "App passwords"
4. Enter a name for your app (e.g., "steam_emailer")
5. Enter the password given into the environment variable: GMAIL_SENDER_PASSWORD
