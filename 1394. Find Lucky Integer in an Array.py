## Solution 1 

class Solution:
	def findLucky(self, arr: List[int]) -> int:
		s=-1
		a=Counter(arr)
		b=list(set(arr))
		for i in b:
			if i==a[i]:
				s=max(s,i)
		return s
    
    
  ## My solution
  
class Solution:
  def findLucky(self, arr: List[int]) -> int:
      dic = {}
      list1 = []
      for i in arr:
          if i in dic:
              dic[i] +=1
          else:
              dic[i] = 1
      for i in dic:
          if dic[i] == i:
              #print(i)
              list1.append(i)
      #print(max(list1))
      a = sorted(list1)
      return a[-1]


        
