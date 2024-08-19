# pennycress-soil-moisture

A Python-based script for mapping Soil Water Availability (SWA) scores to identify climate divergence among pennycress natural accessions.

**Manuscript:**

`TBD`

**Directories:**

    pennycress-soil-moisture
    ├── country_parser.py
    ├── dryland_mask.npy
    ├── polygons.json
    ├── swa_scores.csv
    └── visualizations.ipynb

**Files**

The `country_parser.py` script parses the world-administrative-boundaries json file and returns a Python dictionary of country-polygon pairs.

The `dryland_mask.npy` file is a boolean numpy array of all dryland locations in an equispaced latitude-longitude grid and is used for plotting.

The `polygons.json` file includes sequences of latitude longitude coordinates that define the polygon boundaries for countries around the world.

The `swa_scores.csv` file includes spring and fall soil water availability scores to identify climate divergence among pennycress natural accessions.

The `visualizations.ipynb` notebook is used for data loading and figure generation.

**Citation:**

    TBD
