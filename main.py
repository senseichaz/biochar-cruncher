import os
import math
import urllib2
import csv
import matplotlib.pyplot as plt
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

column = {}
for h in headers:
    column[h] = []
    
for row in reader:
    for h, v in zip(headers, row):
        column[h].append(v)

print headers