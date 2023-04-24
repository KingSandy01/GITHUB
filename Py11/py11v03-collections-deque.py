# using deque from collections library

import string
import collections


# print(string.ascii_lowercase)

def main():
    # pass
    myd = collections.deque(string.ascii_lowercase)
    print("Number of elements are: ", str(len(myd)))

    for i in myd:
        print(i, end=',')
    
    myd.popleft()
    myd.appendleft(11111)

    myd.rotate(5)


    print("\n", myd)


if __name__ == '__main__':
    main()
