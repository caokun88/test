# coding=utf8

import datetime

DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_FORMAT = '%Y-%m-%d'


def date_to_age(birthday):
    """
    由出生日期导出年龄
    :param birthday: 出生日期
    :return: 年龄
    """
    now = datetime.date.today()
    age = now.year - birthday.year
    return age


def age_to_date(age):
    """
    又年龄推算出生日
    :param age:
    :return:
    """
    now = datetime.date.today()
    birthday = datetime.date(now.year - int(age), 1, 1)
    return birthday


def min_max(x, min_num, max_num):
    """
    min-max 标准化
    :param x: 数值
    :param min_num: 最小数
    :param max_num: 最大数
    :return: 系数
    """
    coefficient = (x - min_num) / float(max_num - min_num)
    return coefficient