from django.conf import settings

import xmlrpclib

class HTTPDigestTransport(xmlrpclib.SafeTransport):
    """
    Transport that uses urllib2 so that we can do Digest authentication.
    
    Based upon code at http://bytes.com/topic/python/answers/509382-solution-xml-rpc-over-proxy
    """

    def __init__(self, username, pw, realm, verbose = None, use_datetime=0):
        self.__username = username
        self.__pw = pw
        self.__realm = realm
        self.verbose = verbose
        self._use_datetime = use_datetime

    def request(self, host, handler, request_body, verbose):
        import urllib2

        url='http://'+host+handler
        if verbose or self.verbose:
            print "ProxyTransport URL: [%s]"%url

        request = urllib2.Request(url)
        request.add_data(request_body)
        # Note: 'Host' and 'Content-Length' are added automatically
        request.add_header("User-Agent", self.user_agent)
        request.add_header("Content-Type", "text/xml") # Important

        # setup digest authentication
        authhandler = urllib2.HTTPDigestAuthHandler()
        authhandler.add_password(self.__realm, url, self.__username, self.__pw)
        opener = urllib2.build_opener(authhandler)

        f=opener.open(request)
        return(self.parse_response(f))


class TracXmlRpc:
    def __init__(self):
        self.digestTransport = HTTPDigestTransport(settings.TRAC_USERNAME, settings.TRAC_PASSWORD, settings.TRAC_REALM)
        self.server = xmlrpclib.ServerProxy(settings.TRAC_URL, transport=self.digestTransport)
    
    def ticket_create(self, summary, description, attrs={}, notify=True):
        default_attrs = {
            'cc': getattr(settings, 'TRAC_DEFAULT_CC', ''),
            'keywords': getattr(settings, 'TRAC_DEFAULT_KEYWORDS', ''),
        }
        
        default_attrs.update(attrs)
        
        ticket_id = self.server.ticket.create(summary, description, default_attrs, notify)
        return ''
