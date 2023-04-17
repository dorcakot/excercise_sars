# Exercise 1: Sars-CoV-2 Lineage Determination

This is a simple variant calling workflow for SARS-CoV-2:

1. Index the reference genome:

`bwa index reference.fasta`

2. Align reads in fastq files to the reference and sort:

`bwa mem reference.fasta sample.R1.fastq sample.R2.fastq | samtools sort -o sample_aligned.bam`

3. Index the binary alignment file:

`samtools index sample_aligned.bam`

4. Variant calling using bcftools:

`bcftools mpileup -f reference.fasta sample_aligned.bam | bcftools call --ploidy 1 -mv -Ob -o sample_calls.bcf`
`bcftools index sample_calls.bcf`

5. Create consensus sequence with bcftools:

`cat reference.fasta | bcftools consensus sample_calls.bcf > sample_consensus.fa`

6. Lineage assignment done online using [Nextclade](clades.nextstrain.org) with the following results:

Dataset1 is of lineage B.1.1.7 - Alpha.

Dataset2 is of lineage BA.1.18 - Omicron.


This workflow can be run using `snakemake` and list of samples can be specified in the config file.
