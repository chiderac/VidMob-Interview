class Solution:
    def calculate(self, s: str) -> int:
        
        def valid(self, s): # method to check if string contains any alphabetic characters, if so raise value error and give invalid Input
            contains_alpha = any(t.isalpha() for t in s)
            if len(s) > 2 and contains_alpha:
                raise ValueError (" Invalid Input")
            return s

        # method to transform string:
        # remove space from string
        # check to see if ++ is seen through string and replace with +
        # check to see if -- is seen through string and replace with -
        # check to see if +- is seen through string and replace with +
        # for loop used to detect if there are any operators next to each other within string, if so raise Syntax error
        def transformation(self, s):
            s = valid(self, s)
            s = s.replace(' ', '')
            s = s.replace("++", "+") 
            s = s.replace("--", "+") 
            s = s.replace("+-", "+") 
            operator = ['+', '-', '/', '*']
            for c1,c2 in zip(s[:-1],s[1:]):
                if c1 in operator and c2 in operator:
                    raise SyntaxError
            return s
        
        
        # depth first search implementation 
        def dfs(idx):
            result = transformation(self, s)
            stack = []
            operation = '+'
            curr_num = ''
            def renew_stack(op, v):
                v = float(v)
                
                #if op is +, append v to stack 
                if op == '+':
                    stack.append(v)
                
                
                #if op is -, change v to negative and append to stack 
                elif op == '-':
                    stack.append(-v)
                    
                #if op = *, pop the last element from the stack and multiply the last element by v.
                elif op == '*':
                    stack.append(stack.pop() * v)
                
                #if op = /, pop the last element from the stack and divide the last element by v. 
                #Once evaluated append the result into the stack
                elif op == '/':
                    stack.append(float(stack.pop() / v))
            
            
            #iterate through string (s), and identify elements by index
            #if program encounters an element that is a digit or a decimal point add to variable curr_num         
            while idx < len(result):
                char = result[idx]
                if char.isdigit() or char == '.':
                    curr_num += char
                
                #if it encounters an operator and it has seen an operator without seeing a new number add 
                elif char in {"+", "-", "/", "*"}:
                    if curr_num == '':  
                        curr_num += char
                    
                    #else use method renew_stack that will go back reset the op and curr_num 
                    else:
                        renew_stack(operation, curr_num)
                        curr_num = ''
                        operation = char
                
                # if open parentheses are encountered dfs method is applied to expression inside of itself until the closed parenthesis is found
                # evaluation of stack made from expression in parethensis is done and the result used in the wider evaluation of original expression
                elif char == '(':
                    curr_num, nidx = dfs(idx+1)
                    idx = nidx - 1
                elif char == ')':
                    renew_stack(operation, curr_num)
                    return str(sum(stack)), idx+1
                idx += 1
            renew_stack(operation, curr_num)
            return sum(stack) # evaluate stack  
        return dfs(0)
  
# I have tested using the examples and the answers come out not normalized for example:  1+2 = 3.0 - I am so sorry I should have changed this

if __name__ == '__main__':
    S = Solution()  

    p1 = '1+2'
    r1 = S.calculate(p1)
    print("{} is {}".format(p1, r1))
        

    p2 = '21*(1+1)'
    r2 = S.calculate(p2)
    print("{} is {}".format(p2, r2))


    p3 = '21.1+2'
    r3 = S.calculate(p3)
    print("{} is {}".format(p3, r3))
        
    p4 = '4-2*3.5'
    r4 = S.calculate(p4)
    print("{} is {}".format(p4, r4))

    p5 = '(4-2)*3.5'
    r5 = S.calculate(p5)    
    print("{} is {}".format(p5, r5))

    p6 = "-.32 /   .5"
    r6 = S.calculate(p6)
    print("{} is {}".format(p6, r6))

    p7="-5+-8--11*2"
    r7=S.calculate(p7)
    print("{} is {}".format(p7, r7))

    p8 ="(2-4)*5/(4+3)"
    r8=S.calculate(p8)
    print("{} is {}".format(p8, r8))

    p9="2-+*4"
    r9=S.calculate(p9)
    print("{} is {}".format(p9, r9))

    p11 ="19 + cinnamon"
    r11=S.calculate(p11)
    print("{} is {}".format(p11, r11))