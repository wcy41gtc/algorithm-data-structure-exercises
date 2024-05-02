# Balanced Parentheses Exercise
# In this exercise you are going to apply what you learned about stacks with
# a real world problem. We will be using stacks to make sure the parentheses 
# are balanced in mathematical expressions such as: ((3^2 + 8)*(5/2))/(2+6)
# In real life you can see this extend to many things such as text editor 
# plugins and interactive development environments for all sorts of bracket 
# completion checks. 

# Take a string as an input and return True if it's parentheses are balanced or 
# False if it is not. 

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    stack = Stack()
    for _ in equation:
        if _ == "(":
            stack.push(_)
        if _ == ")":
            if stack.size() !=0:
                stack.pop()
            elif stack.size() == 0:
                return False
    if stack.size() == 0:
        return True
    else:
        return False
    
# Test
def test():
    print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
    print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
if __name__ == '__main__':
    test()