    

def brackets(s):
    
    dic ={ "{":"}", "[":"]", "(":")"}

    stack =  []
            
    if len(s) < 2:
                return False

    for char in s:
        #check is char is opening bracket
        if char in dic.keys():
            stack.append(char)

        # if not check if closing bracket matches top of stack
        elif len(stack) > 0 and (char == dic[stack[-1]]) :
            stack.pop()

        # if closing bracket does not match, then the brackets are not correct, therefore return False
        else:
            return False


        # if the stack is empty at the end, then all the brackets correctly match
    if len(stack) == 0:
        return True



print(brackets("){"))
