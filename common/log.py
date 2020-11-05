"""
    author: hf     by 2020-10-27
"""
import logging, os, time, datetime
from os import path

path = os.path.dirname(path.dirname(__file__)) + '\logs/'


class Logger:
    def __init__(self, name='', path=path, level='DEBUG', comdlevel="DEBUG", Flevel="DEBUG"):
        # 这里为了简便，同时处理：输出控制台和保存到文件中
        # 第一步，创建一个logger
        # 设置输出的等级
        LEVELS = {'NOSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)  # Log等级总开关

        # 第二步，创建一个handler，用于写入日志文件
        logfile = '{}/{}{}.log'.format(path, datetime.datetime.now().strftime('%Y%m%d'), name)
        fh = logging.FileHandler(logfile, mode='a')  # open的打开模式这里可以进行参考
        fh.setLevel(LEVELS.get(Flevel))  # 输出到file的log等级的开关

        # 第三步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(LEVELS.get(comdlevel))  # 输出到console的log等级的开关

        # 第四步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 第五步，将logger添加到handler里面
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def info(self, message):
        # info信息
        self.logger.info(message)

    def debug(self, message):
        # debug信息
        self.logger.debug(message)

    def warning(self, message):
        # 警告信息
        self.logger.warning(message)

    def error(self, message):
        # 错误信息
        self.logger.error(message)

    def critical(self, message):
        # 危急信息
        self.logger.critical(message)
