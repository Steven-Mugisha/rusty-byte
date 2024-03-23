class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        max_sum = 0
        # trees = 2
        # counter = defaultdict(trees)
        counter = {}

        for idx, fruit in enumerate(fruits):

            if fruit in counter:
                counter[fruit] += 1
            
            else:
                counter[fruit] = 1

            if len(counter.keys()) <= 2:
                curr_sum = 0
                for key, val in counter.items():
                    curr_sum += val 
                max_sum = max(max_sum, curr_sum)            

            while len(counter.keys()) > 2:
                counter[fruits[start]] -= 1

                if counter[fruits[start]] == 0: 
                    del counter[fruits[start]]

                start += 1

        return max_sum
            
           



            












