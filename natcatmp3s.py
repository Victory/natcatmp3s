#!/usr/bin/env python

import os
import argparse
import SimpleHTTPServer
import SocketServer

import eyed3

from natsort import natsorted
from pprint import pprint


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

    parser.add_argument(
        "-a", "--artist",
        required=True,
        help="Artist's name")

    parser.add_argument(
        "-l", "--album",
        required=True,
        help="album")

    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="debug/dry run")

    parser.add_argument(
        "-s", "--start-server",
        action="store_true",
        help="If set start simplehttpserver")

    parser.add_argument(
        "-p", "--port",
        default=8888,
        help="Port to start simplehttpserver on")

    return parser.parse_args()


def fwrite(target, source_filename):
    """write(read) wrapper"""
    print "source file:", source_filename
    if DEBUG:
        return

    source = open(source_filename, 'r')
    target.write(source.read())
    source.close()


def is_mp3(source_name):
    return source_name[-3:] == 'mp3'


def parse_dir(dirpath, target_name):
    target = open(target_name, 'w')
    if DEBUG:
        print "full target name", target_name

    files = os.listdir(dirpath)
    files = natsorted(files)
    for fl in files:
        source_name = os.path.join(dirpath, fl)
        if not is_mp3(source_name):
            return

        if source_name == target_name:
            continue
        fwrite(target, source_name)
    target.close()


def make_full_target_name(ii, dirs):
    of = str(len(dirs))
    formatstr = "{0:0" + str(len(str(of))) + "d}"
    x = str(formatstr.format(ii + 1))
    return args.target + "." + x + "of" + of + ".mp3"


def tag(target_name, args, track_num):
    a = eyed3.load(target_name)
    a.tag.artist = unicode(args.artist)
    a.tag.album = unicode(args.album)
    a.tag.track_num = track_num
    a.tag.title = u"%s - %s - %s" % (track_num, args.artist, args.album)
    a.tag.save()


def start_server(port=8888):
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", port), Handler)
    print "serving at port", port
    httpd.serve_forever()


if __name__ == '__main__':

    args = get_args()
    DEBUG = args.debug
    pprint(args)

    for ii, curdir in enumerate(args.dir):
        target_name = make_full_target_name(ii, args.dir)
        parse_dir(curdir, target_name)
        tag(target_name, args, ii + 1)

    if args.start_server:
        start_server(int(args.port))
