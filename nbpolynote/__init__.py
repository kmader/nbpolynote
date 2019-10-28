from nbpolynote.handlers import setup_handlers


# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{"module": "nbpolynote"}]


def _jupyter_nbextension_paths():
    return [
        {
            "section": "tree",
            "dest": "nbpolynote",
            "src": "static",
            "require": "nbpolynote/tree",
        }
    ]


def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
