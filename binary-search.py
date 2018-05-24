# Quang Lam

class OrderedList(list):
    def __init__(self,contents=[]):
        super().__init__(contents)
        self.sorted = False


    def __iter__(self):
        if not self.sorted:
            self.sort()
            self.sorted = True

        return super().__iter__()

    def binarySearch(self, l, r, item):
        if r >= l:
            mid = int(l + (r - l) / 2)
            if self.__getitem__(mid) == item:
                return True
            if item > self.__getitem__(mid):
                return self.binarySearch(mid + 1, r, item)
            if item < self.__getitem__(mid):
                return self.binarySearch(l, mid - 1, item)
        else:
            return False

    def __contains__(self,item):
        if not self.sorted:
            self.sort()
            self.sorted = True

        # replace this line with your call to your binary search function.
        return self.binarySearch(0, super().__len__() - 1, item)

    def append(self,item):
        super().append(item)
        self.sorted = False

def main():
    lst = OrderedList()

    print("Binary Search Program")
    print("---------------------")
    print("Make a choice...")
    print("1. Insert into tree.")
    # print("2. Delete from tree.")
    print("2. Lookup value.")

    choice = 0
    while True:
        if choice < 1:
            try:
                choice = int(input("Choice? "))
                if choice < 1 or choice > 3:
                    break
            except ValueError:
                break
        else:
            if choice == 1:
                try:
                    num = int(input("Insert? "))
                    lst.append(num)
                except ValueError:
                    choice = 0
            if choice == 2:
                try:
                    num =int(input("Value? "))
                    if num in lst:
                        print("Yes,", num, "is in the tree.")
                    else:
                        print("No,", num, "is in the tree.")
                except ValueError:
                    choice = 0

if __name__ == "__main__":
    main()