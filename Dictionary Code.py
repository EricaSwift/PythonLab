"""
Erica Swift
Assignment due Feb. 25
Page 139, Figure 10.6 - modified
"""
class intDict(object):
    
    def __init__(self, numBuckets):
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, mocsID, mocDict):
        hashBucket = self.buckets[mocsID%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == mocsID:
                hashBucket[i] = (mocsID, mocDict)
                return
        hashBucket.append((mocsID, mocDict))
        
    def getValue(self, mocsID):
        hashBucket = self.buckets[mocsID%self.numBuckets]
        for e in hashBucket:
            if e[0] == mocsID:
                return e[1]
        return None
    
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}' #result[:-1] omits the last comma

#Page 139
D = intDict(11)
D.addEntry(926, 'Derek')
D.addEntry(954, 'Hailey')
D.addEntry(378, 'David')
D.addEntry(161, 'Sean')
D.addEntry(968, 'John')
D.addEntry(428, 'John')
D.addEntry(929, 'Eric')
D.addEntry(636, 'Jacob')
D.addEntry(569, 'Jackson')
D.addEntry(247, 'Erica')
D.addEntry(385, 'Jacob')

print 'The value of the intDict is:'
print D
print '\n', 'The buckets are:'
for hashBucket in D.buckets: #violates abstraction barrier
    print '  ', hashBucket
