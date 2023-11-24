class Solution:
    def simplifyPath(self, path: str) -> str:
        # three cases --> replace double slash with single slash
        # if .. then pop . / then while str[i] not /: pop.
        # /./ is just the current path directory
        # ... is considered a name
        
        # only pop at end if / or .
        res_stack = []

        for s in path:
            if res_stack and s == '/':
                if res_stack[-1] == '/':
                    continue
                elif len(res_stack) > 2 and res_stack[-1] == '.' and res_stack[-2] == '.' and res_stack[-3] == '.':
                    res_stack.append(s)
                    continue
                elif len(res_stack) > 2 and res_stack[-1] == '.' and res_stack[-2] == '.' and res_stack[-3] == '/':
                    res_stack.pop()
                    res_stack.pop()
                    if len(res_stack) > 1:
                        res_stack.pop()
                        while res_stack[-1] != '/':
                            res_stack.pop()
                    continue
                elif res_stack[-1] == '.' and res_stack[-2] == '/':
                    res_stack.pop()
                    continue
                else:
                    res_stack.append(s)
            else:
                res_stack.append(s)

        # /...
        # /..
        # /.
        # /home/
        if len(res_stack) > 1:
            if len(res_stack) > 2:
                if res_stack[-1] == '.' and res_stack[-2] == '.' and res_stack[-3] == '.':
                    return "".join(res_stack)
                if res_stack[-1] == '.' and res_stack[-2] == '.' and res_stack[-3] == '/':
                    print(res_stack)
                    res_stack.pop()
                    res_stack.pop()
                    if len(res_stack) > 1:
                        res_stack.pop()
                        while res_stack[-1] != '/':
                            res_stack.pop()
            if len(res_stack) > 2:
                if res_stack[-1] == '.' and res_stack[-2] == '.' and res_stack[-3] != '/':
                    return "".join(res_stack)    
            if res_stack[-1] == '.':
                while res_stack[-1] != '/':
                    res_stack.pop()
            if len(res_stack) > 1 and res_stack[-1] == '/':
                res_stack.pop()
        return "".join(res_stack)
                

                
        

        
