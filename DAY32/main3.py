import smtplib
import  datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
MY_EMAIL = "12112041.it@gmail.com"
MY_PASSWORD ="zocefqkubyswdgqy"
if weekday == 1:
    with open(file = "DAY32/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=MY_EMAIL,
                msg= f"Subject:Monday Motivation\n\n{quote}"
            )