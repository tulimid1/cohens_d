def cohensd_1samp(data, mu):
    import numpy 
    d = (numpy.mean(data) - mu) / numpy.std(data,ddof=1)
    return d 

def cohensd_2ind(mu1, mu2, std1, std2, n1, n2):
    import numpy
    d = (mu1 - mu2) / numpy.sqrt(((n1 - 1)*std1**2 + (n2 - 1)*std2**2) / (n1 + n2 - 2))
    return d 

def cohensd_2paired(pre, post, mu, r):
    import numpy
    d = (numpy.mean(pre - post) - mu) / (numpy.sqrt(numpy.var(pre, ddof=1) + numpy.var(post, ddof=1) - 2 * r * numpy.std(pre, ddof=1) * numpy.std(post, ddof=1)) / numpy.sqrt(2 * (1 - r)))
    return d 
