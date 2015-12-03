#!/usr/bin/env python
#
# Copyright 2016 Steve Kyle. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
Configure Serengeti TAXII Client
"""
from __future__ import print_function
import sys
import os
from collections import OrderedDict
from ConfigParser import ConfigParser as _ConfigParser

CONF_FILE = '.serengeti.client'

CONF_OPTIONS = {'CLIENT': { 'cert':None,
                            'cert_key': None,
                            'ca':None,
                            },
                            
                'TAXII':  { 'discovery':None,
                            'poll': None,
                            'inbox':None,
                            'collection': None,
                            'channels':None,                            
                            },
                }


class ConfigParser(_ConfigParser):

    # modified to accept file names as input
    def write(self, fp):
        """Write an .ini-format representation of the configuration state."""
        if isinstance(fp, file):
            _ConfigParser.write(self, fp)
        elif isinstance(fp, basestring):
            with open(fp, 'wb') as fpp:
                _ConfigParser.write(self, fpp)
        else:
            raise TypeError('fp must be of type file or basestring')

    def to_dict(self):
        """Export ConfigParser Object to OrderedDict"""
        d = OrderedDict.fromkeys(self.sections())
        for section in d.keys():
            d[section] = dict(self.items(section))
        return d

    @staticmethod
    def from_dict(d):
        """Import Dict to create new ConfigParser Object"""
        c = ConfigParser()
        for section in d.keys():
            c.add_section(section)
            for option, value in d[section].iteritems():
                c.set(section, option, value)
        return c


if os.path.exists(CONF_FILE) is False:
    cfg_file = open(CONF_FILE, 'w')
    config.add_section('USER')
    config.set('USER','cert','')
    config.set('USER','key','')
    config.set('USER','ca','')
    config.set('USER','ua','')

    config.add_section('TAXII')
    config.set('TAXII','host','')
    config.set('TAXII','poll','')
    config.set('TAXII','disc','')

    config.write(cfg_file)
    cfg_file.close()

config.read(CONF_FILE)
