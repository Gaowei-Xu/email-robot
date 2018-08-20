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
# @Time    : 2018/7/25 下午10:28
# @Author  : Gaowei Xu
# @Email   : gaowxu@hotmail.com
# @File    : qq_email_generator.py

import re


class QQEmailGenerator(object):
    """
    Email generator for QQ
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
            email_addr = qq_account[0] + '@qq.com' + ';\n'
            wh.write(email_addr)
        wh.close()


if __name__ == '__main__':

    generator = QQEmailGenerator(
        [
            './QQ/425272150.txt',
            './QQ/433487256.txt'
        ],

        './QQ_emails.csv'
    )

    generator.filter()
