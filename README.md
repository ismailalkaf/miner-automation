# Monero-Miner
# ⚠️ DISCLAIMER

This project is provided **for educational purposes only**. The developer is **not responsible** for any misuse, consequences, damage, or violations resulting from the use of this code. **Use at your own risk.**

---
This project uses XMRIG CC by [Bendr0id](https://github.com/Bendr0id/xmrigCC)

<p style="color:red;"><strong>IMPORTANT:</strong>For Now the code only supports MONERO mining, if this gets attention il add other CPU intensive options for mining. OR you can edit the command.txt file yourself if you know what you are doing.</p>

# 💻 Browser Miner Automation with Playwright

This project automates browser-based crypto mining using [Playwright](https://playwright.dev/python/) and Google account OTP-based login. It logs into a vulnerable platform, opens multiple tabs, and injects a safe JavaScript-based keep-alive script to maintain mining sessions.

## ⚙️ Features

- 🔐 Auto-login using Gmail OTP (via Gmail API)
- 🚀 Multi-tab mining automation (customizable tab count)
- 🧠 JavaScript-based keep-alive system (safe & non-intrusive)
- 🔄 Command injection into terminal through the web interface
- 🧼 Email cleanup to avoid inbox clutter
- 💵 You Get approx 700-800 Hashrate on every TAB
- TO DO - More advance detections for inactivity, Better config optimization, aim for higher hashrate 

## 🛠 Requirements
- Python 3.10+
- Playwright 
- Gmail API credentials (`credentials.json`)
- Google API packages:
  ```bash
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
- Install playwright browser binaries
  
## 📁 Setup

1. **Clone the Repository**
  ```bash
  git clone https://github.com/AryanSLAYERRR/miner-automation.git
  cd miner-automation
  ```

2. **Install Python Dependencies**
  ```bash
  pip install -r requirements.txt
  playwright install
  ```

3. **Set Up Gmail API**
   
  🟥 **NOTE** 
  **You will be giving the BOT full access to your gmail, so using alt gmail ID is highly preffered**
  
  1. **Create a Google Cloud Project**
      - Go to: https://console.cloud.google.com/
      
      - Click "Create Project" → give it a name (like “Gmail Login BOT”).
    
  2. **Enable Gmail API**
      - After project is created, go to "APIs & Services" > Library.
      
      - Search for "Gmail API" → Click Enable.

  3. **Create OAuth Credentials**
      - Go to APIs & Services > Credentials.
      
      - Click "Create Credentials" → OAuth client ID
      
      - Choose Desktop App.
      
      - Download the credentials.json file.
      
      - Rename it credentials.json and save it in the same directory


4. **Add Your Monero Wallet Address**
      - Use any wallet supported by nanopool.org,
        Open `command.txt` and edit the field (Your_wallet_address) with you own wallet address, there are 3 such fields

5. **Add your email**
      - Head to main.py and edit ("your_email") with the email you used for creating the cloud project

## 🚀 Usage

Run the script:

```bash
python gmailcode.py
```
The script will:
  - Open up a google auth window
  - Select the account you used to create credentials.json
  - You may get an error of insufficent access, or the dev has not allowed you to access it
  - To fix this, Go to console.cloud.google.com
  - Open your project
  - Go to APIS
  - Then Go to OAuth consent Screen
  - Click on Audience
  - Under Test Users, Click on Add users
  - Fill the email you used for this project
  - Save
  - Now rerun `python gmailcode.py`
  - If Sucessfull, it should save a file named `token.json`

  - Now Run
    ```bash
    python main.py
    ```
  - This will start the program and you should see chromium tab pop up and simulating the login process for you

**OPTIONS**
  - You can edit the num_tabs field if you want more tabs mining ( Do not exceed more than 90% ram consumption, as it may cause forceful inactivity)
  - To check mining progress, head to https://nanopool.org and enter your wallet address in the search field

  20 tabs being run
  ![image](https://github.com/user-attachments/assets/7c697625-3813-4759-a4d7-9e380e3ca116)

  ![image](https://github.com/user-attachments/assets/fc672b28-2438-41c5-951b-de3ff1b932bb)

**NOTE**
**THIS IS AN EXPLOIT AND MAY STOP WORKING IF PATCHED**

## 🧠 How Keep-Alive Works

Instead of sending keystrokes, we inject the following safe JavaScript:
- Scrolls the page slightly up and down
- Focuses the terminal's hidden input field
- Dispatches an `input` event

This keeps the mining sessions alive without disrupting the actual terminal behavior.

## 📂 Project Structure

```
miner-automation/
├── gmailcode.py                # Gmail OTP handler
├── main.py                     # Main automation logic
├── command.txt                 # Paste your mining command here
├── credentials.json            # Google OAuth client credentials
├── token.json                  # Auto-generated on first login
├── requirements.txt
├── .gitignore
├── README.md
```

## 🔒 Security Notes

- Your Gmail credentials are stored locally and securely.
- Never share `credentials.json` or `token.json`.
- Avoid using accounts with 2FA unless you're using app passwords.

## 📌 Disclaimer

This project is intended for educational purposes only. Use it responsibly and ensure you're not violating any terms of service or mining policies of the platform you're interacting with.

## 📜 License

MIT License

Copyright (c) 2025 AryanSLAYERRR

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

Created with 💻 by [Aryan Gupta](https://github.com/AryanSLAYERRR)

