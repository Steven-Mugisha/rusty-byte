class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        list1_map = {}

        for i, exp in enumerate(list1):
            list1_map[exp] = i
        
        sum_tracker = float('inf')

        res = []

        for i in range(len(list2)):
            curr_exp = list2[i]
            if curr_exp in list1_map:
                if (list1_map[curr_exp] + i) < sum_tracker:
                    res = [curr_exp]
                    sum_tracker = list1_map[curr_exp] + i
                elif (list1_map[curr_exp] + i) == sum_tracker:
                    res.append(curr_exp)
                
                else: continue
        return res 


        