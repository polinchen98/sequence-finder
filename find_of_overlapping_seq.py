from Bio import SeqIO
import re
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('--input', dest='input', type=str, help='path to input file', required=True)
parser.add_argument('--output', dest='output', type=str, default='output', help='path to output folder')
args = parser.parse_args()


# make directory for result
if not os.path.exists(args.output):
    os.mkdir(args.output)


# function, that find start of interval
def get_start_interval(record_id):
    interval = re.search(r'\d*-\d*', record_id).group(0)
    interval_start = re.search(r'\d*', interval).group(0)
    return int(interval_start)


# function, that find end of interval
def get_interval_end(record_id):
    interval = re.search(r'\d*-\d*', record_id).group(0)
    interval_end = re.findall(r'\d*\w', interval)[1]
    return int(interval_end)


dict_of_records = {}

with open(args.input) as handle:
    for i, record in enumerate(SeqIO.parse(handle, "fasta")):
        dict_of_records[get_start_interval(record.id)] = record

    list_key = list(dict_of_records.keys())
    list_key.sort()

    index = 1
    file_name = 'file_'
    file = open(args.output + '/' + file_name + str(index), 'w')

    is_end_of_match = False

    for i, key in enumerate(list_key):
        description = '>' + dict_of_records[list_key[i]].description
        seq = dict_of_records[list_key[i]].seq

        if i < len(list_key)-1 and list_key[i+1] < get_interval_end(dict_of_records[list_key[i]].id):
            file.write(description + '\n' + str(seq) + '\n')
            is_end_of_match = True
        else:
            if is_end_of_match:
                is_end_of_match = False
                file.write(description + '\n' + str(seq) + '\n')
                index += 1
                file = open(args.output + '/' + file_name + str(index), 'w')
