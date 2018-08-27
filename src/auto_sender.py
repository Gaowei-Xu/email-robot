#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2017, BMW Group, all rights reserved.
#
# Redistribution and use in source and other forms, with or without modification,
# are permitted only in BMW internal usage. Any other companies or third-party
# SHOULD NOT use it.
#
# This software is provided by the copyright holders and contributors "as is" and
# any express or implied warranties, including, but not limited to, the implied
# warranties of merchantability and fitness for a particular purpose are disclaimed.
# In no event shall copyright holders or contributors be liable for any direct,
# indirect, incidental, special, exemplary, or consequential damages
# (including, but not limited to, procurement of substitute goods or services;
# loss of use, data, or profits; or business interruption) however caused
# and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of
# the use of this software, even if advised of the possibility of such damage.
#
# @Time    : 18-8-20
# @Author  : Gavin.Xu
# @Email   : Gavin.Xu@bmw.com
# @Department: EG-CN-72

import random
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import string


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

    def send(self):
        """
        send emails
        :return:
        """
        host = 'smtp.163.com'
        port = 25
        sender_email_addr = 'pumandaxia@163.com'
        sender_email_pwd = 'r4t5y6u7_asdxz'

        # obtain receivers
        receivers = self.get_all_email_addrs()
        receivers_amount = len(receivers)

        # send email
        for i, receiver in enumerate(receivers):
            # server configuration and login
            server = smtplib.SMTP(host, port)
            server.starttls()
            server.login(sender_email_addr, sender_email_pwd)

            try:
                message = self.build_email_content(sender_email_addr, receiver)
                server.sendmail(sender_email_addr, receiver, message.as_string())
                print 'Sending email to customer {}, {}/{}...'.format(receiver, i + 1, receivers_amount)
            except smtplib.SMTPException as e:
                print 'Failed to send email to customer {} with exception: {}'.format(receiver, e)
            finally:
                server.close()
        return

    @staticmethod
    def build_email_content(sender_email_addr, receiver_email_addr):
        """
        build email content

        :param sender_email_addr:
        :param receiver_email_addr:
        :return:
        """
        random_string = ''
        for i in range(4096):
            random_string += ''.join(random.sample(string.ascii_letters + string.digits, 1))

        html_content = """
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
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
                我们是由复旦大学／上海交大／东南大学／中科院微电子所／浙江大学／港科大硕士，博士组成的团队，专业涵盖电子／计算机／软件工程／
                自动化／信息工程等，专业提供高质量的工科论文代写服务！我们团队成员在攻读硕士博士期间曾发表过EI/SCI文章数量超30篇之多！
                曾服务过四川大学，东南大学，北京大学，北京邮电大学，上海交通大学的同学们，均顺利毕业和在期刊发表文章！
            </p>
            <span>具体课题咨询与报价请联系微信"不喂大侠"，微信号为：my_wind33</span>
        </div>
        
        <div>
            <p style="display: none">
                {}
            </p>
        </div>
        </body>
        </html>
        """.format(random_string)
        message = MIMEText(html_content, 'html', 'utf-8')
        message['From'] = formataddr(['论文代写', sender_email_addr])
        message['To'] = receiver_email_addr
        message['Subject'] = "工科论文代写(本科，硕士，在职研毕业论文), 联系微信 my_wind33"

        return message


if __name__ == '__main__':
    auto_sender = AutoSender(
        source_addr_csv_file='../dataset/addrs.csv'
    )

    auto_sender.send()


