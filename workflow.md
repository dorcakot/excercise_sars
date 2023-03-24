# Exercise 1: Sars-CoV-2 Lineage Determination

1. Index the reference genome:

`bwa index sequence.fasta`

2. Align reads in fastq files to the reference and sort:

`bwa mem sequence.fasta Plate135H10.R1.fastq Plate135H10.R2.fastq | samtools sort -o Plate135H10_aligned.bam`

3. Index the binary alignment file:

`samtools index Plate135H10_aligned.bam`

4. Variant calling using bcftools:

`bcftools mpileup -f sequence.fasta Plate135H10_aligned.bam | bcftools call --ploidy 1 -mv -Ob -o Plate135H10_calls.bcf`

5. Variant annotation done online using Ensembl Variant Effect Predictor (VEP)

6. Lineage assignment done online with the following results:

Plate135H10 - 
Plate42B2 - 
