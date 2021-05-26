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
def get_interval_start(record_id):
    interval = re.search(r'\d*-\d*', record_id).group(0)
    interval_start = re.search(r'\d*', interval).group(0)
    return int(interval_start)


# function, that find end of interval
def get_interval_end(record_id):
    interval = re.search(r'\d*-\d*', record_id).group(0)
    interval_end = re.findall(r'\d*\w', interval)[1]
    return int(interval_end)


def concat_records(first_record, second_record):
    step = get_interval_start(second_record.id) - get_interval_start(first_record.id)
    result_seq = first_record.seq[:step] + second_record.seq
    result_id = first_record.id.replace(str(get_interval_end(first_record.id)), str(get_interval_end(second_record.id)))
    result_description = first_record.description.replace(first_record.id, result_id)
    return SeqIO.SeqRecord(result_seq, result_id, result_id, result_description)


dict_of_records = {}

with open(args.input) as handle:
    for i, record in enumerate(SeqIO.parse(handle, "fasta")):
        dict_of_records[get_interval_start(record.id)] = record

    list_key = list(dict_of_records.keys())
    list_key.sort()

    current_record = None
    is_end_of_match = False

    for i, key in enumerate(list_key):
        if i < len(list_key) - 1 and list_key[i + 1] < get_interval_end(dict_of_records[list_key[i]].id):
            if not current_record:
                current_record = dict_of_records[key]
            else:
                current_record = concat_records(current_record, dict_of_records[key])
            is_end_of_match = True
        else:
            if is_end_of_match:
                current_record = concat_records(current_record, dict_of_records[key])
                file_name = args.output + '/' + 'file_' + str(get_interval_start(current_record.id)) + '_' + str(
                    get_interval_end(current_record.id))
                file = open(file_name, 'w')
                file.write(current_record.description + '\n' + str(current_record.seq) + '\n')
                is_end_of_match = False
                current_record = None
