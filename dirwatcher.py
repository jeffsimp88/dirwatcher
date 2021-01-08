#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Jeffrey Simspon"

import sys
import logging
import signal
import time
import os


logger = logging.getLogger(__name__)

exit_flag = False

line_num = 0
files = {}


def search_for_magic(filename, start_line, magic_string):
    """Looks for a magic string and its line provided in command."""
    logger.info(f"Looking for {magic_string}")
    global line_num
    with open(filename) as f:
        for line_num, line in enumerate(f):
            if line_num >= start_line:
                if magic_string in line:
                    logger.info(f"Found {magic_string} on line {line_num}")
    return line_num + 1


def file_added(file_list, extension):
    """Checks if a file is added in directory"""
    global files
    for f in file_list:
        if f.endswith(extension):
            if f not in files:
                files[f] = 0
                logger.info(f"{f} added to directory.")


def file_deleted(file_list, extension):
    """Checks if file deleted in directory."""
    global files
    for f in list(files):
        if f not in file_list:
            logger.info(f"{f} deleted from directory")
            del files[f]


def watch_directory(path, magic_string, extension, interval):
    """Watches a selected directory for any added/deleted files"""
    list_files = os.listdir(path)
    file_added(list_files, extension)
    file_deleted(list_files, extension)
    for f in files:
        path = os.path.join(path, f)
        files[f] = search_for_magic(path, files[f], magic_string)
    return


def create_parser():
    # Your code here
    return


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT.
    Other signals can be mapped here as well (SIGHUP?)
    Basically, it just sets a global flag,
    and main() will exit its loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    # log the associated signal name
    logger.warn('Received ' + signal.Signals(sig_num).name)
    global exit_flag
    exit_flag = True


def main(args):
    # Hook into these two signals from the OS
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.
    polling_interval = "temp variable"

    while not exit_flag:
        try:
            # call my directory watching function
            pass
        except Exception as e:
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            logger.error(e)
            pass

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start
    return


if __name__ == '__main__':
    main(sys.argv[1:])
