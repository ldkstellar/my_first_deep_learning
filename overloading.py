# 연산자 오버로딩
class SquareNumbers:
    def __init__(self,my_list):
        self.my_list = my_list # initialize
    def __getitem__(self,idx): #indexing
        return self.my_list[idx] + 10
    def __len__(self): #len
        return len(self.my_list)
squares = SquareNumbers([0,1,2,3,4])
for i in range(len(squares)):
    print(squares[i],end=" ")
    
        
        