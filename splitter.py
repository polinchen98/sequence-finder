import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sequence', dest='sequence', type=str, help='Path to file with sequence', required=True)
parser.add_argument('-l', '--length', dest='length', type=int,
                    help='The length of the fragments into which input sequence will be cut', required=True)
parser.add_argument('-i', '--interval', dest='interval', type=int,
                    help='The interval at which the fragments will be cut', required=True)
parser.add_argument('-o', '--output', dest='output', type=str, default='split_sequence', help='Path to output file')
args = parser.parse_args()

file = open(args.sequence)

sequence_name = ''
sequence = ''

is_first_line = True
for line in file:
    if not is_first_line:
        sequence += line.replace('\n', '')
    else:
        sequence_name = line
        is_first_line = False


if not os.path.exists(args.output):
    os.mkdir(args.output)

output = open(args.output + '.fna', 'w')


def prepare_sequence_name(name, start_index, length):
    insert_interval = '_' + str(start_index) + '-' + str(start_index + length)
    index_of_space = name.find(' ')
    result_name = name[:index_of_space] + insert_interval + name[index_of_space:]
    return result_name


for i in range(0, len(sequence), args.interval):
    prepared_name = prepare_sequence_name(sequence_name, i + 1, args.length - 1)

    if i + args.length < len(sequence):
        output.write(prepared_name + sequence[i:i + args.length] + '\n')
    else:
        output.write(prepared_name + sequence[-args.length:])
        break
