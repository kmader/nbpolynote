import setuptools

setuptools.setup(
    name="nbpolynote",
    version="0.0.1",
    url="https://github.com/kmader/nbpolynote",
    author="Kevin Mader",
    description="Jupyter extension to proxy Polynote sessions in jupyter",
    packages=setuptools.find_packages(),
    keywords=["Jupyter"],
    classifiers=["Framework :: Jupyter"],
    install_requires=["notebook", "jupyter_server_proxy >= 0.3.2"],
    package_data={"nbpolynote": ["static/*", "polynote/**"]},
)
