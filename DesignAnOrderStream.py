#!/usr/bin/python3

class OrderedStream:

    def __init__(self, n: int):
        self._length = n
        self._chunk = []
        self._pointer = 0
        for i in range(n+1):
            self._chunk.append([])

    def insert(self, idKey: int, value: str):
        self._chunk[idKey-1] = value
        output = []
        for i in range(self._pointer, self._length):
            if self._chunk[i] == [] and output == []:
                return []
            elif self._chunk[i] == []:
                self._pointer = i
                break
            else:
                output.append(self._chunk[i])
        return output


    
# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
stream = OrderedStream(5)
print(stream.insert(3, "ccccc"))
print(stream.insert(1, "aaaaa"))
print(stream.insert(2, "bbbbb"))
print(stream.insert(5, "eeeee"))
print(stream.insert(4, "ddddd"))
