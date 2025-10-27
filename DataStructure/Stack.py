#common stack functions
#push(item): push item to the top of the stack
#pop () remove and return the top item
#peek(): return the top item without removing it 
#is_empty(): return true if stack is empty

#Stack follows the Last In First Out (LIFO) principle
class Stack:
    def __init__(self):
        #Constructor
        self.items = []

    def isEmpty(self):
        return not self.items

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items) # for printing the items of the stack, without this it will print the object location instead

def reverse_string(my_string):
    # Use the "accumulator pattern."
    # Start with an "empty bucket" of the right data type,
    # and build the solution by filling the bucket within a loop.
    reversed_string = ""

    # Create a new stack
    stack = Stack()

    # Iterate through my_string and push the characters onto the stack
    for char in my_string:
        stack.push(char)

    # Use a while loop with the exit condition that the stack is empty.
    # Within this loop, update reversed_string with characters popped off the stack.
    while not stack.isEmpty():
        reversed_string+=stack.pop()
    # Return the result
    return reversed_string


if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.isEmpty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushing 1,2,3:", stack)
    print("Top item is:", stack.peek())
    print("Stack size is:", stack.size())
    print("Popped item is:", stack.pop())
    print("Stack after popping an item:", stack)

    # can be used for reversing a string
    string = "Hello, World!"
    reversed_result = reverse_string(string)
    print("Reversed string is:", reversed_result)

