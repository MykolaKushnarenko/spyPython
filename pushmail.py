import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os

filepath = "C:/Users/Niko/Downloads/snake.abc"
basename = os.path.basename(filepath)

part = MIMEBase('application', "octet-stream")
part.set_payload(open(filepath,"r").read())
encode_base64(part)

toaddr = ['<nikokusha@gmail.com>']
me = 'From: My Name <hackbancry@gmail.com>'
you = 'To: ' + ', '.join(toaddr)

server = 'smtp.gmail.com' # Сервер отпраитель
port = 25 # возможные порты: 587, 465
user_name = 'hackbancry@gmail.com' # Адрес отправителя
user_passwd = 'silvercrown1' # Пароль отправителя

# Формируем заголовок письма
msg = MIMEMultipart('mixed')
msg['Subject'] = 'Заголовок письма'
msg['From'] = me
msg['To'] = toaddr[0] # отправка 2-м адресаиам
#msg['cc'] = ', '.join([ toaddr[2] ]) # отправка копии 1-му адресату

# Формируем письмо
part1 = MIMEText('ку', 'plain')
#part2 = MIMEText('Содержимое приложенного файла', 'text/html;name="tasks.htm"', 'utf-8')
msg.attach(part1)
#msg.attach(part2)
msg.attach(part)
# Подключение
s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()
# Авторизация
s.login(user_name, user_passwd)
# Отправка пиьма
s.sendmail(me, toaddr, msg.as_string())
s.quit()