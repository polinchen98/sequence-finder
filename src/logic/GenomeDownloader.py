import os
import subprocess
from Bio import SeqIO
import requests
import glob
import ncbi_genome_download as ngd


class GenomeDownloader:
    def __init__(self, output, genus, species, id):
        log = print

        # Make folder for algorithm
        if not os.path.exists(output):
            os.mkdir(output)

        ncbi_target_output_folder = output + '/' + genus + '_' + species

        log('Downloading all genomes of target species')

        ngd.download(section='genbank', genera=genus + ' ' + species, groups='bacteria', file_formats='fasta',
                     output=ncbi_target_output_folder, flat_output=True)

        type_strain_folder = output + '/' + 'type_strain'
        if not os.path.exists(type_strain_folder):
            os.mkdir(type_strain_folder)

        log('Unzipping files')

        unzip_command = ['gunzip', '-r', ncbi_target_output_folder]
        subprocess.call(unzip_command)

        list_of_unzip_files = os.listdir(ncbi_target_output_folder)

        for file_name in list_of_unzip_files:
            path_to_file = ncbi_target_output_folder + '/' + file_name

            # Transfer of the file write genome of type strain in other folder
            records = SeqIO.parse(path_to_file, 'fasta')
            for record in records:
                if record.id == id:
                    os.rename(path_to_file, type_strain_folder + '/' + file_name)

        log('Making POSITIVE data base')

        database_folder = output + '/database_' + species

        if not os.path.exists(database_folder):
            os.mkdir(database_folder)

        files = ' '.join(glob.glob(ncbi_target_output_folder + "/*.fna"))
        path_to_database = database_folder + '/' + species
        make_db = ['makeblastdb', '-in', files, '-out', path_to_database, '-title', species, '-dbtype', 'nucl',
                   '-parse_seqids']
        subprocess.call(make_db)

        log('Getting genus info by API NCBI')

        genus_info = requests.get('https://api.ncbi.nlm.nih.gov/datasets/v1alpha/genome/taxon/' + genus + '/tree')

        others_list = []
        for _species in genus_info.json()['children']:
            others_list.append(_species['sci_name'].lower())
        others_list.remove(genus.lower() + ' ' + species.lower())

        log('Downloading all genomes of others species for target genus')

        ncbi_others_output_folder = output + '/' + 'others'
        ngd.download(section='genbank', genera=','.join(others_list), groups='bacteria', file_formats='fasta',
                     output=ncbi_others_output_folder,
                     flat_output=True)

        log('Unzipping files')

        unzip_command = ['gunzip', '-r', ncbi_others_output_folder]
        subprocess.call(unzip_command)

        log('Making NEGATIVE data base')

        database_folder = output + '/database_others'

        if not os.path.exists(database_folder):
            os.mkdir(database_folder)

        files = ' '.join(glob.glob(ncbi_others_output_folder + "/*.fna"))
        path_to_database = database_folder + '/others'
        make_db = ['makeblastdb', '-in', files, '-out', path_to_database, '-title', 'others_species', '-dbtype', 'nucl',
                   '-parse_seqids']
        subprocess.call(make_db)

        log('Complete!')
