class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # "AABABBA",     
        # k = 1, map.keys() == 2, key minimum value: B: 1, >= k = 1, curr_max
        # {A:2, B:1} == 5

        counter = collections.defaultdict(int)
        l = 0
        curr_max = 0
        result = 0

        for r in range(len(s)):
            curr_max += 1
            counter[s[r]] += 1

            print(f"first {curr_max - max(counter.values())}, last {min(counter.values())}")

            while curr_max - max(counter.values()) > k:

                counter[s[l]] -= 1
                curr_max -= 1
                l += 1

            result = max(result, curr_max)
            
        return result


        
            








