import os
import primer3
import argparse
from Bio import SeqIO

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


if not os.path.exists(args.output):
    os.mkdir(args.output)

list_of_files = os.listdir(args.input)

sequence_index = 1

primer = {}

for file_name in list_of_files:
    path_to_file = args.input + '/' + file_name
    file = open(path_to_file, 'r')
    with open(path_to_file) as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            seq_id = record.id
            seq = str(record.seq)

        if len(seq) >= args.length:
            primer = primer3.bindings.designPrimers(
                {
                    'SEQUENCE_ID': seq_id,
                    'SEQUENCE_TEMPLATE': seq,
                },
                {
                    'PRIMER_OPT_SIZE': args.opt,
                    'PRIMER_MIN_SIZE': args.min,
                    'PRIMER_MAX_SIZE': args.max,
                    'PRIMER_OPT_TM': args.opt_tm,
                    'PRIMER_MIN_TM': args.min_tm,
                    'PRIMER_MAX_TM': args.max_tm,
                })

            with open(args.output + '/' + 'primer_' + str(sequence_index), 'w') as out:
                out.write(record.description + '\n' + '\n')
                for key, val in primer.items():

                    out.write('{}:{}\n'.format(key, val))
                sequence_index += 1



