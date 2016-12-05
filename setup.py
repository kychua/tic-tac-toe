try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tic Tac Toe',
    'author': 'author',
    'url': 'URL to get it at',
    'download_url': 'where to download it',
    'author_email': 'my email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['tictactoe'],
    'scripts': [],
    'name': 'Tic Tac Toe'
}


setup(**config)
