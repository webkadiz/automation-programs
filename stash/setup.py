from os import mkdir
from os.path import exists
from constants import STASH_DIR, STASH_ENTRIES_DIR, STASH_STATE_FILE

try:
    mkdir(STASH_DIR)
    mkdir(STASH_ENTRIES_DIR)
except:
    pass

if not exists(STASH_STATE_FILE):
    open(STASH_STATE_FILE, 'w').close()
