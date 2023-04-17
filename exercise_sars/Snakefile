configfile: "config.json"

rule all:
    input:
        expand("data/{sample}/{sample}_consensus.fa", sample=config["samples"])

rule bwa_index_ref:
    input:
        "data/reference/reference.fasta"
    output:
        "data/reference/reference.fasta.bwt"
    shell:
        "bwa index {input}"

rule align_sort_samples:
    input:
        ref="data/reference/reference.fasta",
        ref_index="data/reference/reference.fasta.bwt",
        r1="data/{sample}/{sample}.R1.fastq.gz",
        r2="data/{sample}/{sample}.R2.fastq.gz"
    output:
        "data/{sample}/{sample}_aligned.bam"
    shell:
        "bwa mem {input.ref} {input.r1} {input.r2} | samtools sort -o {output}"

rule index_alignment:
    input:
        "data/{sample}/{sample}_aligned.bam"
    output:
        "data/{sample}/{sample}_aligned.bam.bai"
    shell:
        "samtools index {input}"

rule call_variants:
    input:
        reference="data/reference/reference.fasta",
        bam="data/{sample}/{sample}_aligned.bam",
        index="data/{sample}/{sample}_aligned.bam.bai"
    output:
        "data/{sample}/{sample}_calls.bcf"
    shell:
        "bcftools mpileup -f {input.reference} {input.bam} | bcftools call --ploidy 1 -mv -Ob -o {output}"
        "&& bcftools index {output}"

rule consensus_sequence:
    input:
        reference="data/reference/reference.fasta",
        calls="data/{sample}/{sample}_calls.bcf"
    output:
        "data/{sample}/{sample}_consensus.fa"
    shell:
        "cat {input.reference} | bcftools consensus {input.calls} > {output}"
