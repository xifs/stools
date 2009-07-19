#encoding=utf-8

import os,smtplib

smtp = 'smtp.gmail.com'
come = 'gsli52@gmail.com'
to = 'xiws13@gmail.com'
mail = 'Subject:test'
server = smtplib.SMTP(smtp)
server.sendmail(come,to,mail)
server.quit()
