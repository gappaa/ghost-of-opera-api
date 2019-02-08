#!/usr/bin/env python


from clear.clear_function import clear_directories
import argparse
import logging


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", action='append', help="directories to clean", required=True)
    parser.add_argument("-f", action='append', help="files to clean", required=True)
    args = parser.parse_args()
    logging.basicConfig()
    logger = logging.getLogger('clear-file-cmd')
    logger.setLevel(logging.INFO)
    clear_directories(args.d, args.f, logger)

