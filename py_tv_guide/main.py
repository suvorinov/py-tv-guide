# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-05-12 16:08:49
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-07-25 10:19:49

import cmd
import argparse
import logging
from multiprocessing import Pool, current_process
from typing import Dict, List, Tuple
from collections import defaultdict
from dataclasses import dataclass, field

import yaml
from xmltv import xmltv_helpers
from xmltv.models import Channel, Programme, Tv

from py_tv_guide.epg import EPG
from py_tv_guide.sites import * # noqa
from py_utils import now

DEFAULT_POOL_SIZE = 5


class Cli(cmd.Cmd):

    """docstring for Cli
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.intro = "Добро пожаловать в TV Guide\nДля справки наберите 'help'"
        self.doc_header = "Что мы можем"
        self.undoc_header = 'Неизвестная команда'

    def do_exit(self, args):
        """exit - выход"""
        exit(0)


@dataclass(frozen=True)
class ChannelKey:
    id: str = field(compare=True, hash=True)
    channel: Channel = field(compare=False, hash=False)


class PyTvGuide(object):
    """docstring for PyTvGuide"""

    def __init__(self):
        super(PyTvGuide, self).__init__()
        self.log = logging.getLogger(__name__)
        self.args = self.__parse_args()
        self.config = self.__read_config()
        self.scrapers = self.__init_scrapers()
        pool_size = self.config.get('pool_size')
        self.pool_size = pool_size if pool_size is not None else DEFAULT_POOL_SIZE # noqa
        self.pool = Pool(self.pool_size)

    def __parse_args(self):
        parser = argparse.ArgumentParser(
            prog='tv_guide',
            description='A simple, multi-threaded, modular EPG grabber written in Python') # noqa

        parser.add_argument(
            "-p", "--progress-bar",
            help="show progress bars",
            action="store_true")

        parser.add_argument(
            "-q", "--quiet",
            help="quiet mode (no progress-bar, no console logs)",
            action="store_true")

        requiredArgs = parser.add_argument_group('required arguments')
        requiredArgs.add_argument(
            "-c", "--config", help="Path to tv_guide.yaml file", required=True)
        args = parser.parse_args()

        if args.quiet:
            args.progress_bar = False
        if args.progress_bar or args.quiet:
            # Disable console logging if progress-bar is enabled
            logging.getLogger().removeHandler(logging.getLogger().handlers[0])
        return args

    def __read_config(self) -> Dict:
        try:
            with open(self.args.config, "r") as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
            raise e
        return config

    def __init_scrapers(self) -> Dict[str, EPG]:
        _scrapers = {}
        implementations = EPG.__subclasses__()
        proxy = self.config.get('proxy')
        user_agent = self.config.get('user_agent')
        for scraper_class in implementations:
            obj = scraper_class(proxy=proxy, user_agent=user_agent)
            obj.get_epg()
            _scrapers[obj.site_name] = obj
        return _scrapers

    def __fetch_data(self) -> Dict[ChannelKey, List[Programme]]:
        pbar_id = 'All Channels'
        programs_by_channel = defaultdict(list)
        channels = self.config.get('channels')
        self.log.info(
            f'Start grabbing programs for {len(channels)} channels using {self.pool_size} workers.') # noqa

        return None

    def __fetch_channel(self, chan) -> Tuple[ChannelKey, List[Programme]]:
        return None, None

    def run(self):
        print("Run TVGuide")
        print(now())
        data = self.__fetch_data()


def main() -> None:
    # Cli().cmdloop()

    py_tv_guide = PyTvGuide()
    py_tv_guide.run()


if __name__ == '__main__':
    main()
