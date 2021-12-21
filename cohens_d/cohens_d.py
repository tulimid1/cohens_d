def cohensd_1samp(data, mu=0):
    '''
    Calculate cohen's d for 1 sample. 

    INPUTS:
    data: data vector 
    mu: population mean, default=0

    OUTPUT:
    d: absolute cohens d
    '''
    import numpy 
    d = numpy.abs((numpy.mean(data) - mu) / numpy.std(data,ddof=1))
    return d 

def cohensd_2ind_from_stats(mu1, mu2, std1, std2, n1, n2):
    '''
    Calculate cohen's d for 2 independent samples from statistics

    INPUTS:
    mu1: mean of group 1 
    mu2: mean of group 2 
    std1: standard deviation of group 1
    std2: standard deviation of group 2 
    n1: n of group 1 
    n2: n of group 2 

    OUTPUT:
    d: absolute cohen's d 
    '''
    import numpy
    d = numpy.abs((mu1 - mu2) / numpy.sqrt(((n1 - 1)*std1**2 + (n2 - 1)*std2**2) / (n1 + n2 - 2)))
    return d 

def cohensd_2ind(group1, group2):
    '''
    Calculate cohen's d for 2 independent samples 

    INPUTS:
    group1: group 1 data vector 
    group2: group 2 data vector 

    OUTPUTS:
    d: absolute cohen's d 
    '''
    import numpy 
    d = (numpy.mean(group1) - numpy.mean(group2)) / (numpy.sqrt((((len(group1) - 1) * numpy.var(group1, ddof=1)) + ((len(group2) - 1) * numpy.var(group2, ddof=2))) / (len(group1) + len(group2) - 2)))
    return numpy.abs(d)

def cohensd_2paired(pre, post, r, mu=0):
    '''
    Calculate cohen's d for 2 paired samples 

    INPUTS:
    pre: pre data vector 
    post: post data vector 
    r: pearsons corrleation
    mu: mean to compare, default=0

    OUTPUT:
    d: absolute cohen's d 
    '''
    import numpy
    d = numpy.abs((numpy.mean(pre - post) - mu) / (numpy.sqrt(numpy.var(pre, ddof=1) + numpy.var(post, ddof=1) - 2 * r * numpy.std(pre, ddof=1) * numpy.std(post, ddof=1)) / numpy.sqrt(2 * (1 - r))))
    return d 
