# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('mystuff', 'templates'))

templ = env.get_template('index.html')
datum = templ.render(directories=['dir1', 'dir2', 'dir3'])

print datum

# with open('dunno.html', 'w+') as f:
#     f.write(datum)


def filter_for_files(directory):
    """For the given directory, take the files within it and make
    them into the html files."""

    # Get all the files, even if they are nested.


    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

    return onlyfiles

    # Iterate through them, converting them to html.

    # Write them to a new directory.

    pass
