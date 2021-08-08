from os.path import join
from constants import STASH_ENTRIES_DIR

def copyEntity(src, dest):
    with open(src) as srcFile, open(dest, 'w') as destFile:
        for line in srcFile:
            destFile.write(line)

def entityPathByIdx(idx):
    return join(STASH_ENTRIES_DIR, str(idx))

