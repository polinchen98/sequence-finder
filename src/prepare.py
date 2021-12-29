#!/usr/bin/env python
import argparse
from .logic import GenomeDownloader


def make_prepare():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--genus', dest='genus', type=str, help='Bacteria genus. For example: pectobacterium',
                        required=True)
    parser.add_argument('-s', '--species', dest='species', type=str, help='Bacteria species. For example: parmentieri',
                        required=True)
    parser.add_argument('-i', '--id', dest='id', type=str, help='INSDC from NCBI', required=True)
    parser.add_argument('-o', '--output', dest='output', type=str, default='download', help='path to output folder')
    parser.add_argument('-ps', '--positive_strain', dest='positive_strain', type=str,
                        help='Strains that are misclassified in the negative database. Must be classified as a positive database.')
    parser.add_argument('-ns', '--negative_strain', dest='negative_strain', type=str,
                        help='Strains that are misclassified in the positive database. Must be classified as a negative database.')

    args = parser.parse_args()
    return args.output, args.genus, args.species, args.id


output, genus, species, id = make_prepare()

GenomeDownloader(output, genus, species, id)
