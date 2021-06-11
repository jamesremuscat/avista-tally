from setuptools import setup, find_namespace_packages

setup(
    name='avista_tally',
    use_scm_version=True,
    description='Tally client for Avista',
    author='James Muscat',
    author_email='jamesremuscat@gmail.com',
    url='https://github.com/jamesremuscat/avista-tally',
    packages=find_namespace_packages('src', exclude=["*.tests"]),
    package_dir={'': 'src'},
    long_description="""\
    Tally client for Avista networks, designed to run on a Raspberry Pi with
    Blinkt HAT.
    """,
    setup_requires=['setuptools_scm'],
    tests_require=[],
    install_requires=[
        'autobahn[serialization,twisted]'
    ],
    extras_require={
        "blinkt": ['blinkt']
    },
    entry_points={
        'console_scripts': [
            'avista-tally=avista_tally.__main__:run'
        ],
    }
)
