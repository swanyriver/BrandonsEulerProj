import math

class digitInt(int):
    def __len__(self):
        return int(math.log10(self))+1

    def __getitem__(self,key):
        if isinstance(key, slice):
            l = len(self)
            start, stop = key.start, key.stop

            if start == None: start = 0
            if stop == None: stop = l

            if start < 0: start += l
            if stop < 0: stop += l
            if stop <= start: raise IndexError
            if stop>l or start>=l: raise IndexError

            a = self
            a = a//(10**(l-stop))
            return a%(10**(stop-start))


        elif isinstance(key, int) or isinstance(key, long):
            l = len(self)
            if key<0: key = l + key
            if key >= l: raise IndexError
            a = self
            a = a//(10**(l-key-1))
            return a%10


        else:
            raise TypeError

