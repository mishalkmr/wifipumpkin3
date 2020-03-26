import re
from ast import literal_eval 
from wifipumpkin3.plugins.captivePortal.plugin import CaptiveTemplatePlugin
import wifipumpkin3.core.utility.constants as C
"""
Description:
    This program is a core for wifi-pumpkin.py. file which includes functionality
    plugins for Pumpkin-Proxy.

Copyright:
    Copyright (C) 2015-2016 Marcos Nesster P0cl4bs Team
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
"""


class Loginv4(CaptiveTemplatePlugin):
    meta = {
        'Name'      : 'Login_v4',
        'Version'   : '1.0',
        'Description' : 'Example is a simple portal default page',
        'Author'    : 'Pumpkin-Dev',
        'Language' : 'En',
        'TemplatePath' : C.TEMPLATES_FLASK + 'templates/Login_v4',
        'StaticPath' : C.TEMPLATES_FLASK + 'templates/Login_v4/static',
        'Preview' : 'plugins/captivePortal/templates/Login_v4/preview.png'
    }

    def __init__(self):
        for key,value in self.meta.items():
            self.__dict__[key] = value
        self.dict_domain = {}
        self.ConfigParser = False