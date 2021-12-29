from Bio import SeqIO


class Splitter:
    def __init__(self, output, sequence, length, interval):

        output_file = open(output + '.fna', 'w')

        with open(sequence) as handle:
            for record in SeqIO.parse(handle, "fasta"):
                for i in range(0, len(record.seq), interval):

                    id_with_interval = record.id + '_' + str(i + 1) + '-' + str(i + length + 1)
                    description = '>' + record.description.replace(record.id, id_with_interval) + '\n'

                    if i + length < len(record.seq):
                        output_file.write(description + str(record.seq[i:i + length]) + '\n')

                    else:
                        output_file.write(description + str(record.seq[-length:]))
                        break
