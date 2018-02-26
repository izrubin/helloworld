#!/usr/bin/env python

import argparse
import helloworld

def parse_command_line():
    " parses arguments for the helloworld.py funtions"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add short args
    parser.add_argument(
        "-n", "--name",
        help="optional name to say hello to",
        type=str)

    # add long args
    parser.add_argument(
        "--nextm",
        help="print the number of days until the next millenium",
        action="store_true")

    parser.add_argument(
        "--roll",
        help="print two numbers as if you rolled two 6-sided dice",
        action="store_true")

    # parse args
    args = parser.parse_args()
    return args


def main():
    "run helloworld on parsed args"
    args = parse_command_line()
    helloworld.helloworld(
        name=args.name,
        nextm=args.nextm,
        roll=args.roll)

