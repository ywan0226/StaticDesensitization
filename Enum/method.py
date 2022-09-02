# encoding:utf-8
from enum import Enum


class MethodEnum(Enum):
    replace = "替换"
    invalid = "无效化"
    scrambled = "乱序"
    sea = "对称加密"
