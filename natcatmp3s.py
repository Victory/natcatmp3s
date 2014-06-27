#!/usr/bin/env python

import os

from natsort import natsorted

DEBUG=True

if DEBUG:
    print "running in 'dry run' mode"

DIR_NAME = 'test-audio'
OUT_NAME = 'test-audio.mp3'
FULL_NAME = os.path.join(DIR_NAME, OUT_NAME)
print "writing to:", FULL_NAME

files = os.listdir('test-audio')
files = natsorted(files)

def fwrite(target, source_filename):
    """write(read) wrapper"""
    print "source file:", source_filename
    if DEBUG:
        return

    source = open(cur_name, 'r')
    target.write(source.read())
    source.close()

target = open(FULL_NAME, 'w')

for fl in files:
    source_name = os.path.join(DIR_NAME, fl)
    if source_name == FULL_NAME:
        continue
    fwrite(target, source_name)

target.close()
