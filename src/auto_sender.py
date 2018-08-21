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


class AutoSender(object):
    """
    auto email sender class
    Reference: http://www.runoob.com/python/python-email.html
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
        sender_email_pwd = 'y6u7i8o912123x'

        # server configuration and login
        server = smtplib.SMTP(host, port)
        server.starttls()
        server.login(sender_email_addr, sender_email_pwd)

        # obtain receivers
        receivers = self.get_all_email_addrs()
        receivers_amount = len(receivers)

        # send email
        for i, receiver in enumerate(receivers):
            try:
                message = self.build_email_content(sender_email_addr, receiver)
                server.sendmail(sender_email_addr, receiver, message.as_string())
                print 'Sending email to customer {}, {}/{}...'.format(receiver, i + 1, receivers_amount)
            except smtplib.SMTPException as e:
                print 'Failed to send with exception: {}'.format(e)
        return

    @staticmethod
    def build_email_content(sender_email_addr, receiver_email_addr):
        """
        build email content

        :param sender_email_addr:
        :param receiver_email_addr:
        :return:
        """
        html_content = """
        <h2>CHINA</h2>
        <p>I am Chinese</p>
        """
        message = MIMEText(html_content, 'html', 'utf-8')
        message['From'] = formataddr(['不喂大侠', sender_email_addr])
        message['To'] = formataddr([receiver_email_addr])
        message['Subject'] = "邮件测试"

        return message


if __name__ == '__main__':
    auto_sender = AutoSender(
        source_addr_csv_file='../dataset/addrs.csv'
    )

    auto_sender.send()


