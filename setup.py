from distutils.core import setup

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: System :: Filesystems',
]

# requires
# daemon
setup(
    name = "crontub",
    version = "0.2",
    description = "A dynamic cron daemon",
    long_description = """crontub let's you specify your cron information in the files which will be croned.""",
    license = "GNU GPL v3",
    author = "Nic Ferrier",
    author_email = "nic@ferrier.me.uk",
    url = "http://github.com/nicferrier/crontub",
    download_url="http://github.com/nicferrier/crontub/downloads",
    platforms = ["any"],
    scripts = ["src/crontub"],
    classifiers =  classifiers
    )
