# `Description` 

[![DOI](https://zenodo.org/badge/457334153.svg)](https://zenodo.org/badge/latestdoi/457334153)

Tutorial to generate bins. The html version can be found [here](https://ndombrowski.github.io/Binning_tutorial//index.html).

The goal of this tutorial is to: 

- Work with the contigs we generated in the Assembly tutorial (or your own contigs)
- Do the read mapping and generate coverage files
- Adjust the coverage files for the different binning tools
- Bin with Metabat, Maxbin, Concoct, BinSanity
- Combine bins from different the binning tools by using DasTool
- Get the genome stats
- Get a first overview of the taxonomic assignment
- Create summary documents for the contigs and bins

For this tutorial we work with assemblies (and the raw reads) from 3 metagenomes. The reason to include more than one metagenome is that most binning tools take into account sequence information as well as coverage information, which make use of having data from several metagenomes (i.e. depth profiles in our case).

# `Cite`

If you found this tutorial useful and use it in your work and you reuse some code feel free to add a link to this repository to your methods section.

