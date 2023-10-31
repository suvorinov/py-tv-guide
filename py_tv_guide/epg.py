# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-05-13 18:42:10
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-07-22 09:53:46

import logging
from abc import ABC, abstractmethod
from datetime import date
from typing import List

from xmltv.models import Channel, Programme


class EPG(ABC):
    """docstring for EPG"""

    def __init__(self, name: str):
        super(EPG, self).__init__()

        self.log = logging.getLogger(name)

    @property
    @abstractmethod
    def site_name(self) -> str:
        """Returns the site name of the EPG website this scraper supports""" # noqa

    @property
    @abstractmethod
    def site_id(self) -> str:
        """Returns the site id of the EPG website this scraper supports"""

    @abstractmethod
    def get_epg(self) -> object:
        """Download EPG"""

    @abstractmethod
    def channel(self, site_id, xmltv_id, name) -> Channel:
        """Returns the requested channel object."""

    @abstractmethod
    def channels(self) -> List[Channel]:
        """Returns list of channels."""

    @abstractmethod
    def programs(self,
                 channel: Channel,
                 channel_site_id: str,
                 fetch_date: date) -> List[Programme]:
        """
        Returns a list of all programs for the given channel and day.

        Notes:
            - All dates must be in local xmltv format with timezone info.
            - Stop times are automatically set from programs' start times.
            - The order of returned programs is irrelevant, they are sorted
            by channel & start time.

        Parameters:
            channel_site_id: the channel's name as present on this EPG site
            date: the day of which programs need to be fetched for

        Returns:
            List[Programme]: the fetched channel and its programmes
            for the given 'day'.
        """
