---
layout: page
title: Python
---

# [cohensd_1samp](https://github.com/tulimid1/cohens_d/blob/main/cohens_d/cohens_d.py)
---

Calculate cohen's d for 1 sample. See [Using_cohens_d.ipynb](https://github.com/tulimid1/cohens_d/blob/main/cohens_d/Using_cohens_d.ipynb) for a notebook of given examples. 

## Syntax
---
     import cohens_d as cD

[d = cD.cohensd_1samp(data)](#a)

[d = cD.cohensd_1samp(data, Name=Value)](#b)

## Description
---
### A
[d](#outarg) = cD.cohensd_1samp([data](#inarg1)) returns cohen's d for 1 sample comparing to [mu](#name-value-arguments)=0. [example](#example-1)

### B 
[d](#outarg) = cD.cohensd_1samp([data](#inarg1), [Name=Value](#name-value-arguments)) returns cohen's d for 1 sample with additional options specified by one name-value pair arguments. For example, you can compare to a mean of 15 ([mu](#name-value-arguments)=15). [example](#example-2)

## Examples 
---
### Example 1
Generate some random data and find cohen's d.  

    import numpy as np 
    
    data = np.random.normal(0, 1, size=(100,))
    d = cD.cohensd_1samp(data)

d = 0.058009400346186867

### Example 2 
Generate some random data and find cohen's d when comparing to mean of 15. 

    import numpy as np 
    
    data = np.random.normal(0, 1, size=(100,))
    d = cD.cohensd_1samp(data, mu=15)
    
d = 15.881558105056795

## Input Arguments
---
### ```data```
Data vector. 

Vector of data to calculate 1 sample cohen's d. 

Data Types: (numeric)

### Name-Value Arguments

Specified optional pairs of ```Name=Value``` arguments. ```Name``` is the is the argument name and ```Value``` is the corresponding value. You can specify several name and value pair arguments in any order as ```Name1=Value1,...,NameN=ValueN```. 

**Example**: ```mu=15``` specifies comparison to a mean of 15. 

### ```mu```
Mean to compare against (default=0)

Value to subtract from mean of [data](#inarg1). 

Data Types: (scalar, float, numeric)

## Output
---

### ```d```
Effect size. 

Cohen's d effect size for 1 sample test. 

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
