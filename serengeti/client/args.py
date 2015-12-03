

import argparse

class Option(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

# Default Command Line Arguments
CLI_ARGS  = [Option('-u', '--url', dest='url', help='XXX')]
CLI_ARGS += [Option('-t', '--host', dest='host', help='XXX')]
CLI_ARGS += [Option('-p', '--port', dest='port', help='XXX')]
CLI_ARGS += [Option('-s', '--https', dest='https', help='XXX')]
CLI_ARGS += [Option('-c', '--cert', dest='cert', help='XXX')]
CLI_ARGS += [Option('-k', '--key', dest='key', help='XXX')]
CLI_ARGS += [Option('--proxy', dest='proxy', help='XXX')]


def get_arg_parser(parser_description = None, arg_list=None):
    """

    """
    arg_list = arg_list or CLI_ARGS
    parser = argparse.ArgumentParser(description=parser_description)
    for option in arg_list:
        parser.add_argument(*option.args, **option.kwargs)
    return parser
