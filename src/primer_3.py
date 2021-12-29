#!/usr/bin/env python
import argparse
from .logic import PrimersMaking


def make_primers():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', type=str, help='Path to input file', required=True)
    parser.add_argument('--output', dest='output', type=str, default='file_with_primers', help='Path to output folder')
    parser.add_argument('--length', dest='length', type=int, help='The length of the sequence from which the primers will be selected')
    parser.add_argument('--opt_primer', dest='opt', type=int, help='Optimum length (in bases) of a primer. Primer3 will attempt to pick primers close to this length')
    parser.add_argument('--min_primer', dest='min', type=int, help='Minimum acceptable length of a primer. Must be greater than 0 and less than or equal to max_primer')
    parser.add_argument('--max_primer', dest='max', type=int, help='Maximum acceptable length (in bases) of a primer. Currently this parameter cannot be larger than 35')
    parser.add_argument('--opt_tm', dest='opt_tm', default=60.0, type=float, help='Optimum melting temperature (Celsius) for a primer. Default = 60.0')
    parser.add_argument('--min_tm', dest='min_tm', default=57.0, type=float, help='Minimum acceptable melting temperature (Celsius) for a primer oligo. Default = 57.0')
    parser.add_argument('--max_tm', dest='max_tm', default=63.0, type=float, help='Maximum acceptable melting temperature (Celsius) for a primer oligo. Default = 63.0')
    args = parser.parse_args()
    return args.input, args.output, args.length, args.opt, args.min, args.max, args.opt_tm, args.min_tm, args.max_tm


input, output, length, opt, min, max, opt_tm, min_tm, max_tm = make_primers()
PrimersMaking(input, output, length, opt, min, max, opt_tm, min_tm, max_tm)
