import smtplib
from config import USERNAME, PASSWORD
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import yagmail


import html
import mimetypes
import ssl
from email.headerregistry import Address
from email.message import EmailMessage
from email.utils import make_msgid
from pathlib import Path

def yagmail_test(to_address, msg_body, image_path):
    yag = yagmail.SMTP(USERNAME, PASSWORD)
    #yag.send(to_address, contents=[yagmail.inline("someimg.png"), "<h1>This is a test</h1>","This is some text as well"])
    yag.send(to_address,
             contents=[yagmail.inline(image_path), "<h1>This is a test</h1>", "This is some text as well"])



def email_attached_img(to_address, msg_body, image_path, img_id):
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()

    # full_email = "\r\n".join([
    #     "From: " + USERNAME,
    #     "To: " + to_address,
    #     "Subject: Test message with image",
    #     "",
    #     msg
    # ])

    full_email = MIMEMultipart()
    full_email['subject'] = "new html message?"
    full_email['To'] = to_address
    full_email['From'] = USERNAME
    full_email.preamble = """Your mail reader does not support the report format.
    Please visit us <a href="http://www.mysite.com">online</a>! """
    #msgAlternative = MIMEMultipart("alternative")
    #full_email.attach(msgAlternative)

    #msgText = MIMEText("This is the alternative message",'plain')
    #msgAlternative.attach(msgText)

    HTML_BODY = MIMEText(msg_body, 'html')

    #msgAlternative.attach(HTML_BODY)
    full_email.attach(HTML_BODY)

    fp = open(image_path,'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Contend-Id','<%s>' % img_id)
    msgImage.add_header('X-Attachment-Id', img_id)
    msgImage.add_header('Content-Disposition','inline; filename=\"' + image_path + '\"')
    full_email.attach(msgImage)

    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, to_address, full_email.as_string())
    server.quit()

def email_message(to_address,msg):
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()

    # full_email = "\r\n".join([
    #     "From: " + USERNAME,
    #     "To: " + to_address,
    #     "Subject: Test message with image",
    #     "",
    #     msg
    # ])

    full_email = MIMEMultipart('alternative')
    full_email['subject'] = "Html message?"
    full_email['To'] = to_address
    full_email['From'] = USERNAME
    full_email.preamble = """Your mail reader does not support the report format.
Please visit us <a href="http://www.mysite.com">online</a>! """

    HTML_BODY = MIMEText(msg,'html')

    full_email.attach(HTML_BODY)

    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, to_address, full_email.as_string())
    server.quit()


def email_test():
    title = 'More picture reports'
    path = Path('someimg.png')
    #me = Address("Pepé Le Pew", *gmail_user.rsplit('@', 1))

    msg = EmailMessage()
    msg['Subject'] = 'Picture email!'
    msg['From'] = USERNAME
    msg['To'] = "tmsteem82@gmail.com"
    msg.set_content('[image: {title}]'.format(title=title))  # text/plain
    cid = 1 #make_msgid()[1:-1]  # strip <>
    msg.add_alternative(  # text/html
        '<div>This is a random title</div><div><img src="cid:{cid}" alt="{alt}"/></div>'
            .format(cid=cid, alt=html.escape(title, quote=True)),
        subtype='html')
    maintype, subtype = mimetypes.guess_type(str(path))[0].split('/', 1)
    msg.get_payload()[1].add_related(  # image/png
        path.read_bytes(), maintype, subtype, cid="<{cid}>".format(cid=cid))

    # save to disk a local copy of the message
    Path('outgoing.msg').write_bytes(bytes(msg))

    with smtplib.SMTP('smtp.gmail.com', timeout=10) as s:
        s.starttls(context=ssl.create_default_context())
        s.login(USERNAME, PASSWORD)
        s.send_message(msg)


if __name__ == "__main__":
    email_test()
