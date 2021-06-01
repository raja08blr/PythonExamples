import glob
import hashlib

d = {}

path = r"C:\Users\QuickboostTest\Documents\RajareddyV\UK\*.*"

file = glob.glob(path)

for f in file:
    with open(f, 'rb') as getmd5:
        data = getmd5.read()
        gethash = hashlib.md5(data).hexdigest()
        print("f: " + gethash)
        d[f] = gethash
print(d)