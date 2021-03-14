import argparse
import os
import subprocess
from Bio import SeqIO
import requests
import glob

parser = argparse.ArgumentParser()
parser.add_argument('-g','--genus', dest='genus', type=str, help='Bacteria genus. For example: pectobacterium', required=True)
parser.add_argument('-s','--species', dest='species', type=str, help='Bacteria species. For example: parmentieri', required=True)
parser.add_argument('-i','--id', dest='id', type=str, help='INSDC from NCBI', required=True)
parser.add_argument('-o','--output', dest='output', type=str, default='download', help='path to output folder')
args = parser.parse_args()

# Make folder for algorithm
if not os.path.exists(args.output):
    os.mkdir(args.output)

ncbi_target_output_folder = args.output + '/' + args.genus + '_' + args.species

print('Downloading all genomes of target species')

ncbi_download_target_species = ['ncbi-genome-download', '--section', 'genbank', '--formats', 'fasta', '--genera', args.genus + ' ' + args.species, 'bacteria',
                 '--output-folder', ncbi_target_output_folder, '--flat-output']

subprocess.call(ncbi_download_target_species)


list_of_gz_files = os.listdir(ncbi_target_output_folder)

type_strain_folder = args.output + '/' + 'type_strain'
if not os.path.exists(type_strain_folder):
    os.mkdir(type_strain_folder)

print('Unzipping files')
unzip_command = ['gunzip', '-r', ncbi_target_output_folder]
subprocess.call(unzip_command)

list_of_unzip_files = os.listdir(ncbi_target_output_folder)

for file_name in list_of_unzip_files:
    path_to_file = ncbi_target_output_folder + '/' + file_name

    # Transfer of the file wite genome of type strain in other folder
    records = SeqIO.parse(path_to_file, 'fasta')
    for record in records:
        if record.id == args.id:
            os.rename(path_to_file, type_strain_folder + '/' + file_name)


print('Making POSITIVE data base')

list_of_target_species_files = os.listdir(ncbi_target_output_folder)
database_folder = args.output + '/database_' + args.species

if not os.path.exists(database_folder):
    os.mkdir(database_folder)

files = ' '.join(glob.glob(ncbi_target_output_folder + "/*.fna"))
path_to_database = database_folder + '/' + args.species
make_db = ['makeblastdb', '-in', files, '-out', path_to_database, '-title', args.species, '-dbtype', 'nucl', '-parse_seqids']
subprocess.call(make_db)


print('Getting genus info by API NCBI')

genus_info = requests.get('https://api.ncbi.nlm.nih.gov/datasets/v1alpha/genome/taxon/' + args.genus + '/tree')

others_list = []
for species in genus_info.json()['children']:
    others_list.append(species['sci_name'].lower())
others_list.remove(args.genus.lower() + ' ' + args.species.lower())


print('Downloading all genomes of others species for target genus')

ncbi_others_output_folder = args.output + '/' + 'others'
ncbi_download_others_species = ['ncbi-genome-download', '--section', 'genbank', '--formats', 'fasta', '--genera', ','.join(others_list), 'bacteria',
                 '--output-folder', ncbi_others_output_folder, '--flat-output']
subprocess.call(ncbi_download_others_species)

print('Unzipping files')

unzip_command = ['gunzip', '-r', ncbi_others_output_folder]
subprocess.call(unzip_command)

print('Making NEGATIVE data base')

list_of_others_species_files = os.listdir(ncbi_others_output_folder)
database_folder = args.output + '/database_others'

if not os.path.exists(database_folder):
    os.mkdir(database_folder)

files = ' '.join(glob.glob(ncbi_others_output_folder + "/*.fna"))
path_to_database = database_folder + '/others'
make_db = ['makeblastdb', '-in', files, '-out', path_to_database, '-title', 'others_species', '-dbtype', 'nucl', '-parse_seqids']
subprocess.call(make_db)

print('Complete!')
