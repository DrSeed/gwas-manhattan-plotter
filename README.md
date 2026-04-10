# GWAS Manhattan Plot Generator

> You ran a GWAS on 500,000 variants. How do you visualise that? A Manhattan plot, named because it looks like the Manhattan skyline, shows every variant's significance across chromosomes. The peaks above the genome-wide significance line are your hits.

## What This Generates

**Manhattan Plot**: Every dot = a variant. X-axis = chromosome position. Y-axis = -log10(p-value). The red line at 5e-8 is the significance threshold (surviving ~1M effective tests).

**QQ Plot**: Observed vs. expected p-values. If most points follow the diagonal and only the tail shoots up, your GWAS is well-calibrated. If the whole distribution is inflated, you have population stratification. Check lambda: 1.0-1.05 is healthy, above 1.1 is concerning.

## Usage
```bash
python gwas_plots.py --sumstats data/gwas_results.txt --output plots/
```
