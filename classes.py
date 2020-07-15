class manga(dict):

    def __setitem__(self, key, item):
        if isinstance(key,str):
            key = key.casefold()
        super().__setitem__(key, item)

    