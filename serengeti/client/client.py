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
Serengeti TAXII Client Script
"""
import sys
import os

from datetime import datetime
import libtaxii.messages_11 as tm11
from urlparse import urljoin
from OpenSSL import crypto
import argparse
import threading
import readline
import rlcompleter
import glob
import warnings

from requests.exceptions import SSLError
from requests import Request, Session
from requests.auth import AuthBase
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from libtaxii.constants import VID_TAXII_SERVICES_11
from libtaxii.constants import VID_TAXII_HTTPS_10
from libtaxii.constants import VID_TAXII_XML_11
import libtaxii.taxii_default_query as tdq
import libtaxii
from lxml import etree
from ConfigParser import ConfigParser
import os
import atexit


