#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:53:17 2021

@author: VictoriaZhao
"""
import math


#1 Compare Version Number 

def CompVernN(version1, version2):
    list1 = [int(v) for v in str(version1).split(".")]
    list2 = [int(v) for v in str(version2).split(".")]
    for i in range(max(len(list1),len(list2))):
        v1 = list1[i] if i < len(list1) else 0
        v2 = list2[i] if i < len(list2) else 0
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1;
    return 0;
     
CompVernN(3.1, 1.9)

#2 Excel Sheet Column Title
#numb = 82595524
def converttotitle(numb):
    cha = []
    result = []
    nolast = 999
    last = 999
    
    for i in range(ord("A"),ord("Z")+1):
        cha.append(chr(i));
    
    while nolast > 0:
        nolast, last = divmod(numb-1,26)
        result.append(cha[last])
        numb = nolast
        result.reverse()
    return"".join(result)

converttotitle(82595524)

#3 Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s):
    ChaSet = []
    l = 0
    res = 0
    
    for r in range(0,len(s)):
        while s[r] in ChaSet:
            ChaSet.remove(s[l])
            l += 1;
        ChaSet.append(s[r])
        res = max(res,r-l+1)
    return res
            
lengthOfLongestSubstring("abcabcbb")

#4 Longest Palindromic Substring
# s = "cbba"

def longestPalindrome(s):
    res = ""
    reslen = 0
    
    for i in range(len(s)):
        #odd 
        if len(s) % 2 == 1: r = l = i
        else: l , r = i, i+1
        
        while l >= 0 and r < len(s) and s[r] == s[l]:
            if (r-l+1) > reslen:
                reslen = r-l+1
                res = s[l:r+1]
            r += 1 
            l -= 1
    return res

longestPalindrome('babad')

#5  Maximum Gap

def maximumGap(nums):
    res = []
    interval  = math.ceil((max(nums)-min(nums))/(len(nums)-2+1))
    n_buckets = (max(nums)-min(nums))//interval+1
    buckets = [[None,None] for b in range(1,n_buckets+1)]
    
    if len(nums) < 2: res = 0
    if max(nums) - min(nums) == 0: res = 0;
    
    for n in nums:
        bucket = buckets[(n - min(nums))// interval]
        bucket[0] = min(bucket[0],n) if bucket[0] else n
        bucket[1] = max(bucket[1],n) if bucket[1] else n
    
    buckets = [bk for bk in buckets if bk[0]]
    
    for i in range(1,len(buckets)): res.append( buckets[i][0]-buckets[i-1][1] )
    result = max(res)

    return result

maximumGap([3,6,9,1])

#6 Median of Two Sorted Arrays - omit please don't do it
#7 Two Sum 

def twoSum(nums , target):

    HashMap = {} # value : index
    for i, n in enumerate(nums):
        #print (i,n)
        diff = target - n
        if diff in HashMap: 
            return [HashMap[diff],i]
        HashMap[n] = i
        
        
twoSum([2,7,11,15] ,9)

#8 Two Sum II - Input array is sorted
def twoSum2(numbers, target):
    l = 0
    r = len(numbers) -1
    
    while l<r:
        sum2 = numbers[l] + numbers[r]
        
        if sum2 > target:
            r -= 1
        elif sum2 < target:
            l += 1
        else:
            return [l+1, r+1]


twoSum2([2,7,11,15], 9)


#9 Reverse Integer
#x = 123
def reverse(x):   
    MIN = -2147483648 # -2**31
    MAX = 2147483647  # 2**31-1
    
    res = 0    
    while x>0:
        digit = int(math.fmod(x,10))                    #-1 % 10 = 9
        x = int(x/10)
        if (res > MAX//10 or
            (res == MAX//10 and digit >= (MAX % 10))):
                return 0
        if (res < int(MIN/10) or
              (res == int(MIN/10) and digit < math.fmod(MIN,10))):
                return 0
        res = (res*10) + digit
    return res
    
reverse(123)


        
   



    
        
    
























