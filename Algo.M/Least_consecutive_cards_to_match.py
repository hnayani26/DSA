from typing import List
import math

def least_consecutive_cards_to_match(arr: List[int]) -> int:
   
    min_win=math.inf
    left=0
    hm={}
    hm[arr[0]]=1
    
    for right in range(1,len(arr)):
        if(arr[right] in hm):
            hm[arr[right]]+=1
        else:
            hm[arr[right]]=1
            
        while(hm[arr[right]]>1):
                min_win=min(min_win,right-left+1)
                hm[arr[left]]-=1
                left += 1
                
    if(min_win==math.inf):
        return -1
            
    return min_win

if __name__ == '__main__':
    cards = [3, 4, 2, 3, 4, 7]
    res = least_consecutive_cards_to_match(cards)
    print(res)
