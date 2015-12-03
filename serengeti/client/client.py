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
import warnings
import glob

from . import args
from . import config
from . import service


def main(*args, **kwargs):
  """Client Entry Point"""
  parser = args.get_arg_parser()
  args = parser.parse_args()
  
  config = config.read_config()
  config.merge_args(args)
  
  request = config.get_request()
  response = service.handler(request)
  
  print(response)

if __name__ == '__main__':
  main()

