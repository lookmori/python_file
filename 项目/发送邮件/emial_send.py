import smtplib

from email.mime.text import MIMEText

from email.header import Header

# 邮件服务器地址
mail_host = 'smtp.163.com'
#用户名
mail_user = 'v18338258072@163.com'
# 用户密码
mail_password = '3364487975lfp.'


sender = 'v18338258072@163.com'
#接受邮件人
receivers = ['lookmori@163.com']

# 普通文本格式
message = MIMEText('python 发送邮件实验','plain','utf-8')

# html 格式邮件
# email_html = """<h1>点击我试一试</h1><a href='www.baidu.com'>这是html格式邮件，点击我跳转到百度</a> """
# message = MIMEText(email_html,'html','utf-8')

message['From'] = Header('发送头','utf-8')
message['To'] = Header('接收头','utf-8')

# 邮件主题
subject = 'PYTHON stmp 邮件测试'
message['Subject'] = Header(subject,'utf-8')

try:
    smtobj = smtplib.SMTP()
    smtobj.connect(mail_host,25)
    smtobj.login(mail_user,mail_password)
    smtobj.sendmail(sender,receivers,message.as_string())
    print('发送邮件成功！')
except smtplib.SMTPException:
    print('无法发送邮件')