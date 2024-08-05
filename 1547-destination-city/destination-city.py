class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        # create graph {london: 1, NewYork: 1, Lima:1, SaoPaulo:0}

        # out, and in

        # out_paths = defaultdict()
        # in_paths = defaultdict()

        # for start, end in enumerate(paths):
        #     if out_paths.get(start) == 0:
        #         out_paths[start] = 1
            
        #     else:
        #         out_paths[start] += 1
        
        # print(f'dict {out_paths}')


        out = set()

        for start, end in paths:
            out.add(start)
        
        
        for start, end in paths:
            if end not in out:
                return end
        
        

            


