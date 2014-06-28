#!/usr/bin/env python

import os

import argparse

from natsort import natsorted
from pprint import pprint

DEBUG = True

if DEBUG:
    print "running in 'dry run' mode"

DIR_NAME = 'test-audio'
OUT_NAME = 'test-audio.mp3'
FULL_NAME = os.path.join(DIR_NAME, OUT_NAME)
print "writing to:", FULL_NAME

files = os.listdir('test-audio')
files = natsorted(files)


def get_args():
    parser = argparse.ArgumentParser(
        description='Concat mp3 files and add id3 tags')

    parser.add_argument(
        "dir", nargs='*',
        help="name of directory",
        default=['.'])

    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target Prefix")

    return parser.parse_args()


def fwrite(target, source_filename):
    """write(read) wrapper"""
    print "source file:", source_filename
    if DEBUG:
        return

    source = open(cur_name, 'r')
    target.write(source.read())
    source.close()

def parse_dir(dirpath, target):
    for fl in files:
        source_name = os.path.join(dirpath, fl)
        if source_name == FULL_NAME:
            continue
        fwrite(target, source_name)


def make_full_target_name(args):
    return args.target + ".mp3"

args = get_args()
pprint(args)
target = open(make_full_target_name(args), 'w')
parse_dir(DIR_NAME, target)
target.close()
