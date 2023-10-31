# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-05-17 16:16:30
# @Last Modified by:   suvorinov
# @Last Modified time: 2023-05-17 16:17:25

from os import listdir
from os.path import basename, dirname

__all__ = [basename(f)[:-3] for f in listdir(dirname(__file__))
           if f[-3:] == ".py" and not f.endswith("__init__.py")]
