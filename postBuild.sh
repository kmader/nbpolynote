jupyter serverextension enable --py jupyter_server_proxy
wget https://github.com/polynote/polynote/releases/download/0.2.8/polynote-dist.tar.gz
cd nbpolynote; tar -xvf ../polynote-dist.tar.gz; cd ..
python setup.py develop
jupyter serverextension enable  --user --py nbpolynote
jupyter nbextension     install --user --py nbpolynote
jupyter nbextension     enable  --user --py nbpolynote
