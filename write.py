#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func(headA, headB):
    A = headA
    B = headB
    while A!=B:
        if A:
            A = A.next
        else:
            A = headB
        if B:
            B = B.next
        else:
            B = headA
    return A
    
    
        
    
    


if __name__ == '__main__':
    print(func([2,3,4]))