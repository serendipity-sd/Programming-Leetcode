from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        (time[i]+ time[j]) % 60 =  0 
        case one:
            time[i] % 60 + time[j] % 60 = 60 
            20 % 60 + 100 % 60 = 20 + 40 = 60
        case two:
            time[i] % 60 = 0
            time[j] % 60 = 0
            60  % 60 = 0
            120 % 60 = 0
        """
        result = 0 
        mapping = defaultdict(int)
        for t in time:
            key = t % 60
            if key == 0:
                result += mapping[0]
            else:
                result += mapping[60 - key]
            mapping[key] += 1
        return result
