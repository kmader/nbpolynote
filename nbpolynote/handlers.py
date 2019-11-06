from urllib.parse import urlunparse, urlparse

from tornado import web

from notebook.base.handlers import IPythonHandler
from notebook.utils import url_path_join as ujoin

from jupyter_server_proxy.handlers import SuperviseAndProxyHandler
import yaml
import os

POLYNOTE_ROOT = os.path.dirname(os.path.abspath(__file__))


class PolynoteProxyHandler(SuperviseAndProxyHandler):
    name = "Polynote"

    def get_cmd(self):
        config_dict = {"listen": {"port": self.port, "host": "0.0.0.0"}}
        config_dict["ui"] = {"base_uri": self.proxy_base}
        with open(os.path.join(POLYNOTE_ROOT, "polynote", "config.yml"), "w") as f:
            yaml.dump(config_dict, stream=f)

        cmd = [os.path.join(POLYNOTE_ROOT, "polynote", "polynote")]
        return cmd

    def get_env(self):
        return {}

    def get_timeout(self):
        """
        Return timeout (in s) to wait before giving up on process readiness
        """
        return 30


class AddSlashHandler(IPythonHandler):
    """Handler for adding trailing slash to URLs that need them"""

    @web.authenticated
    def get(self, *args):
        src = urlparse(self.request.uri)
        dest = src._replace(path=src.path + "/")
        self.redirect(urlunparse(dest))


def setup_handlers(web_app):
    web_app.add_handlers(
        ".*",
        [
            (
                ujoin(web_app.settings["base_url"], "polynote/(.*)"),
                PolynoteProxyHandler,
                dict(state={"port": 8192}),
            ),
            (ujoin(web_app.settings["base_url"], "polynote"), AddSlashHandler),
        ],
    )
