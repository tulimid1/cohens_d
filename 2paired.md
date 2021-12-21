---
layout: page
title: Python
---

# [cohensd_2paired](https://github.com/tulimid1/cohens_d/blob/main/cohens_d/cohens_d.py)
---

Calculate cohen's d for 2 paired samples. See [Using_cohens_d.ipynb](https://github.com/tulimid1/cohens_d/blob/main/cohens_d/Using_cohens_d.ipynb) for a notebook of given examples. 

## Syntax
---
    import cohens_d as cD

[d = cD.cohensd_2paired(pre, post, r)](#a)

[d = cD.cohensd_2paired(pre, post, r, Name=Value)](#b)

## Description
---
### A
[d](#d) = cD.cohensd_2paired([pre](#pre), [post](#post), [r](#r)) returns cohen's d for 2 paired samples. [example](#example-1)

### B 
[d](#d) = cD.cohensd_2paired([pre](#pre), [post](#post), [r](#r), [Name=Value](#name-value-arguments)) returns cohen's d for 2 paired samples with additional options specified by one or more name-value pair arguments. For example, you can compare to a mean. [example](#example-2)

## Examples 
---
### Example 1
Generate some random data and find cohen's d. 

    mu = np.array([3, 5])
    sigma = np.array([[1, 0.6], [0.6, 3]])
    data = np.random.multivariate_normal(mu, sigma, (100,))
    cD.cohensd_2paired(data[:,0], data[:,1], stats.pearsonr(data[:,0], data[:,1])[0])

d = 1.4798889031781874

### Example 2 
Generate some random data and calculate cohen's d with mean of 15. 

    mu = np.array([3, 5])
    sigma = np.array([[1, 0.6], [0.6, 3]])
    data = np.random.multivariate_normal(mu, sigma, (100,))
    cD.cohensd_2paired(data[:,0], data[:,1], stats.pearsonr(data[:,0], data[:,1])[0], mu=15)
    
d = 11.677274518688368

## Input Arguments
---
### ```pre```
Pre data vector

Vector of pre data. 

Data Types: (numeric, vector)

### ```post```
Post data vector. 

Vector of post data

Data Types: (numeric, vector)

### `r`
Correlation of pre and post. 

Pearson's correlation (r) of pre and post data. 

Data Types: (numeric, scalar)

### Name-Value Arguments

Specified optional pairs of ```Name=Value``` arguments. ```Name``` is the is the argument name and ```Value``` is the corresponding value. You can specify several name and value pair arguments in any order as ```Name1=Value1,...,NameN=ValueN```. 

**Example**: ```mu=15``` specifies compare difference in pre and post against mean of 15. 

### ```mu```
Mean to compare against (default=0)

Mean to compare difference of [pre](#pre) and [post](#post) data vectors against. 

Data Types: (scalar, numeric, float)

## Output
---

### ```d```
Effect size. 

Cohen's d effect size for 2 paired samples. 

Data Types: (scalar, float, numeric)

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
