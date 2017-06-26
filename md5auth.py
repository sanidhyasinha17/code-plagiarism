import hashlib

def md5sum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


    #take the original file, comput its md5 sum.
    #take the skeptical file, comput its md5 sum.
    #if md5_original == md5_skeptical, the match is found . 