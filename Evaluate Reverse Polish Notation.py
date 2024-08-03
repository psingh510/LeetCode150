tokens = ["1","2","+","3","*","4","-"]
stack = []
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+','*','-','/']:
                stack.append(i)

            else:
                last_elm = int(stack.pop())
                sec_last = int(stack.pop())
                if i == '+':
                    stack.append(sec_last+last_elm)
                elif i == '*':
                    stack.append(sec_last*last_elm)
                
                elif i == '-':
                    stack.append(sec_last-last_elm)

                elif i == '/':
                    stack.append(sec_last/last_elm)
        return int(stack[-1])
