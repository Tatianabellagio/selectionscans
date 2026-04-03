# selectionscans

Selection scan analyses for *Arabidopsis thaliana* populations. The repository compares modern and historical samples to detect signatures of recent selection, and applies multiple complementary statistics to identify selective sweeps in contemporary populations.

---

## Analyses

### Modern vs historical

Compares allele frequency spectra and diversity statistics between historical and modern GrENE-Net samples to detect loci with signatures of recent directional change.

| Statistic | File |
|-----------|------|
| Nucleotide diversity (π) | `df_pi_hist_vs_modern_w1000.csv` |
| FST, ΔAF, ΔHe | `fst_deltaaf_deltahe.csv` |

### Selective sweep scans (modern samples)

Multiple statistics applied genome-wide to identify candidate sweep regions.

| Method | File |
|--------|------|
| iHH12 | `selection_scan/ihh12_maf01_all.csv` |
| nSL | `selection_scan/nsl_all_maf01.csv` |
| Nucleotide diversity (π) | `selection_scan/pi_all_maf01.csv` |
| SweepFinder2 | `sweepfinder/sweep_df_results100w_nb.csv` |
| Omega | `omega/omega_grid1000.csv` |

---

## Repository structure

```
preprocessing.ipynb            # Data preprocessing and filtering
modern_vs_historical.ipynb     # Modern vs historical comparison
selection_scan/                # iHH12, nSL, and π results
sweepfinder/                   # SweepFinder2 results
omega/                         # Omega statistic results
climate/                       # Climate covariate data
```

---

## Tools & dependencies

- [scikit-allel](https://scikit-allel.readthedocs.io/) — population genetics statistics (iHH12, nSL, π, FST)
- [SweepFinder2](https://personal.utdallas.edu/~csw022000/sweepfinder2.html) — composite likelihood sweep detection
- Python 3, Jupyter
