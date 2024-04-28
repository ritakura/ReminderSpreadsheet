import smtplib
import pandas as pd
import gspread
from datetime import date
from oauth2client.service_account import ServiceAccountCredentials
import config
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = config.EMAIL
    msg['from'] = user
    password = config.PASS

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def send_text():
    SCOPE = ['https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name(config.JSON, SCOPE)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    spreadsheet = client.open_by_key(config.SHEETS_ID)
    schedule_data = spreadsheet.worksheet("Current_Week").get_all_values()
    volunteers_data = spreadsheet.worksheet("Info").get_all_values()

    # Convert data to DataFrames
    schedule = pd.DataFrame(schedule_data[1:], columns=schedule_data[0])
    volunteers = pd.DataFrame(volunteers_data[1:], columns=volunteers_data[0])

    # Grab today's day
    today = date.today()
    days = {    0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday" }
    dow = (today.weekday() + 1) % 7

    # Grab people scheduled for tomorrow
    tmr = schedule[days[dow]]
    people = {}
    for i in range(0, len(tmr)):
        if tmr[i] == "":
            continue
        if tmr[i] in people.keys():
            continue
        people[tmr[i]] = i + 6

    # Send texts
    for x in people:
        num = volunteers[x][0]
        carrier = volunteers[x][1]
        email_alert("Reminder:", "You are scheduled to volunteer tomorrow at " + str(people[x]) + ":00.", str(num) + "@" + carrier)

if __name__ == '__main__':
    send_text()