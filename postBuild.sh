wget https://github.com/polynote/polynote/releases/download/0.2.8/polynote-dist.tar.gz
tar -xvf polynote-dist.tar.gz
jupyter serverextension enable --py jupyter_server_proxy
python setup.py develop
