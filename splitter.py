file_name = input('file_sequence: ')
file = open(file_name)

length_sequence = int(input('Length sequence: '))
interval = int(input('Interval: '))

sequence_name = ''
sequence = ''

is_first_line = True
for line in file:
    if not is_first_line:
        sequence += line.replace('\n', '')
    else:
        sequence_name = line
        is_first_line = False

output = open('split_sequence.fna', 'w')


def prepare_sequence_name(name, start_index, length):
    insert_interval = '_' + str(start_index) + '-' + str(start_index + length)
    index_of_space = name.find(' ')
    result_name = name[:index_of_space] + insert_interval + name[index_of_space:]
    return result_name


for i in range(0, len(sequence), interval):
    prepared_name = prepare_sequence_name(sequence_name, i + 1, length_sequence - 1)
    if i + length_sequence < len(sequence):
        output.write(prepared_name + sequence[i:i + length_sequence] + '\n')
    else:
        output.write(prepared_name + sequence[-length_sequence:])
        break
