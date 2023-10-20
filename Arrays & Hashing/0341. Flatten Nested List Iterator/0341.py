# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]): # implementation into a list
        self.res = []
        self.idx = 0

        def convertThing(thing):
            if thing.isInteger():
                self.res.append(thing.getInteger())
            else: # thing is a list
                for item in thing.getList():
                    convertThing(item)

        for item in nestedList:
            convertThing(item)

    def next(self) -> int: # simply ask for the next value
        return_thing = self.res[self.idx]
        self.idx += 1
        return return_thing

    def hasNext(self) -> bool: # simple boolean 
        return True if self.idx < len(self.res) else False