#!/usr/bin/env python

import glob
import subprocess
import sys

from distutils.core import setup

if len(sys.argv) > 1 and sys.argv[1] == 'man':
	subprocess.Popen(
		['txt2tags -o - --target man doc/battray.t2t | grep -Ev $^ > doc/battray.1'],
		shell=True)
	exit(0)

setup(
	name = 'battray',
	version = '1.3',
	author = 'Martin Tournoij',
	author_email = 'martin@arp242.net',
	url = 'http://arp242.net/code/battray/',
	description = '',
	download_url = '',
	classifiers = '',
	platforms = '',
	license = '',
	packages = ['battray', 'battray/platforms'],
	scripts = glob.glob('bin/*'),
	data_files = [
		('share/battray', ['data/alert.wav']),
		('share/battray/icons', glob.glob('data/icons/*')),
		('man/man1', ['doc/battray.1']),
	],
)