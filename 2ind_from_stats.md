---
layout: page
title: Python
---

# [cohensd_2ind_from_stats](https://github.com/tulimid1/cohens_d/blob/main/cohens_d/cohens_d.py)
---

Calculate cohen's d for 2 independent samples from the group statistics. See [Using_cohens_d.ipynb](https://github.com/tulimid1/cohens_d/blob/main/cohens_d/Using_cohens_d.ipynb) for a notebook of given examples. 

## Syntax
---
    import cohens_d as cD

[d = cD.cohensd_2ind_from_stats(mu1, mu2. std1, std2, n1, n2)](#a)

## Description
---
### A
[d](#d) = cD.cohensd_2ind_from_stats([mu1](#mu1), [mu2](#mu2), [std1](#std1), [std2](#std2), [n1](#n1), [n2](#n2)) returns cohen's d for 2 independent samples from statistics. [example](#example-1)

## Examples 
---
### Example 1
Generate some arbitrary parameters and find cohen's d.  

    mu1, mu2, std1, std2, n1, n2 = 10, 5, 1, 1.5, 100, 105
    cD.cohensd_2ind_from_stats(mu1=mu1, mu2=mu2, std1=std1, std2=std2, n1=n1, n2=n2)

d = 3.9038750287682418

## Input Arguments
---
### ```mu1```
Mean of group 1. 

Data Types: (scalar, float)

### ```mu2```
Mean of group 2. 

Data Types: (scalar, float)

### ```std1```
Standard deviation of group 1.

Data Types: (scalar, float)

### ```std2```
Standard deviation of group 2. 

Data Types: (scalar, float)

### ```n1```
Sample size of group 1. 

Data Types: (scalar, float)

### ```n2```
Sample size of group 2. 

Data Types: (scalar, float)

## Output
---

### ```d```
Effect size. 

Cohen's d effet size for 2 independent samples from statistics. 

Data Types: (scalar, float)

## More About 
---
[Lecture](https://github.com/joshcash9/Statistics_BME/blob/master/04_effect_power.pdf)

I refrained from outputting size of effect (e.g., 'small', 'medium', 'large') because these are arbitrary and should be thought of as such. 

## Tips 
---

## Issues and Discussion 
---

[Issues](https://github.com/tulimid1/cohens_d/issues) and [Discussion](https://github.com/tulimid1/cohens_d/discussions).

If you don't know how to use github (or don't want to), just send me an [email](mailto:tulimid@udel.edu). 
