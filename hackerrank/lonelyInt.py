#!/usr/bin/py
def lonelyinteger(a):
    for x in a:
        if (a.count(x)==1):
            answer = x
            break
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
