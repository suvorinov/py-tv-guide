# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-05-11 16:09:48
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-06-07 08:55:44

import os

from py_tv_guide.logging import setup_logging

log_config = os.path.dirname(os.path.abspath(__file__)) + '/logging.yaml'
setup_logging(path=log_config)
