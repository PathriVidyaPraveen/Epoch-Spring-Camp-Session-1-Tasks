import numpy as np
class Node :
    def __init__(self,value,children=[],op=None,op_args=None):
        self.value = np.array(value) 
        self.children = children
        self.op = op
        self.op_args = op_args if op_args else []
        self.grad = 0 #Bonus task
    # Operator overloading
    def __add__(self,second):
        second = second if isinstance(second, Node) else Node(second)
        return Node(value = self.value + second.value,children = [self,second],op="add")
    def __sub__(self,second):
        second = second if isinstance(second, Node) else Node(second)
        return Node(value = self.value - second.value , children = [self,second], op = "sub")
    def __mul__(self,second):
        second = second if isinstance(second, Node) else Node(second)
        return Node(value = self.value * second.value , children = [self,second] , op = "mul")
    def __truediv__(self,second):
        second = second if isinstance(second, Node) else Node(second)
        return Node(value = self.value/second.value , children = [self,second] , op = "div")
    def __pow__(self,second):
        second = second if isinstance(second, Node) else Node(second)
        return Node(value = self.value ** second.value , children = [self,second] , op = "pow")
    def __repr__(self):
        return "Node(value={}, operation={})".format(self.value,self.op)
    # Bonus Task
    def backward(self,grad=1):
        # Should impleement gradients recursively as mentioned in question
        self.grad += grad
        if self.op == "add":
            # Gradient is passed unchanged to both operands
            self.children[0].backward(grad)
            self.children[1].backward(grad)
        elif self.op == "sub":
            # Left operand receives grad and right operand receives -grad
            self.children[0].backward(grad)
            self.children[1].backward(-1*grad)
        elif self.op == "mul":
            # Use product rule to back propagate thee gradients
            self.children[0].backward(self.children[1].value * grad)
            self.children[1].backward(self.children[0].value * grad)
        elif self.op == "div":
            # Uses the quotient rule to backpropagate the gradients
            self.children[0].backward(grad/self.children[1].value)
            self.children[1].backward(-1*grad*self.children[0].value / ((self.children[1].value)**2))
        elif self.op == "pow" :
            x = self.children[0].value
            y = self.children[1].value
            self.children[0].backward(grad*y*(x**(y-1)))
            if x > 0 :
                self.children[1].backward(grad*(x**y)*(np.log(x)))
        


# x = Node(1)
# y = Node(2)
# z = Node(3)

# a = x + y
# b = a * z

# print("a :  ",a)
# print("b :  ", b)

# print("Children of a :  {}".format(a.children))
# print("Children of b :  {}".format(b.children))

# Verify the correctness of the gradient calculation 
a = Node(2) 
b = Node(3) 

c = (a * 2) + b  
d = c ** 3       

d.backward()

print(f"Gradient of d with respect to a: {a.grad}")
print(f"Gradient of d with respect to b: {b.grad}")
print(f"Gradient of d with respect to c: {c.grad}")




