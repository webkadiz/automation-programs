from os.path import exists
from constants import STASH_STATE_FILE


KEY_FIELDS = [
    NAME := 'name',
    TYPE := 'type',
    DEFAULT := 'default',
]
KEYS = [
    ENTRIES_LEN := {
        'name': 'ENTRIES_LEN',
        'type': int,
        'default': 0,
    },
    LAST_ENTRY := {
        'name': 'LAST_ENTRY',
        'type': str,
        'default': '',
    },
    LAST_ENTRY_POS := {
        'name': 'LAST_ENTRY_POS',
        'type': int,
        'default': 0,
    }
]

class State():
    def __init__(self):
        self.setup()

    def setup(self):
        self.dict = {}

        for key in KEYS:
            self[key] = key.get(DEFAULT)

        with open(STASH_STATE_FILE, 'r+') as stateFile:
            for i, line in enumerate(stateFile):
                stateValue = line.strip()
                self[KEYS[i]] = stateValue

    def __getitem__(self, key):
        stateValue = self.dict[key.get(NAME)]

        typedStateValue = key.get(TYPE)(stateValue)
        
        return typedStateValue

    def __setitem__(self, key, value):
        try:
            self.dict[key.get(NAME)] = key.get(TYPE)(value)
        except:
            self.dict[key.get(NAME)] = key.get(DEFAULT)
    
    def save(self):
        with open(STASH_STATE_FILE, 'w') as stateFile:
            for key in KEYS:
                stateFile.write(str(self[key]) + '\n')


state = State()

# export

__all__ = ['state']

for key in KEYS:
    __all__.append(key.get(NAME))
