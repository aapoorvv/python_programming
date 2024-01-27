import smtplib

my_email = "12112041.it@gmail.com"
passw = "zocefqkubyswdgqy"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user = my_email, password = passw)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="ap2002gupta@gmail.com", 
        msg="Subject:Hello\n\nbody-Hello"
    )
