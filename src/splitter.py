#!/usr/bin/env python
import argparse
from .logic import Splitter


def make_split_sequence():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sequence', dest='sequence', type=str, help='Path to file with sequence', required=True)
    parser.add_argument('-l', '--length', dest='length', type=int,
                        help='The length of the fragments into which input sequence will be cut', required=True)
    parser.add_argument('-i', '--interval', dest='interval', type=int,
                        help='The interval at which the fragments will be cut', required=True)
    parser.add_argument('-o', '--output', dest='output', type=str, default='split_sequence', help='Path to output file')

    args = parser.parse_args()
    return args.output, args.sequence, args.length, args.interval


output, sequence, length, interval = make_split_sequence()

Splitter(output, sequence, length, interval)
