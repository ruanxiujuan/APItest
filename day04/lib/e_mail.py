"""发送邮件"""
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import email_config


def send_email(report_file):
    # 1. 组装邮件正文
    msg = MIMEMultipart()
    body = MIMEText(email_config["body"], "plain", "utf-8")
    msg.attach(body)  # plain纯文本/html

    # 2. 组装邮件头
    msg["From"] = email_config["user"]
    msg["To"] = email_config["receiver"]
    msg["Subject"] = email_config["subject"]

    # 3. 添加附件
    attr = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    attr["Content-Type"] = "application/octet-stream"
    attr["Content-Disposition"] = "attachment; filename='report.html'"
    msg.attach(attr)

    # 4. 连接smtp服务器并发送邮件
    smtp = smtplib.SMTP(email_config["server"])   # 连接smtp服务器
    smtp.login(msg["From"], "hanzhichao123")  # 登录
    smtp.sendmail(msg["From"], msg["To"], msg.as_string())  #发送
    logging.info("邮件发送完成")