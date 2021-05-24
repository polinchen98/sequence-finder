# Sequence finder

Light and fast Python pipeline for searching species-specific regions in bacterial genomes.


### Requirements

You need have installed:
- [bioconda](https://bioconda.github.io/user/install.html)
- Blast - `conda install -c bioconda blast`

### Installation

Clone repo

`git clone https://github.com/polinchen98/sequence-finder.git`

Install packages

`pip install -r requirements.txt`

If this fails on older versions of Python, try updating your `pip` tool first:

`pip install --upgrade pip`

### Usage

`prepare.py` - downloading and creating databases(positive and negative)

`python prepare.py --genus pectobacterium --species parmentieri --id CP015749.1`

---

`splitter.py` - split sequence with a specified interval and length

`python splitter.py --sequence path/to/input/file.fna --length 100 --interval 10 --output path/to/output/file`

`--length` (-l): length of fragment (e.g 100)

`--interval` (-i): step (e.g 10)

---

`blast.py` - compares splitted genome with the selected database and creates two files: `hits.fna` and `no_hits.fna`

`python blast.py --input path/to/input_file.fna --db path/to/blast_database_folder`

---

`find_of_overlapping_seq.py` - make files with overlapping sequences

`python find_of_overlapping_seq.py --input path/to/input_file.fna`
