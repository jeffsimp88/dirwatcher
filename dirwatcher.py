#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Jeffrey Simspon"

import sys
import logging


logger = logging.getLogger(__name__)


def search_for_magic(filename, start_line, magic_string):
    """Looks for a magic string and its line provided in command."""
    logger.info(f"Looking for {magic_string}")
    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    return


def create_parser():
    # Your code here
    return


def signal_handler(sig_num, frame):
    # Your code here
    return


def main(args):
    # Your code here
    return


if __name__ == '__main__':
    main(sys.argv[1:])
