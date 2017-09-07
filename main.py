import os
import math
import urllib2
import csv
import matplotlib.pyplot as plt
import numpy as np
# from pylab import figure, axes, pie, title, show


# retrieve davis .csv database
# url = 'http://biochar.ucdavis.edu/files/data/data.csv';

# file_name = url.split('/')[-1]
# u = urllib2.urlopen(url)
# f = open(file_name, 'wb')
# meta = u.info()
# file_size = int(meta.getheaders("Content-Length")[0])
# print "Downloading: %s Bytes: %s" % (file_name, file_size)

# # downloading buffer
# file_size_dl = 0
# block_sz = 8192
# while True:
#     buffer = u.read(block_sz)
#     if not buffer:
#         break

#     file_size_dl += len(buffer)
#     f.write(buffer)
#     status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
#     status = status + chr(8)*(len(status)+1)
#     print status,

# f.close()

f = open("data.csv", 'rb')
reader = csv.reader(f)
headers = reader.next()

# rearrange to matrix of columns
column = {}
for h in headers:
    column[h] = []
    
for row in reader:
    for h, v in zip(headers, row):
        column[h].append(v)
        
# ask user for prompt of variable comparison?
# exp 1 = temp, 2 = ash...etc


# redefining of variables
t = column[headers[10]]
ash = column[headers[11]]
c = column[headers[13]]
n = column[headers[14]]
h = column[headers[15]]
o = column[headers[16]]
ph = column[headers[17]] 


# tedious replacement of empty variables (could loop this...)
for i in range(len(t)):
    if t[i] == '':
        t[i] = np.nan
    if ash[i] == '':
        ash[i] = np.nan
    if ash[i] == '':
        ash[i] = np.nan
    if c[i] == '':
        c[i] = np.nan
    if n[i] == '':
        n[i] = np.nan
    if h[i] == '':
        h[i] = np.nan
    if o[i] == '':
        o[i] = np.nan
    if ph[i] == '':
        ph[i] = np.nan

# tedious changing from string to np array of floats (could loop this...)
t = np.array(t)
t = t.astype(np.float)
ash = np.array(ash)
ash = ash.astype(np.float)
c = np.array(c)
c = c.astype(np.float)
n = np.array(n)
n = n.astype(np.float)
h = np.array(h)
h = h.astype(np.float)
o = np.array(o)
o = o.astype(np.float)
ph = np.array(ph)
ph = ph.astype(np.float)

print ph