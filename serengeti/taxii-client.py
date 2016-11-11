# -*- coding: utf-8 -*-
"""
Test Script for debugging DHS TAXII Connection.
"""
import sys
import argparse
import requests
import datetime
import random
from dateutil.tz import tzutc
import libtaxii.messages_11 as taxii_messages
from libtaxii.messages_11 import SubscriptionInformation
from libtaxii.messages_11 import ContentBlock
from libtaxii.messages_11 import RecordCount

# ====================
# Defaults
# ====================
feedname = ''
subid = ''
url_publish = ''
url_discovery = ''
url_poll = ''
cert_file = ''
key_file = ''
ca_file = ''
stix_xmlfile = ''
http_proxy = ''
https_proxy = ''

HTTP_HEADERS = {'X-TAXII-Content-Type': taxii_messages.VID_TAXII_XML_11,
                'X-TAXII-Protocol': taxii_messages.VID_TAXII_HTTPS_10,
                'X-TAXII-Services': taxii_messages.VID_TAXII_SERVICES_11,
                'Accept': 'application/xml',
                'Content-Type': 'application/xml'}

argparser = argparse.ArgumentParser()
argparser.add_argument('task', action='store', choices=(
    'poll', 'publish', 'discovery',), nargs=1)
argparser.add_argument('--url_publish', action='store',
                       default=url_publish, nargs=1)
argparser.add_argument('--url_discovery', action='store',
                       default=url_discovery)
argparser.add_argument('--url_poll', action='store', default=url_poll)
argparser.add_argument('--feedname', action='store', default=feedname)
argparser.add_argument('--subid', action='store', default=subid)
argparser.add_argument('--cert_file', action='store', default=cert_file)
argparser.add_argument('--key_file', action='store', default=key_file)
argparser.add_argument('--ca_file', action='store', default=ca_file)
argparser.add_argument('--data', type=argparse.FileType('r'))
argparser.add_argument('--stix_xmlfile', type=argparse.FileType('r'))


def generate_message_id():
    """Return 20 digit random integer as a string."""
    return str(random.getrandbits(32))


def poll(**kwargs):
    """Send Poll Request. Return Response Text"""
    url = kwargs.pop('url')
    data = kwargs.pop('data', None)
    if data is None:
        message_id = kwargs.pop('message_id', generate_message_id())
        collection_name = kwargs.pop('feedname', feedname)
        subscription_id = kwargs.pop('subid', subid)
        pr = taxii_messages.PollRequest(message_id=message_id,
                                        collection_name=collection_name,
                                        subscription_id=subscription_id)
        data = pr.to_xml()

    headers = kwargs.pop('headers', HTTP_HEADERS)
    resp = requests.post(url, headers=headers, data=data, **kwargs)
    return resp.text


def publish(**kwargs):
    """Send Inpox Message. Return Response Text"""
    url = kwargs.pop('url')
    data = kwargs.pop('data', None)
    if data is None:
        message_id = kwargs.pop('message_id', generate_message_id())
        collection_name = kwargs.pop('feedname', feedname)
        subscription_id = kwargs.pop('subid', subid)
        stix_xml = kwargs.pop('stix_xml', get_sample_stix())
        content_block = ContentBlock(taxii_messages.CB_STIX_XML_111, stix_xml)
        subscription_info = SubscriptionInformation(collection_name=collection_name,
                                                    subscription_id=subscription_id,
                                                    inclusive_end_timestamp_label=datetime.datetime.now(tzutc()))

        ib = taxii_messages.InboxMessage(message_id=message_id,
                                         extended_headers=None,
                                         subscription_information=subscription_info,
                                         record_count=RecordCount(
                                             1, partial_count=False),
                                         content_blocks=[content_block])
        data = ib.to_xml()

    headers = kwargs.pop('headers', HTTP_HEADERS)
    resp = requests.post(url, headers=headers, data=data, **kwargs)
    return resp.text


def discovery(**kwargs):
    """Send Discovery Request"""
    url = kwargs.pop('url')
    data = kwargs.pop('data', None)
    message_id = kwargs.pop('message_id', generate_message_id())
    if data is None:
        dr = taxii_messages.DiscoveryRequest(message_id=message_id)
        dr.message_id = kwargs.pop('message_id', generate_message_id())
        data = dr.to_xml()

    headers = kwargs.pop('headers', HTTP_HEADERS)
    resp = requests.post(url, headers=headers, data=data, **kwargs)
    return resp.text


run_task = {
    'poll': poll,
    'discovery': discovery,
    'publish': publish
}

if __name__ == '__main__':
    args = argparser.parse_args()
    error_msg = ''
    
    if not args.cert_file:
        error_msg += 'Please Identify the location of the client ' \
            'certificate (--cert_file <PATH/TO/CERT>)\n'
            
    if not args.key_file:
        error_msg += 'Please Identify the location of the private ' \
            'key (--key_file <PATH/TO/KEY>)\n'

    if not args.ca_file:
        error_msg += 'Please Identify the location of the CA ' \
            'bundle file (--key_file <PATH/TO/CA>)\n'

    if error_msg:
        sys.exit(error_msg)

    cert = (args.cert_file, args.key_file)
    verify = args.ca_file
    data = args.data.read() if args.data else None
    task = args.task[0]
    url = getattr(args, 'url_' + task)
    kwargs = dict(url=url, cert=cert, verify=verify, data=data)

    if args.stix_xmlfile:
        kwargs['stix_xml'] = args.stix_xmlfile.read()

    resp = run_task[task](**kwargs)
    print(resp)
