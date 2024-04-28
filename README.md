# ReminderSpreadsheet
Semi-automated texts to send volunteers reminders the day before their shift.\
Author: Reina Itakura (ritakura@ucdavis.edu) Contact for any questions.

# Setting up Google Account
1. Create a new google account or use an existing one.
2. Enable 2-factor authentication.
3. Create a App password.
4. Go to the google cloud console and enable the Google Spreadsheets API.
5. Create a Service Account and enable all necessary permissions.
6. Generate an access key and download the JSON file to directory where the python script will be.

# Setting up the Spreadsheets
Example of a google spreadsheet: https://docs.google.com/spreadsheets/d/**1EQAbS30ys5ZKUQ4GyYd-4EP20yWKFuJSSZrpFxZet90**/edit#gid=0
- The Spreadsheet ID of this google spread sheet is the part in bold. Record the spreadsheet ID of **YOUR** google spreadsheet
- The Spreadsheet must be in this format.
- Use this link to determine the sms gateway domain for a volunteer's carrier: https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/

# Setting up the Python Script
1. Make sure you have python installed.
2. Install any necessary packages
3. Go into the config.py file and replace all square brackets with the corresponding vales for your google account.
- EMAIL = "xxx@gmail.com"
- PASS = "App password created during Google Account setup"
- SHEETS_ID = "The long alphanumeric string in bold"
- JSON = "file name of the json file you downloaded when generating an access key"
4. You should be ready to run the script.

# How to run
1. Complete all previous steps
2. run the alert.py script: $ python alert.py
3. Volunteers scheduled to volunteer on the next day will receive text messages.

# Demo
https://drive.google.com/file/d/1DIEHfPZfzCc-SpuYh-M-CSTFJQT7IX9j/view?usp=drive_link
