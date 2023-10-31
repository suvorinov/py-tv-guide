# -*- coding: utf-8 -*-
# @Author: Oleg Suvorinov
# @Date:   2023-06-06 15:17:25
# @Last Modified by:   Oleg Suvorinov
# @Last Modified time: 2023-06-07 08:28:31

from py_tv_guide.sites.programtv_ru import ProgramTV_RU


programtv_ru = ProgramTV_RU()
print(programtv_ru.site_name)
print(programtv_ru.site_id)
print(programtv_ru.channels())
