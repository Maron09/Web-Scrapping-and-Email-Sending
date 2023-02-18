import requests  #http requests


from bs4 import BeautifulSoup # Web Scraping
import smtplib #email body
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
import datetime #System data and time manipulation

now = datetime.datetime.now()

#email content placeholder

content = ""


#extracting News Stories


def extract_news(url):
    print("Extracting News Stories......")
    cnt = ""
    cnt += ("<b> News Top Stories: </b>\n" + "<br>" + "-"*50+ "<br>")
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class','title','valign',''})):
        cnt+= ((str(i +1) + '::' + tag.text + '\n' + '<br>') if tag.text != 'More' else '')
    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ("<br>==========<br>")
content += ("<b><br>End of Message")


# Let's send the email
print(("Composing Email...."))

#Update your email details
SERVER = 'smtp.gmail.com' #smtp server
PORT = 535 #smtp port
USERNAME = 'example@gmail.com' #email address
PASSWORD = '********' #email password
TO = 'example@gmail.com' #recipient email address


#fb = open(file_name, 'rb')
#Create a text/plain message
msg = MIMEMultipart()

#msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['Subject'] = 'News Top Stories' + '' + str(now.day) + '-' + str(now.month) + '-' + str(now.month) + '-' + str(now.year)
msg['TO'] = TO
msg['From'] = USERNAME

msg.attach(MIMEText(content, "html"))
#fb.close()

print("Initiating Server.....")

server = smtplib.SMTP_SSL('smtp.gmail.com')
EMAIL_USE_TLS = False
#server = smtplib.SMTP SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
# server.starttls()
server.ehlo()
server.login(USERNAME, PASSWORD) 

print("Sending Email.....")

server.sendmail(USERNAME, TO)
server.sendmail(USERNAME, TO, msg.as_string())

print("Email Sent....")

server.quit()