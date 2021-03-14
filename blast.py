from Bio.Blast.Applications import NcbiblastnCommandline
from Bio import SeqIO
from Bio.Blast import NCBIXML
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', dest='input', type=str, help='path to input file', required=True)
parser.add_argument('--db', dest='db', type=str, help='path to blast database', required=True)
parser.add_argument('--output', dest='output', type=str, default='blast_result', help='path to output folder')
parser.add_argument('--format', dest='format', default='fasta', type=str, help='format of input file')
args = parser.parse_args()

sequence_file = open(args.input, 'r')
sequence_lines = sequence_file.readlines()
records = SeqIO.to_dict(SeqIO.parse(args.input, args.format))

# Count of sequences in file for blast
sequences_per_chunk = 1000
line_per_sequence = int(len(sequence_lines) / len(records))

if not os.path.exists(args.output):
    os.mkdir(args.output)

# Results files 'hits' and 'no_hits'
hits_file = open(args.output + '/' + 'hits.fna', 'w')
no_hits_file = open(args.output + '/' + 'no_hits.fna', 'w')


# Function that spares a array into subarrays
def split_list(array, length):
    return [array[i:i + length] for i in range(0, len(array), length)]


# Array of string (1000 sequences + 1000 names)
chunks = split_list(sequence_lines, sequences_per_chunk * line_per_sequence)
chunk_name = 'chunk.fna'
chunk_result_file_name = 'chunk_result.xml'

# For statistics
records_count = 0
no_hits_count = 0
hits_count = 0

# loop through subarrays of 1000 sequences
# a temporary file is created to which the current 1000 sequences are written
for i, chunk in enumerate(chunks):
    chunk_file = open(chunk_name, 'w')
    text = ''.join(chunk)
    chunk_file.write(text)

    # creates a temporary file for output, which is overwritten each time
    blastn_cline = NcbiblastnCommandline(task='megablast', query=chunk_name, db=args.db,
                                         outfmt=5, out=chunk_result_file_name, num_threads=4)
    stdout, stderr = blastn_cline()

    # algorithm for finding hits and non-hits from each 1000 sequences
    q_dict = SeqIO.index(chunk_name, 'fasta')

    hits = []
    for record in NCBIXML.parse(open(chunk_result_file_name)):

        if record.alignments:
            hits.append(record.query.split()[0])

    no_hits = set(q_dict.keys()) - set(hits)
    orphan_records = [q_dict[name] for name in no_hits]

    # for checking the algorithm
    records_count += len(q_dict)
    hits_count += len(hits)
    no_hits_count += len(no_hits)

    for hit in hits:
        hits_file.write(q_dict[hit].format('fasta'))

    for no_hit in no_hits:
        no_hits_file.write(q_dict[no_hit].format('fasta'))

    chunk_file.close()

    print(i + 1, ' from ', len(chunks), ':',
          "found %i records in query, %i have hits, making %i no hits" % (records_count, hits_count, no_hits_count))


os.remove(chunk_name)
os.remove(chunk_result_file_name)

print('Complete!')
