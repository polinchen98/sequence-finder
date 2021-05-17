import argparse
import os
from Bio import SeqIO


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sequence', dest='sequence', type=str, help='Path to file with sequence', required=True)
parser.add_argument('-l', '--length', dest='length', type=int,
                    help='The length of the fragments into which input sequence will be cut', required=True)
parser.add_argument('-i', '--interval', dest='interval', type=int,
                    help='The interval at which the fragments will be cut', required=True)
parser.add_argument('-o', '--output', dest='output', type=str, default='split_sequence', help='Path to output file')
args = parser.parse_args()


if not os.path.exists(args.output):
    os.mkdir(args.output)

output = open(args.output + '.fna', 'w')

with open(args.sequence) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        for i in range(0, len(record.seq), args.interval):

            id_with_interval = record.id + '_' + str(i + 1) + '-' + str(i + args.length + 1)
            description = '>' + record.description.replace(record.id, id_with_interval) + '\n'

            if i + args.length < len(record.seq):
                output.write(description + str(record.seq[i:i + args.length]) + '\n')

            else:
                output.write(description + str(record.seq[-args.length:]))
                break
