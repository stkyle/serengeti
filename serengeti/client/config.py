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

from ConfigParser import SafeConfigParser as ConfigParser
CONF_FILE = '.serengeti.client'

config = ConfigParser()
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
