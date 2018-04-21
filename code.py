import os, sys
import hashlib
parentFolder='E:/resume_sep15'
def hashfile(path, blocksize = 65536):
    if os.path.islink(path):
    	afile=os.readlink(path)
    	afile = open(path, 'rb')
    else:
    	afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
dict1 = {}
for dirName, subdirs, fileList in os.walk(parentFolder):
    for filename in fileList:
        path = os.path.join(dirName, filename)
        file_hash = hashfile(path)
        if file_hash in dict1:
            dict1[file_hash].append(path)
        else:
            dict1[file_hash] = [path]
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('*******************')
    else:
        print('No duplicate files found.')
printResults(dict1)