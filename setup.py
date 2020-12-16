from setuptools import setup
setup(
    name = 'A8',
    version = '0.1.0',
    packages = ['chongcli'],
    entry_points = {
        'console_scripts': [
            'chongcli = chongcli.__main__:main'
        ]
    })