class prioqueue:
    def __init__(self):
    #I want to start root at index 1
        self.arr = [None]
        self.size = 0
    def left_child(self,idx):
    #returns index of left child
        return idx*2
    def right_child(self,idx):
    #returns index of right child
        return idx*2+1
    def parent(self,idx):
    #returns index of parent
        return idx//2
    def swap_nodes(self,a,b):
    #swaps the value of both indexes
        self.arr[a],self.arr[b]=self.arr[b],self.arr[a]

    def bob_down(self,idx):
    #bob down the selected idx if big
    #we want min at top
        left_idx=self.left_child(idx)#index of left child
        right_idx=self.right_child(idx)#index of right child
        if(left_idx>self.size):#if left child doesnt exist, then right doesnt exist too. just go home
            return
        elif(right_idx>self.size):#if right child doesn't exist, neither does left child's children, but go left
            left_val = self.arr[left_idx][1]#value of left child
            current_val = self.arr[idx][1]#value of current
            if(left_val<current_val):
                self.swap_nodes(left_idx,idx)
        else:#if both exists
            left_val = self.arr[left_idx][1]#value of left; number of monsters
            right_val = self.arr[right_idx][1]#value of right; number of monsters
            current_val = self.arr[idx][1]#value of child; number of monsters
            if(right_val < left_val):#if right is less than left, then evaluate if right is also less than current
                if(right_val < current_val):#if right is less, swap then repeat
                    self.swap_nodes(right_idx,idx)
                    self.bob_down(right_idx)
            else:#if either works, then evaluate if left is less than current
                if(left_val < current_val):#if left is less, swap then repeat
                    self.swap_nodes(left_idx,idx)
                    self.bob_down(left_idx)
    def bob_up(self,idx):
    #bob up the selected idx if smol
    #we want min at top
        parent_idx = self.parent(idx)#index of parent
        parent_val = self.arr[parent_idx][1]#value of parent
        current_val = self.arr[idx][1]#value of current index
        if(idx == 1):#if index is the root, then no parent
            return
        if(current_val < parent_val):#if smaller than parent
            self.swap_nodes(parent_idx,idx)#then swap
            
            if(parent_idx > 1):#if current val is not root
                self.bob_up(parent_idx)#bob up more
    def insert(self,val):
    #inserting elements
        self.size+=1#increment size
        idx=self.size#inserted element is last
        self.arr.append(val)#append tuple to end of array      
        if(idx>1):#if not root
            self.bob_up(idx)
    def get(self):
    #get the minimum, which is prolly on top
        self.swap_nodes(1,self.size)#swap with last node first
        result = self.arr.pop()#then store that last node on var and remove
        self.size-=1#then decrease size
        if(self.size>0):#if queue is not empty
            self.bob_down(1)#then bob down the first element
        return result#then return result

pq=prioqueue()
pq.insert((2,5))
pq.insert((4,15))
pq.insert((5,6))
print(pq.arr)