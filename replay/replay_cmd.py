#!/usr/bin/env python


import argparse
import logging
from file_parser import Parser

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("-f",action='append', help="infos.txt to log", required=True)
    args = p.parse_args()

    logging.basicConfig()
    logger = logging.getLogger('replay-cmd')
    logger.setLevel(logging.INFO)

    parser = Parser(logger)
    for file in args.f:
        parser.parse(file)
