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


class AutoSender(object):
    """
    auto email sender class
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
        return

    def build_email_content(self):
        """
        build email content
        :return:
        """
        return


if __name__ == '__main__':
    auto_sender = AutoSender(
        source_addr_csv_file='../dataset/addrs.csv'
    )

    print auto_sender.get_all_email_addrs()


