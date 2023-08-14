# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-05-17 16:17:57
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-06-22 17:59:58

import os
from typing import Dict

from lxml import etree as ET
from xmltv.models import (Actor, Channel, Credits, Desc, DisplayName,
                          EpisodeNum, Icon, Programme, SubTitle, Title)

from py_tv_guide.epg import EPG
from py_downloader import download


class ProgramTV_RU(EPG):
    """docstring for ProgramTV_RU"""

    def __init__(self, proxy=None, user_agent=None):
        super(ProgramTV_RU, self).__init__(name=__name__)

        self.__site_name = "programtv.ru"
        self.__site_id = "programtv.ru"
        self.__base_url = 'https://cdn.suvorinov.ru/epg/programtv.ru/programtv.xml'
        self.__data = None

    @property
    def site_name(self) -> str:
        return self.__site_name

    @property
    def site_id(self) -> str:
        return self.__site_id

    def get_epg(self) -> object:
        self.log.info("Getting EPG data...")
        try:
            _file_data = download(self.__base_url, verbose=True)
        except Exception as e:
            raise e
        else:
            return {}

    def channels(self, limit: int = 10) -> Dict:
        _channels = {
            'count': 10,
            'channels': []
        }
        print(os.path.dirname(os.path.abspath(__file__)))
        return _channels

    def fetch_channel(self, chan_site_id, name) -> Channel:
        return None
