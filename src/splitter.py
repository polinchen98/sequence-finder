import argparse
from logic import Splitter


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sequence', dest='sequence', type=str, help='Path to file with sequence', required=True)
parser.add_argument('-l', '--length', dest='length', type=int,
                    help='The length of the fragments into which input sequence will be cut', required=True)
parser.add_argument('-i', '--interval', dest='interval', type=int,
                    help='The interval at which the fragments will be cut', required=True)
parser.add_argument('-o', '--output', dest='output', type=str, default='split_sequence', help='Path to output file')

args = parser.parse_args()

Splitter(args.output, args.sequence, args.length, args.interval)
