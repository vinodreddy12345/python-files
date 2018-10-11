
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
#Next, log in to the server
s.login("vinodreddym7.vr@gmail.com", "vinodreddy")
#Send the mail
msg = "hello"
 # The /n separates the message from the headers
s.sendmail("vinodreddym7.vr@gmail.com", "yogi66796@gmail.com", msg)
s.quit()
