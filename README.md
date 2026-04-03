# selectionscans

Selection scan analyses for *Arabidopsis thaliana* populations. The repository compares modern and historical samples to detect signatures of recent selection, and applies multiple complementary statistics to identify selective sweeps in contemporary populations.

All code, step-by-step methodology, and result datasets are in this repository. Each analysis notebook links to the relevant tool documentation with explanations of the theory behind each statistic.

---

## Summary of findings

Two sets of analyses were performed:

**1. Modern vs historical comparison** (FST, ΔAF, Δheterozygosity, Δπ) — Cross-checks with independent temporal data. Results are consistent with GWAS hits and provide a useful validation layer, particularly for variants showing frequency shifts between time points.

**2. Selective sweep scans on modern samples** (iHH12, nSL, π, SweepFinder2, Omega) — Each tool captures a different genomic signal left by a sweep (reduced diversity, elevated haplotype homozygosity, high LD, shifts in the SFS), making them complementary.

### Key candidate: AT2G21840 – AT2G21860 (Chr 2)

The strongest and most consistent signal is near **AT2G21840–AT2G21860**:

- A sharp reduction in nucleotide diversity (π) is visible in modern (1001 Genomes) samples within ~5 kb of those genes, consistent with a **completed selective sweep** (virtually no diversity remaining)
- **SweepFinder2** shows a major CLR peak within 50 kb of this region — the highest genome-wide signal
- The modern vs historical comparison (FST and ΔAF) also peaks around these genes, consistent with the GEA/GWAS hits
- Other haplotype-based statistics (iHH12, nSL) have difficulty detecting this signal, likely because the sweep is complete and rare alleles have been removed — many tools filter on low MAF, which would exclude the sweep footprint

This pattern suggests a **hard, completed sweep** at or near AT2G21840.

### Secondary candidate: AT4G05100 (Chr 4)

Around **AT4G05100**, the signal is more consistent with an **incomplete sweep**:

- iHH12 and nSL both show elevated homozygosity at this locus — the classic signature of a sweep in progress
- The signal is not a dominant peak but shows consistent low heterozygosity surrounded by regions of higher heterozygosity
- Also recovers as a peak in the modern vs historical FST and ΔAF comparison

---

## Analyses

### Modern vs historical

| Statistic | File |
|-----------|------|
| Nucleotide diversity (π) | `df_pi_hist_vs_modern_w1000.csv` |
| FST, ΔAF, ΔHe | `fst_deltaaf_deltahe.csv` |

Notebook: `modern_vs_historical.ipynb`

### Selective sweep scans (modern samples)

| Method | Signal detected | File |
|--------|----------------|------|
| iHH12 | Elevated haplotype homozygosity | `selection_scan/ihh12_maf01_all.csv` |
| nSL | Elevated haplotype homozygosity | `selection_scan/nsl_all_maf01.csv` |
| π | Reduced nucleotide diversity | `selection_scan/pi_all_maf01.csv` |
| SweepFinder2 | Shift in site frequency spectrum | `sweepfinder/sweep_df_results100w_nb.csv` |
| Omega | High LD flanking the sweep | `omega/omega_grid1000.csv` |

Notebooks: `selection_scan/`, `sweepfinder/sweepfinder.ipynb`, `omega/omega.ipynb`

---

## Repository structure

```
preprocessing.ipynb            # Data preprocessing and filtering
modern_vs_historical.ipynb     # Modern vs historical comparison (FST, ΔAF, Δπ, ΔHe)
selection_scan/                # iHH12, nSL, π (selscan)
sweepfinder/                   # SweepFinder2
omega/                         # Omega statistic
climate/                       # Climate covariate data for ecotypes and sites
figures/                       # Result plots
```

---


## Tools & dependencies

- [scikit-allel](https://scikit-allel.readthedocs.io/) — FST, π, ΔAF, ΔHe
- [selscan](https://github.com/szpiech/selscan) — iHH12, nSL
- [SweepFinder2](https://personal.utdallas.edu/~csw022000/sweepfinder2.html) — composite likelihood ratio sweep detection
- [OmegaPlus](https://cme.h-its.org/exelixis/web/software/omegaplus/) — LD-based sweep detection
- Python 3, R, Jupyter
