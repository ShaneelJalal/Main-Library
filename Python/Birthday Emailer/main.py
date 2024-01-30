'''
Birthday Mailer
'''
#----------------------------- IMPORTS -----------------------------#
import smtplib
import datetime as dt
import random
import pandas

#----------------------------- CONSTANTS ---------------------------#
today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
my_email = "################"
password = "####################"

#----------------------------- MAIN -------------------------------#

# new_dict = {new_key:new_value for (index, row) in data.iterrows()}
birthdays_dict = {(data_row["month"], data_row["day"]): data_row
                  for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
