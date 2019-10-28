import setuptools

setuptools.setup(
    name="nbdlstudioproxy",
    version='0.0.1',
    url="https://github.com/kmader/dlstudio-binder",
    author="Tim Head-ish",
    description="Jupyter extension to proxy DeepLearningStudio sessions",
    packages=setuptools.find_packages(),
    keywords=['Jupyter'],
    classifiers=['Framework :: Jupyter'],
    install_requires=[
        'notebook',
        'nbserverproxy >= 0.3.2'
    ],
    package_data={'nbdlstudioproxy': ['static/*']},
)
