def cohensd_1samp(data, mu):
    '''
    Calculate cohen's d for 1 sample. 

    INPUTS:
    data: data vector 
    mu: population mean 

    OUTPUT:
    d: absolute cohens d
    '''
    import numpy 
    d = numpy.abs((numpy.mean(data) - mu) / numpy.std(data,ddof=1))
    return d 

def cohensd_2ind(mu1, mu2, std1, std2, n1, n2):
    '''
    Calculate cohen's d for 2 independent samples 

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

def cohensd_2paired(pre, post, mu, r):
    '''
    Calculate cohen's d for 2 paired samples 

    INPUTS:
    pre: pre data vector 
    post: post data vector 
    mu: mean to compare 
    r: pearsons corrleation

    OUTPUT:
    d: absolute cohen's d 
    '''
    import numpy
    d = numpy.abs((numpy.mean(pre - post) - mu) / (numpy.sqrt(numpy.var(pre, ddof=1) + numpy.var(post, ddof=1) - 2 * r * numpy.std(pre, ddof=1) * numpy.std(post, ddof=1)) / numpy.sqrt(2 * (1 - r))))
    return d 
