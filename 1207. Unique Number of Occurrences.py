class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        
        # create a hash map
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        if len(set(dic.values())) != len(set(arr)):
            return False
        return True
      
      ## My solution
      
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
               
        # create a hash map
        a = Counter(arr)
        

        if len(set(a.values())) != len(set(arr)):
            return False
        return True
      
