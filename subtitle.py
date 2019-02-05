import re
import glob
import sys

def createNewFilename(path):
    p = '/'.join(path.split('/')[:-1]) + '/New_' + path.split('/')[-1]
    print(p)
    return p

dir = str(sys.argv[1])
if dir[-1] != '/':
    dir += '/'
print(dir)

srt_files = glob.glob(dir+'**/*.srt', recursive=True)
print(srt_files)

for filename in srt_files:
    f = open(filename, "r")
    text = f.read()
    regex = re.compile(r'{.*}', re.IGNORECASE)
    replaced = regex.sub("", text)
    regex = re.compile(u'前情回顧', re.IGNORECASE)
    replaced = regex.sub("", replaced)
    # print(replaced)
    newFile = createNewFilename(filename)
    f = open(newFile, "w")
    f.write(replaced)

f.close()
