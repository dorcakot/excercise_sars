# Exercise 2: Cancer Genomics Data Analysis

This is a simple variant calling workflow for producing read-depth plots and calling structural variants:

1. Align the data to the human reference genome + sort and index the alignments:

`bwa index reference.fasta`

2. Align reads in fastq files to the reference and sort:

`bwa mem reference.fasta sample.R1.fastq sample.R2.fastq | samtools sort -o sample_aligned.bam`

3. Index the binary alignment file:

`samtools index sample_subset.bam`

4. Subset to X chromosome:

`samtools view -b sample_aligned.bam chrX:20000000-40000000 > sample_subset.bam`

5. Calculate depth using samtools:

`samtools depth sample_subset.bam > sample_subset.depth`

6. Using python package seaborn, create the read-depth ration plot:

`python3 plot.py --normal data/sample1/wt_subset.depth --tumor data/sample1/tu/tu_subset.depth`


This workflow can be run using `snakemake` and list of samples can be specified in the config file.

