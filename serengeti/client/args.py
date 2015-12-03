    def get_arg_parser(self,
                       parser_description,
                       path="/services/discovery/",
                       host="taxiitest.mitre.org",
                       port="80",
                       https=False,
                       cert=None,
                       key=None,
                       username=None,
                       password=None,
                       proxy='noproxy',
                       xml_output=False):
        """
        Parser things common to all scripts. Parsers for specific TAXII Services should
        add their own arguments.
        """
        parser = argparse.ArgumentParser(description=parser_description)
        url = "https" if https else "http" + "://" + host + ":" + str(port) + path
        parser.add_argument("-u",
                            "--url",
                            dest="url",
                            default=url,
                            help="The URL to connect to. Defaults to %s." % url)
        parser.add_argument("--host",
                            dest="host",
                            default=host,
                            help=argparse.SUPPRESS
                            )
        parser.add_argument("--port",
                            dest="port",
                            default=port,
                            type=int,
                            help=argparse.SUPPRESS)
        parser.add_argument("--path",
                            dest="path",
                            default=path,
                            help=argparse.SUPPRESS)
        parser.add_argument("--https",
                            dest="https",
                            default=https,
                            type=bool,
                            help=argparse.SUPPRESS)
        parser.add_argument("--cert",
                            dest="cert",
                            default=cert,
                            help="The file location of the certificate to use. Defaults to %s." % cert)
        parser.add_argument("--key",
                            dest="key",
                            default=key,
                            help="The file location of the private key to use. Defaults to %s." % key)
        parser.add_argument("--username",
                            dest="username",
                            default=username,
                            help="The username to authenticate with. Defaults to %s." % username)
        parser.add_argument("--pass",
                            dest="password",
                            default=password,
                            help="The password to authenticate with. Defaults to %s." % password)
        parser.add_argument("--proxy",
                            dest="proxy",
                            action=ProxyAction, default=proxy,
                            help="The proxy to use (e.g., http://myproxy.example.com:80/), or 'noproxy' to not use "
                                 "any proxy. If omitted, the system's proxy settings will be used.")
        parser.add_argument("--xml-output",
                            dest="xml_output",
                            action='store_true',
                            default=xml_output,
                            help="If present, the raw XML of the response will be printed to standard out. "
                                 "Otherwise, a \"Rich\" output will be presented.")

        return parser
