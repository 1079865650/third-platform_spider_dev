# _*_ coding : utf-8 _*_
# @Time : 2023-01-19 11:45
# @Author : wws
# @File : test
# @Project : third-platform_spider_text
import datetime

from db_utils import get_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from parse_utils import *
from datetime import datetime


@staticmethod
def get_href(string):
    return str(string).split('id=')[1]


if __name__ == '__main__':
    print('')


