# bibtex-subscript-fixer
A Python script to automatically convert chemical formulas in BibTeX files into proper subscript notation (e.g., TiO₂, CO₂).

This Python script automatically converts chemical formulas in `.bib` reference files into proper subscript notation for use in Mendeley, Zotero, or LaTeX.

### Example
- `TiO2` → `TiO<sub>2</sub>`
- `Fe2O3` → `Fe<sub>2</sub>O<sub>3</sub>`
- `CO2` → `CO<sub>2</sub>`

### Usage
```bash
python fix_bib_subscripts.py input.bib output.bib
