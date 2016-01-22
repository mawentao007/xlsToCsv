#coding:utf-8
__author__ = 'marvin'

import re

sample = u'I am from 美国。We should be friends. 朋友。'
print(sample)
for n in re.findall(r'[\u4e00-\u9fff]+',sample):
    print(n)