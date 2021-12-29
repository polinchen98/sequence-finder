import os
import primer3
from Bio import SeqIO


class PrimersMaking:
    def __init__(self, input_folder, output_folder, length, opt, min, max, opt_tm, min_tm, max_tm):
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

        list_of_files = os.listdir(input_folder)

        sequence_index = 1

        primer = {}

        for file_name in list_of_files:
            path_to_file = input_folder + '/' + file_name
            file = open(path_to_file, 'r')
            with file as handle:
                for record in SeqIO.parse(handle, 'fasta'):
                    seq_id = record.id
                    seq = str(record.seq)

                if len(seq) >= length:
                    primer = primer3.bindings.designPrimers(
                        {
                            'SEQUENCE_ID': seq_id,
                            'SEQUENCE_TEMPLATE': seq,
                        },
                        {
                            'PRIMER_OPT_SIZE': opt,
                            'PRIMER_MIN_SIZE': min,
                            'PRIMER_MAX_SIZE': max,
                            'PRIMER_OPT_TM': opt_tm,
                            'PRIMER_MIN_TM': min_tm,
                            'PRIMER_MAX_TM': max_tm,
                        })

                    with open(output_folder + '/' + 'primer_' + str(sequence_index), 'w') as out:
                        out.write(record.description + '\n' + '\n')
                        for key, val in primer.items():

                            out.write('{}:{}\n'.format(key, val))
                        sequence_index += 1
