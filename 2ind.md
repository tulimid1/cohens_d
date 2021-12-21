---
layout: page
title: Python
---

# [cohensd_2ind](https://github.com/tulimid1/cohens_d/blob/main/cohens_d/cohens_d.py)
---

Calculate cohen's d for 2 independent samples. See [Using_cohens_d.ipynb](https://github.com/tulimid1/cohens_d/blob/main/cohens_d/Using_cohens_d.ipynb) for a notebook of given examples. 

## Syntax
---
    import cohens_d as cD

[d = cD.cohensd_2ind(inarg1, inarg2)](#a)

## Description
---
### A
[d](#d) = cD.cohensd_2ind([group1](#group1), [group2](#group2)) returns cohen's d for 2 independent samples. [example](#example-1)

## Examples 
---
### Example 1
Generate some random data and find cohen's d.  

    import numpy as np 
    
    group1 = np.random.normal(0, 1, (100,))
    group2 = np.random.normal(1, 1, (150,))
    cD.cohensd_2ind(group1, group2)

d = 1.035420225827119

## Input Arguments
---
### ```group1```
Data vector for group 1. 

Vector of data to calculate cohen's d for 2 independent samples. 

Data Types: (numeric, vector)

### ```group2```
Data vector for group 2. 

Vector of data to calculate cohen's d for 2 independent samples. 

Data Types: (numeric, vector)

## Output
---

### ```d```
Effect size. 

Cohen's d effect size for 2 independent samples.  

Data Types: (scalar, float, numeric)

## More About 
---
[Lecture](https://github.com/joshcash9/Statistics_BME/blob/master/04_effect_power.pdf)

## Tips 
---

## Issues and Discussion 
---

[Issues](https://github.com/tulimid1/cohens_d/issues) and [Discussion](https://github.com/tulimid1/cohens_d/discussions).

If you don't know how to use github (or don't want to), just send me an [email](mailto:tulimid@udel.edu). 
