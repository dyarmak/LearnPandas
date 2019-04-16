import numpy as np
import pandas as pd

s = pd.Series([12, -4, 7, 9])
print(s)

s = pd.Series([12, -4, 7, 9], index=['a','b','c','d'])
print(s)

print(s.values)
print(s.index)
print(s['b'])
print(s[1])

s[1] = 0
print(s[1])

print(s/2)
print(s)

print(np.log(s))

serd = pd.Series([1,0,2,1,2,3], index=['white','white','blue','green',' green','yellow']) 
print(serd)
print(serd.unique()) # Returns a list of the unique values
print(serd.value_counts()) # Counts how many times a value appears and returns an array with the valus and its count
print(serd[serd.isin([0,3])]) # Returns entries that contain what is specified in []


s2 = pd.Series([5,-3,np.NaN,14])
print(s2)
print(s2.isnull())
print(s2.notnull()) # These are going to be handy functions! ****************************

print(s2[s2.isnull()]) # Here I am using meth: isnull() as a FILTER on the obj: s2 Series object
print(s2[s2.notnull()]) # The return is the index and value that satisfies the filter

# A dict can be imported as a Series
mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
myseries = pd.Series(mydict)
print(myseries)
colors = ['red','yellow','orange','blue','green']
myseries = pd.Series(mydict, index=colors) 
print(myseries)

mydict2 = {'red':400,'yellow':1000,'black':700}
myseries2 = pd.Series(mydict2) 
print(myseries2)

print(myseries+myseries2) # This combines all the labels, but only displays data where index is in both series

