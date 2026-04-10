#!/usr/bin/env python3
import pandas as pd, numpy as np, argparse
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

def manhattan_plot(df, output, sig_level=5e-8):
    df['-log10p'] = -np.log10(df['P'])
    offset = 0; ticks = []; labels = []
    for chrom in sorted(df['CHR'].unique()):
        mask = df['CHR'] == chrom
        df.loc[mask, 'cumpos'] = df.loc[mask, 'BP'] + offset
        ticks.append(df.loc[mask, 'cumpos'].median())
        labels.append(str(chrom))
        offset = df.loc[mask, 'cumpos'].max()
    fig, ax = plt.subplots(figsize=(16, 6))
    colors = ['#1f77b4', '#aec7e8']
    for chrom in df['CHR'].unique():
        mask = df['CHR'] == chrom
        ax.scatter(df.loc[mask, 'cumpos'], df.loc[mask, '-log10p'], s=2, c=colors[chrom % 2], alpha=0.7)
    ax.axhline(-np.log10(sig_level), color='red', linestyle='--')
    ax.set_xticks(ticks); ax.set_xticklabels(labels)
    ax.set_xlabel('Chromosome'); ax.set_ylabel('-log10(p-value)')
    plt.tight_layout(); plt.savefig(output, dpi=300); plt.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sumstats', required=True)
    parser.add_argument('--output', default='plots')
    args = parser.parse_args()
    Path(args.output).mkdir(exist_ok=True)
    df = pd.read_csv(args.sumstats, sep='\t')
    manhattan_plot(df, f'{args.output}/manhattan.png')
    print('Plots generated.')

if __name__ == '__main__':
    main()
