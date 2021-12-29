#!/usr/bin/env python
import argparse
from .logic import Blast


def run_blast():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', type=str, help='Path to input file', required=True)
    parser.add_argument('--db', dest='db', type=str, help='Path to blast database', required=True)
    parser.add_argument('--output', dest='output', type=str, default='blast_result', help='Path to output folder')
    parser.add_argument('--format', dest='format', default='fasta', type=str, help='Format of input file')
    parser.add_argument('--evalue', dest='evalue', default=10, type=int,
                        help='The BLAST E-value is the number of expected hits of similar quality (score) that could be found just by chance. ')
    parser.add_argument('--num_threads', dest='num_threads', type=int,
                        help='Number of threads (CPUs) to use in blast search')
    parser.add_argument('--task', dest='task', default='blastn', type=str,
                        help='Four different tasks are supported: 1) “megablast”, for very similar sequences (e.g, sequencing errors), 2) “dc-megablast”, typically used for inter-species comparisons, 3) “blastn”, the traditional program used for inter-species comparisons, 4) “blastn-short”, optimized for sequences less than 30 nucleotides.')

    args = parser.parse_args()
    return args.input, args.db, args.output, args.format, args.evalue, args.num_threads, args.task


input, db, output, format, e_value, num_threads, task = run_blast()

Blast(input, db, output, format, e_value, num_threads, task)
