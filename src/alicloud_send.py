#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# IMPORTANT: READ BEFORE DOWNLOADING, COPYING, INSTALLING OR USING.
#
#  By downloading, copying, installing or using the software you agree to this license.
#  If you do not agree to this license, do not download, install,
#  copy or use the software.
#
#
#       Shanghai ShanMing Information & Technology Ltd. License Agreement
#                For quant trade strategy and library
#
# Copyright (C) 2017, Shanghai ShanMing Information & Technology Ltd., all rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are NOT permitted.
#
# @Time    : 2018/8/23 下午8:02
# @Author  : Gaowei Xu
# @Email   : gaowxu@hotmail.com
# @File    : alicloud_send.py
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.header import Header


class AutoSender(object):
    """
    auto email sender class
    Reference: http://www.runoob.com/python/python-email.html
    Tools reference: https://qun.qq.com/member.html#gid=220543148
    """

    def __init__(self, source_addr_csv_file):
        """
        initialization
        """
        self._source_addr_csv_file = source_addr_csv_file

    @staticmethod
    def html_content():
        """
        get html content

        :return:
        """
        html_content = """
        <html>
        <head>
            <meta charset="UTF-8">
            <title>工科论文代写</title>
        </head>
        <body>
        <h2 style="color: midnightblue">工科论文代写</h2>

        <div>
           <span>
               <strong style="color: midnightblue">
                    毕业论文，学术论文（本科，全日制硕士，在职硕士），
                    专业为
                   <b style="color: rebeccapurple">
                       计算机／软件工程／电子科学／自动化／信息工程／大数据／仪器科学等专业
                   </b>
                   提供高质量论文代写服务！
                </strong>
           </span>
        </div>

        <div>
            <p style="color: darkslategrey; " >
                同学，您好，我们是由复旦大学／上海交大／东南大学／中科院微电子所／浙江大学／港科大硕士，博士组成的团队，专业涵盖电子／计算机／软件工程／
                自动化／信息工程等，专业提供高质量的工科论文代写服务！我们团队成员在攻读硕士博士期间曾发表过EI/SCI文章数量超30篇之多！
                曾服务过四川大学，东南大学，北京大学，北京邮电大学，上海交通大学的同学们，均顺利毕业和在期刊发表文章！
            </p>
            <span>具体课题咨询与报价请联系微信"不喂大侠"，微信号为：my_wind33</span>
        </div>
        </body>
        </html>
        """
        return html_content

    def get_all_email_addrs(self):
        """
        get all emails address (needs to be sent to)

        :return:
        """
        email_addr_container = list()

        rf = open(self._source_addr_csv_file, 'rb')
        lines = rf.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            email_addr_container.append(line)
        rf.close()

        return email_addr_container

    def send(self, username='buweidaxia@papersoeasy.com', password='XGW1qaz2wsx_das', replyto='pumandaxia@163.com'):
        """
        send email to each receiver

        :param username: 发件人地址，通过控制台创建的发件人地址
        :param password: 发件人密码，通过控制台创建的发件人密码
        :param replyto: 自定义的回复地址
        :return:
        """
        # obtain receivers
        receivers = self.get_all_email_addrs()
        receivers_amount = len(receivers)

        # send email for each receiver
        for i, receiver in enumerate(receivers):
            message = self.build_email_content(
                username=username,
                replyto=replyto,
                rcptto=receiver         # 收件人地址或是地址列表，支持多个收件人，最多30个
            )

            try:
                client = smtplib.SMTP()
                # client = smtplib.SMTP_SSL()
                client.connect('smtpdm.aliyun.com', 80)

                client.set_debuglevel(0)
                client.login(username, password)
                # 发件人和认证地址必须一致
                # 备注：若想取到DATA命令返回值,可参考smtplib的sendmaili封装方法:
                #      使用SMTP.mail/SMTP.rcpt/SMTP.data方法
                client.sendmail(username, receiver, message.as_string())
                client.quit()
                print '邮件成功发送至潜在客户{}, ({}/{})...！'.format(receiver, i+1, receivers_amount)
            except smtplib.SMTPConnectError, e:
                print '邮件发送至潜在客户{}失败，连接失败:'.format(receiver), e.smtp_code, e.smtp_error
            except smtplib.SMTPAuthenticationError, e:
                print '邮件发送至潜在客户{}失败，认证错误:'.format(receiver), e.smtp_code, e.smtp_error
            except smtplib.SMTPSenderRefused, e:
                print '邮件发送至潜在客户{}失败，发件人被拒绝:'.format(receiver), e.smtp_code, e.smtp_error
            except smtplib.SMTPRecipientsRefused, e:
                print '邮件发送至潜在客户{}失败，收件人被拒绝:'.format(receiver), e.smtp_code, e.smtp_error
            except smtplib.SMTPDataError, e:
                print '邮件发送至潜在客户{}失败，数据接收拒绝:'.format(receiver), e.smtp_code, e.smtp_error
            except smtplib.SMTPException, e:
                print '邮件发送至潜在客户{}失败, '.format(receiver), e.message
            except Exception, e:
                print '邮件发送至潜在客户{}异常, '.format(receiver), str(e)
        return

    @staticmethod
    def build_email_content(username, replyto, rcptto):
        """
        build email content

        :param username: 发件人地址，通过控制台创建的发件人地址
        :param replyto: 自定义的回复地址
        :param rcpto: 收件人地址或是地址列表，支持多个收件人，最多30个
        :return:
        """
        # 构建alternative结构
        message = MIMEMultipart('alternative')
        message['Subject'] = Header('工科论文代写(本科，硕士，在职研毕业论文), 联系微信 my_wind33'.decode('utf-8')).encode()
        message['From'] = '%s <%s>' % (Header('不喂大侠'.decode('utf-8')).encode(), username)
        message['To'] = rcptto
        message['Reply-to'] = replyto
        message['Message-id'] = email.utils.make_msgid()
        message['Date'] = email.utils.formatdate()

        # 构建alternative的text/html部分
        texthtml = MIMEText(AutoSender.html_content(), _subtype='html', _charset='UTF-8')
        message.attach(texthtml)

        return message


if __name__ == '__main__':
    auto_sender = AutoSender(
        source_addr_csv_file='../dataset/addrs_test.csv'
    )

    auto_sender.send()

