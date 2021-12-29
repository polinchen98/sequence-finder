#!/usr/bin/env python
import argparse
from .logic import GenomeMapping


def mapping_genome():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', type=str, help='path to input file', required=True)
    parser.add_argument('--output', dest='output', type=str, default='output', help='path to output folder')
    args = parser.parse_args()
    return args.input, args.output


input, output = mapping_genome()

GenomeMapping(input, output)
