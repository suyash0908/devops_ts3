#!/bin/bash/python3
import smtplib

s=smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login("anand31798@gmail.com","3179724774937007")

subject1='Important'


message1 = "your latest code ha been failed, please debug it as soon as possible."

s.sendmail("anand31798@gmail.com","1706298@kiit.ac.in",message1)

s.quit()
