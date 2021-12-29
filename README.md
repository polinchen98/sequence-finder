[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/polinchen98/sequence-finder)
# S3Finder
## Species-Specific Sequences Finder

---

Light and fast Python pipeline for searching species-specific regions in bacterial genomes.


### Requirements

You need have installed:
- [bioconda](https://bioconda.github.io/user/install.html)
- Blast - `conda install -c bioconda blast`
- primer3 - `pip install primer3-py`
- wxPython - `pip install wxpython`
- ncbi-genome-download - `pip install ncbi-genome-download`

### Installation

#### pip install s3finder

Clone repo

`git clone https://github.com/polinchen98/sequence-finder.git`

Install packages

`pip install -r requirements.txt`

If this fails on older versions of Python, try updating your `pip` tool first:

`pip install --upgrade pip`

### CLI version

`prepare.py` - downloading and creating databases(positive and negative)

`prepare --genus pectobacterium --species parmentieri --id CP015749.1`

---

`splitter.py` - split sequence with a specified interval and length

`splitter --sequence path/to/input/file.fna --length 100 --interval 10 --output path/to/output/file`

`--length` (-l): length of fragment (e.g 100)

`--interval` (-i): step (e.g 10)

---

`blast.py` - compares splitted genome with the selected database and creates two files: `hits.fna` and `no_hits.fna`

`blast --input path/to/input_file.fna --db path/to/blast_database_folder --evalue 10.0 --num_threads 4 --task blastn`

`--task` - four different tasks are supported: 1) “megablast”, for very similar sequences (e.g, sequencing errors), 2) “dc-megablast”, typically used for inter-species comparisons, 3)
                        “blastn”, the traditional program used for inter-species comparisons, 4) “blastn-short”, optimized for sequences less than 30 nucleotides.

---

`find_of_overlapping_seq.py` - make files with overlapping sequences

`mapping --input path/to/input_file.fna`

---

`primer_3.py` - make primers with primer3

`primer --input path/to/input_file --length 150 --opt_primer 20 --min_primer 18 --max_primer 23 --opt_tm 60.0 --min_tm 57.0 --max_tm 63.0` 

`--length` - the length of the sequence from which the primers will be selected

`--opt_primer` - Optimum length (in bases) of a primer. Primer3 will attempt to pick primers close to this length

`--min_primer` - Minimum acceptable length of a primer. Must be greater than 0 and less than or equal to max_primer

`--max_primer` - Maximum acceptable length (in bases) of a primer. Currently this parameter cannot be larger than 35

`--opt_tm` - Optimum melting temperature (Celsius) for a primer. Default = 60.0

`--min_tm` - Minimum acceptable melting temperature (Celsius) for a primer oligo. Default = 57.0

`--max_tm` - Maximum acceptable melting temperature (Celsius) for a primer oligo. Default = 63.0

---

### GUI version

`start-gui` - this command run gui version of programm
