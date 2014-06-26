#!/usr/bin/env python

import os

from natsort import natsorted

DIR_NAME = 'test-audio'
OUT_NAME = 'test-audio.mp3'
FULL_NAME = os.path.join(DIR_NAME, OUT_NAME)
print FULL_NAME

files = os.listdir('test-audio')
files = natsorted(files)

fh = open(FULL_NAME, 'w')

for fl in files:
    cur_name = os.path.join(DIR_NAME, fl)
    if cur_name == FULL_NAME:
        continue
    single = open(cur_name, 'r')
    fh.write(single.read())
    single.close()

fh.close()
