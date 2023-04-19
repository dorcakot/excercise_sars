# !/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import argparse


def generate_plot(tumor, normal):
    normal = pd.read_csv(normal, sep='\t', names=["chr", "position", "depth"], dtype={"chr": str, "position": int, "depth":int})
    tumor = pd.read_csv(tumor, sep='\t', names=["chr", "position", "depth"], dtype={"chr": str, "position": int, "depth":int})

    window = 500
    tumor_red = np.add.reduceat(np.asarray(tumor['depth'][:len(normal['depth'])]), np.arange(0, len(normal['depth']), window))
    normal_red = np.add.reduceat(np.asarray(normal['depth']), np.arange(0, len(normal['depth']), window))
    pos = np.asarray([i for i in range(20000000, 20000000 + len(normal_red)*window, window)])
    sns.set(rc={'figure.figsize':(12,8)})
    plt.axhline(y=0)
    plt.ylabel('log2 depth ratio')
    plt.xlabel('chrX position')
    sns.scatterplot(x=pos, y=np.log2(tumor_red/normal_red)).figure.savefig("depth_ratio.png")

if __name__=='main':
    parser = argparse.ArgumentParser()
    parser.add_argument('tumor')
    parser.add_argument('normal')
    args = parser.parse_args()    
    generate_plot(args.tumor, args.normal)
