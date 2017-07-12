import json
import urllib
import os
import jupyterhub
from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from traitlets import Unicode
from jupyterhub.auth import Authenticator
from tornado import gen

class HttpAuthenticator(Authenticator):

    server = Unicode(
        None,
        allow_none=True,
        config=True,
        help="""
          Http authentication server.
        """
    )
    
    appid = Unicode(
       None,
       allow_none=True,
       config=True,
       help="""
         Application Id recognized by the http authentication server
       """   
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        http_client = AsyncHTTPClient()

        headers = {
            "Accept": "application/json",
            "User-Agent": "JupyterHub",
        }

        params = dict(
            type="json",
            appid=self.appid,
            ac=data['username'],
            pw=data['password']
        )

        req = HTTPRequest(self.server,
                          method="POST",
                          headers=headers,
                          body=urllib.parse.urlencode(params),
                          validate_cert = False
                         )
        
        
        resp = yield http_client.fetch(req)
        reply = json.loads(resp.body.decode('utf8', 'replace'))

        if reply.get("code") == 200:
           return (reply.get("data").get("UserCN"))
        else:
           return None


