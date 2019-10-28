from urllib.parse import urlunparse, urlparse

from tornado import web

from notebook.base.handlers import IPythonHandler
from notebook.utils import url_path_join as ujoin

from jupyter_server_proxy.handlers import SuperviseAndProxyHandler
import yaml


class PolynoteProxyHandler(SuperviseAndProxyHandler):
    name = "Polynote"

    def get_cmd(self):

        with open("polynote/config.yml", "w") as f:
            yaml.dump({"port": self.port, "host": "0.0.0.0"}, stream=f)

        cmd = ["polynote/polynote"]
        return cmd

    def get_env(self):
        return {}


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
                DLStudioProxyHandler,
                dict(state={}),
            ),
            (ujoin(web_app.settings["base_url"], "polynote"), AddSlashHandler),
        ],
    )
