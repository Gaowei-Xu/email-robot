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
# @Time    : 2018/7/19 下午4:59
# @Author  : Gaowei Xu
# @Email   : gaowxu@hotmail.com
# @File    : generate_email.py


class GenerateEmail(object):
    def __init__(self):
        pass

    def hhu_benke(self):
        pass

    def hhu_yanjiusheng(self):
        emails = list()
        classes = self.continuous_nums(0, 10)
        stu_id = self.continuous_nums(0, 60)
        for class_num in classes:
            for id in stu_id:
                email = '161306' + class_num + '00' + id + '@hhu.edu.cn;'
                emails.append(email)
        return emails

    def njupt_yanjiusheng(self):
        emails = list()
        classes = self.continuous_nums(0, 10)
        stu_id = self.continuous_nums(0, 60)
        prefixs = ['201605', '101605', '121605']

        for prefix in prefixs:
            for class_num in classes:
                for id in stu_id:
                    email = prefix + class_num + id + '@njupt.edu.cn;'
                    emails.append(email)
        return emails


    @staticmethod
    def continuous_nums(min, max):
        data_list = list()
        for i in range(min, max):
            if i < 10:
                data = '0' + str(i)

            if i < 100 and i >= 10:
                data = str(i)

            data_list.append(data)

        return data_list


if __name__ == '__main__':
    generator = GenerateEmail()
    emails = generator.njupt_yanjiusheng()
    for email in emails:
        print email




















