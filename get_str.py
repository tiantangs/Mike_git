# # !/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import time
import os
import sys
import csv
import json
import codecs
import pymysql as ps
from pandas import DataFrame as df
import pandas as pd
current_folder = os.getcwd()            # 当前工作目录
up_level_folder = os.path.dirname(current_folder)               # 当前工作目录的上层目录
current_file_name = os.path.basename(__file__).split('.')[0]    # 当前文件名
sys.path.append(current_folder)         # 添加当前目录到系统路径
sys.path.append(up_level_folder)
import _Server.Module_log as log        # 自定义日志函数
today = log.today                       # 当前日期
get_logger = log.logger(__name__, current_file_name)  # 实例化日志对象