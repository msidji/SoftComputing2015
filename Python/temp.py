# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:17:51 2016

@author: Milos
"""

import notebookOperacije as my
import theano
import numpy
import scipy

n = [1.290192, 3.0002, 22.119199999999999, 3.4110999999999998, 12]
n = map(my.prettyFloat4, n)

x = 1.33333445
print 'xx', n, '\nx=', my.prettyFloat4(x)
print n.index(12)

#theano.test()
numpy.test()
#scipy.test()
