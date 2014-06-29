#!/usr/bin/env python

import os

import argparse

from natsort import natsorted
from pprint import pprint

DEBUG = True

if DEBUG:
    print "running in 'dry run' mode"


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


def is_mp3(source_name):
    return source_name[-3:] == 'mp3'


def parse_dir(dirpath, target_name):
    target = open(target_name, 'w')
    full_target_name = os.path.join(dirpath, target_name)
    if DEBUG:
        print "full target name", full_target_name

    files = os.listdir(dirpath)
    files = natsorted(files)
    for fl in files:
        source_name = os.path.join(dirpath, fl)
        if not is_mp3(source_name):
            return

        if source_name == full_target_name:
            continue
        fwrite(target, source_name)
    target.close()


def make_full_target_name(ii, dirs):
    of = str(len(dirs))
    formatstr = "{0:0" + str(len(str(of))) + "d}"
    x = str(formatstr.format(ii+1))
    return args.target + "."  + x + "of" + of +  ".mp3"


args = get_args()
pprint(args)

for ii, curdir in enumerate(args.dir):
    target_name = make_full_target_name(ii, args.dir)
    parse_dir(curdir, target_name)
