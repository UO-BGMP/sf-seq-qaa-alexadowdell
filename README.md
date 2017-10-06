# SF-seq_QAA

This assignment is due Wednesday, Oct 4 by 11:59 PM.

Be sure to upload all relevant materials by the deadline and **double check** to be sure that your off-line repository is up-to-date with your on-line repository. Answers to the questions can be submitted as ```html```, Github markdown, or ```pdf```.

------------------------------------------------------------------------------------------------------------------------------
# Contents of `sf-seq-qaa-alexadowdell`

The master repository for `sf-seq-qaa-alexadowdell` contains the following:
- FastQCFiles/
- Part1/	
- Part2/
- Part3/	
- Scripts/
- `Bi624_PS1.Rmd`
- `Bi624_PS1.html`
- `Bi624_PS1.pdf`	

The contents of each one of the folders above with a short associated description can be found below:

- **FastQCFiles/**
  1. *22_3H_both/*
    - 22_3H_both_S16_L008_R1_001_fastqc/: FastQC outputs for R1 including statistics and associated plots
    - 22_3H_both_S16_L008_R2_001_fastqc/: FastQC outputs for R2 including statistics and associated plots
  2. *32_4G_both/*
    - 32_4G_both_S23_L008_R1_001_fastqc/: FastQC outputs for R1 including statistics and associated plots
    - 32_4G_both_S23_L008_R1_001_fastqc/: FastQC outputs for R2 including statistics and associated plots

- **Part1/**
  - `22_3H_R1_dist_output.tsv`: Per base sequence quality distribution for 22_3H_both R1 file in .tsv format
  - `22_3H_R2_dist_output.tsv`: Per base sequence quality distribution for 22_3H_both R2 file in .tsv format
  - `32_4G_R1_dist_output.tsv`: Per base sequence quality distribution for 32_4G_both R1 file in .tsv format
  - `32_4G_R2_dist_output.tsv`: Per base sequence quality distribution for 32_4G_both R2 file in .tsv format
  - `R1_22_3H_part2Plot.tsv`: Per sequence quality scores distribution for 22_3H_both R1 file in .tsv format
  - `R1_32_4G_part2Plot.tsv`: Per sequence quality scores distribution for 32_4G_both R1 file in .tsv format
  - `R2_22_3H_part2Plot.tsv`: Per sequence quality scores distribution for 22_3H_both R2 file in .tsv format
  - `R2_32_4G_part2Plot.tsv`: Per sequence quality scores distribution for 32_4G_both R2 file in .tsv format
  
- **Part2/**
  1. *Cutadapt/*
    - `slurm-22_3H.out`: Output summary of run statistics for 22_3H_both library post-cutadapt trimming
    - `slurm-32_4G.out`: Output summary of run statistics for 32_4G_both library post-cutadapt trimming
    - `trimmed_cutadapt_22_3H.R1.tsv`: Distribution of read lengths and associated counts for 22_3H_both R1 trimmed cutadapt file
    - `trimmed_cutadapt_22_3H.R2.tsv`: Distribution of read lengths and associated counts for 22_3H_both R2 trimmed cutadapt file
    - `trimmed_cutadapt_32_4G.R1.tsv`: Distribution of read lengths and associated counts for 32_4G_both R1 trimmed cutadapt file
    - `trimmed_cutadapt_32_4G.R2.tsv`: Distribution of read lengths and associated counts for 32_4G_both R2 trimmed cutadapt file
    
  2. *Process_shortreads/*
    - `22_3H_both_R1_trimmed_dist.tsv`: Distribution of read lengths and associated counts for 22_3H_both R1 trimmed process_shortreads file
    - `22_3H_both_R2_trimmed_dist.tsv`: Distribution of read lengths and associated counts for 22_3H_both R2 trimmed process_shortreads file
    - `32_4G_both_R1_trimmed_dist.tsv`: Distribution of read lengths and associated counts for 32_4G_both R1 trimmed process_shortreads file 
    - `32_4G_both_R2_trimmed_dist.tsv`: Distribution of read lengths and associated counts for 32_4G_both R2 trimmed process_shortreads file

- **Part3/**
  - `Mus_musculus.GRCm38.rRNAonly.fa`: rRNA sequences extracted from Ensembl ncRNA used to generate the gmap database

- **Script/**
  - `cutadapt22.srun`: Shell script for cutadapt adapter trimming on library 22_3H_both
  - `cutadapt32.srun`: Shell script for cutadapt adapter trimming on library 32_4G_both
  - `mouseDB.srun`: Shell script for Gmap construction of mouse database using rRNA sequences
  - `mouseGsnap22trim.srun`: Shell script for gsnap run on 22_3H_both library trimmed files from cutadapt output
  - `mouseGsnap32trim.srun`: Shell script for gsnap run on 32_4G_both library trimmed files from cutadapt output
  - `part1Hist1.py`: Python script to generate per base sequence quality distribution for 22_3H_both R1 file
  - `part1Hist1.srun`: Shell script adapted for both libraries and R1/R2 reads to obtain the per base sequence quality distribution output. Runs `part1Hist1.py`, `part1Hist2.py`, `part1Hist3.py`, and `part1Hist4.py`
  - `part1Hist2.py`: Python script to generate per base sequence quality distribution for 22_3H_both R2 file
  - `part1Hist3.py`: Python script to generate per base sequence quality distribution for 32_4G_both R1 file
  - `part1Hist4.py`: Python script to generate per base sequence quality distribution for 32_4G_both R2 file
  - `part2FreqDist.py`: Python script to generate per sequence quality score distributions for both 22_3H_both and 32_4G_both R1 and R2 files 
  - `part2FreqDist.srun`: Shell script called to run `part2FreqDist.py` passed four files as arguments
  - `processShortreads22.srun`: Shell script for process_shortreads adapter trimming on library 22_3H_both
  - `processShortreads32.srun`: Shell script for process_shortreads adapter trimming on library 32_4G_both


- `Bi624_PS1.Rmd`: Rmarkdown file containing full compilation of project including answers to questions, steps taken during each process, R code and scripts used. 

- `Bi624_PS1.html`: Raw html file containing full compilation of project including answers to questions, steps taken during each process, R code and scripts used. 

- `Bi624_PS1.pdf`: PDF generated from Knitr html containing full compilation of project including answers to questions, steps taken during each process, R code and scripts used. 







