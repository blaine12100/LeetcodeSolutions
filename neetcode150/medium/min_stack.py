"""class MinStack:

    def __init__(self):
        self.temp_arr = []
        self.min = 999999
        self.top_val = 0
        self.length_stack = 0

    def push(self, val: int) -> None:
        self.temp_arr[self.top_val] = val
        if val < self.min:
            self.min = val
        self.top_val += 1
        self.length_stack += 1

    def pop(self) -> None:
        #current_top =
        # if current_top == self.min:
        #    self.min = 999999
        del self.temp_arr[self.top_val]
        self.top_val -= 1

        # Pairwise comparison
        temp_top_val = (self.top_val - 2)
        if temp_top_val > 0 and (self.temp_arr[temp_top_val] < self.min):
            self.min = self.temp_arr[temp_top_val]
        else:
            self.min = self.temp_arr[self.top_val]

    def top(self) -> int:
        return self.temp_arr[-1]

    def getMin(self) -> int:
        return self.min
"""

# 29 / 31 test cases passed. THe logic of having each node have it's own min value does not make sense.


class MinStack:
    def __init__(self):
        self.temp_arr = []
        self.min = 999999
        self.temp_length = 0

    def push(self, val: int) -> None:
        self.temp_arr.insert(0, val)
        if val < self.min:
            self.min = val
        else:
            if self.min == 999999:
                self.min = val
        self.temp_length += 1

    def pop(self) -> None:
        # If we are deleting the current min, need to re-initialise the min again as it's no logner valid
        if self.temp_arr[0] == self.min:
            self.min = 999999
        del self.temp_arr[0]
        self.temp_length -= 1

        # Pairwise comparison (Only to be done if we have deleted the current min element)
        if self.min == 999999:
            if self.temp_length > 1:
                self.min = min(self.temp_arr[1], self.temp_arr[0])
            else:
                if self.temp_length == 0:
                    self.min = 999999
                else:
                    self.min = self.temp_arr[0]
        #else:
        #    if self.temp_length == 1:
        #        self.min = self.temp_arr[0]

    def top(self) -> int:
        return self.temp_arr[0]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
#obj.push(512)
current_top = obj.top()
print(current_top)
obj.pop()
current_min = obj.getMin()
print(current_min)
obj.pop()
current_min = obj.getMin()
print(current_min)
obj.pop()
obj.push(2147483647)
current_top = obj.top()
print(current_top)
current_min = obj.getMin()
print(current_min)
obj.push(-2147483648)
current_top = obj.top()
print(current_top)
current_min = obj.getMin()
print(current_min)
obj.pop()
current_min = obj.getMin()
print(current_min)
#current_min = obj.getMin()
#print(current_min)
#current_top = obj.top()
##print(current_top)
#obj.pop()
#current_min = obj.getMin()
#print(current_min)

# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top",
# "getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
# ["MinStack","push","push","push","push","pop","getMin","pop","getMin","pop","getMin"]
# [[],[512],[-1024],[-1024],[512],[],[],[],[],[],[]]
# ["MinStack","push","push","push","getMin","top","pop","getMin"]
#temp_cases = ["MinStack","push","push","push","getMin","pop","top","getMin"]
