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
import re


class EmailAddrGen(object):
    """
    A class for email address generator
    """
    def __init__(self, dataset_paths, output_csv_path):
        self._dataset_paths = dataset_paths
        self._output_csv_path = output_csv_path

    def filter(self):
        for dataset_path in self._dataset_paths:
            fh = open(dataset_path, 'rb')
            lines = fh.readlines()
            qq_accounts = list()
            for line in lines:
                line = line.strip()
                qq_account, exist = self.search_qq_num(line)
                if exist:
                    qq_accounts.append(qq_account)
            print 'File {} has {} QQ accounts...'.format(dataset_path, len(qq_accounts))
            self.dump_email_address(qq_accounts)

    @staticmethod
    def search_qq_num(string):
        pattern = re.compile(r"\d{5,14}")
        qq_account = pattern.findall(string)
        if qq_account:
            return qq_account, True
        else:
            return "NULL", False

    def dump_email_address(self, qq_accounts):
        wh = open(self._output_csv_path, 'a+')
        for qq_account in qq_accounts:
            email_addr = qq_account[0] + '@qq.com' + '\n'
            wh.write(email_addr)
        wh.close()


if __name__ == '__main__':
    generator = EmailAddrGen(
        [
            '../dataset/raw/qun_611489361.csv',
            '../dataset/raw/seu_qq_emails.txt',
            '../dataset/raw/433487256.txt',
            '../dataset/raw/425272150.txt',

        ],

        '../dataset/addrs.csv'
    )

    generator.filter()
