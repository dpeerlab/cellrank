# Overview
![Overview-image](https://github.com/dpeerlab/cellrank/blob/main/cellrank_fate_map.png)

**CellRank** is a scalable, easy to use framework to compute directed cell-state trajectories and uncover cellular dynamics based on Markov state modeling of single-cell data. It is applicable to many single-cell fate mapping scenarios including regeneration, reprogramming and disease, for which direction is unknown. 

CellRank works in two parts: [kernels](https://cellrank.readthedocs.io/en/stable/classes.html#kernels) compute cell-cell transition probabilities and [estimators](https://cellrank.readthedocs.io/en/stable/classes.html#estimators) generate hypothesis based on the previous step. Our kernels are able to take many different types of data as input. Our main estimator is Generalized Perron Cluster Cluster Analysis (G-PCCA) [Reuter et al., 2018] which coarse-grains the Markov chain into a set of macrostates which represent initial, terminal and intermediate states. For each transient cell, we compute its fate probability towards any terminal state. 

CellRank was developed in collaboration between the [Theis lab](https://github.com/theislab) and the Peer lab.

For more information, feel free to refer to our [official page](https://cellrank.readthedocs.io/en/stable/index.html#) or our manuscript [Lange et al. (2022)](https://www.nature.com/articles/s41592-021-01346-6) in **Nature Methods**.

# Installation
For more in-depth instructions, visit our [installation page](https://cellrank.readthedocs.io/en/stable/installation.html).

CellRank can be installed via:
## Bioconda
```
conda install -c conda-forge -c bioconda cellrank
# or with extra libraries, useful for large datasets
conda install -c conda-forge -c bioconda cellrank-krylov
```
## Pypi
```
pip install cellrank
# or with extra libraries, useful for large datasets
pip install 'cellrank[krylov]'
# or with external modules, see External API
pip install 'cellrank[external]'
```
# Usage
Please refer to our [official page](https://cellrank.readthedocs.io/en/stable/index.html#) for various examples and tutorials on how to use CellRank.
