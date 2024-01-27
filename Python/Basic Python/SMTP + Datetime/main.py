'''
STMTP 
'''
#----------------------------- IMPORTS -----------------------------#
import smtplib
import datetime as dt
import random

#----------------------------- CONSTANTS ---------------------------#
my_email = "###############"
password = "APP PASSWORD################"
data = "qoutes.txt"

#----------------------------- MAIN --------------------------------#

# SMTP

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
# 					to_addrs="###########",
# 					msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close() Dont need this line it using "with"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="######################",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# DATE/TIME
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1: # 1 = Monday
	with open("quotes.txt") as quote_file:
		all_quotes = quote_file.readlines()
		quote = random.choice(all_quotes)

	print(quote)
	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(my_email, password)
		connection.sendmail(
			from_addr=my_email,
			to_addrs=my_email,
			msg=f"Subject:Monday Motivation\n\n{quote}")
