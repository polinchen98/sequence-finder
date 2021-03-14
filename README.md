# Sequence finder

Small fast Python pipeline for searching species-specific regions in bacterial genomes.


### Requirements

You need have installed:
- [bioconda](https://bioconda.github.io/user/install.html)
- Blast - `conda install -c bioconda blast`

### Installation

Clone repo

`git clone git@github.com:polinchen98/sequence-finder.git`

Install packages

`pip intall -r requirements.txt`

If this fails on older versions of Python, try updating your `pip` tool first:

`pip install --upgrade pip`

### Usage

`prepare.py` - downloading and creating databases(positive and negative)

`python prepare.py --genus pectobacterium --species parmentieri --id CP015749.1`

---

`splitter.py` - split sequence with a specified interval and length

`python splitter.py`

file_sequence: - `/path/to/file`
Length sequence: - length of fragment (e.g 100)
interval: - step (e.g 10)
---

`blast.py` - compares splitted genome with the selected database and creates two files: `hits.fna` and `no_hits.fna`

`python blast.py --input path/to/input_file.fna --db path/to/blast_database_folder`


