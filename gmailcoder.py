import base64
import os.path
import time
import re
import logging

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Setup logging
logging.basicConfig(level=logging.INFO)

SCOPES = ['https://mail.google.com/']


def get_verification_code():
    creds = None

    try:
        if os.path.exists('token.json'):
            logging.info("Loading credentials from token.json")
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                logging.info("Refreshing expired credentials...")
                creds.refresh(Request())
            else:
                logging.info("Launching browser to authenticate via credentials.json")
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('gmail', 'v1', credentials=creds)
        time.sleep(3)

        logging.info("Polling inbox for verification code...")
        while True:
            results = service.users().messages().list(
                userId='me', maxResults=5, q='subject:Sign in to Million').execute()
            messages = results.get('messages', [])

            if not messages:
                logging.info("No new messages, retrying in 5s...")
                time.sleep(5)
                continue

            for msg in messages:
                full_msg = service.users().messages().get(userId='me', id=msg['id']).execute()
                snippet = full_msg.get('snippet', '')
                logging.info("Snippet: " + snippet)

                match = re.search(r'\b\d{6}\b', snippet)
                if match:
                    code = match.group(0)
                    logging.info("Found code: " + code)
                    return code

            time.sleep(5)

    except Exception as e:
        logging.error("Error occurred: %s", e)
        
def clear_login_emails(service):


    try:
        results = service.users().messages().list(
            userId='me',
            q='subject:"Sign in to Million"',
        ).execute()

        messages = results.get('messages', [])
        if not messages:
            print("No old login emails to clear.")
            return

        for msg in messages:
            service.users().messages().delete(userId='me', id=msg['id']).execute()
        print(f"Cleared {len(messages)} old login email(s).")

    except Exception as e:
        print("Failed to clear old login emails:", e)

if __name__ == "__main__":
    get_verification_code()
