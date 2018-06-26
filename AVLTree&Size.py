# AVL Tree that also stores its size

class Node:
    def __init__(self, val):
        self.key = val; self.left = None; self.right = None

class SizedAVL:
    def __init__(self):
        self.node = None; self.height = -1; self.balance = 0; self.size = 0
    
    def insert(self, key):
        N = Node(key)
        if self.node == None:
            self.node = N; self.node.left = AVL(); self.node.right = AVL()
        elif key < self.node.key: self.node.left.insert(key)
        elif key > self.node.key: self.node.right.insert(key)
        self.rebalance()

    def delete(self, key):
        if self.node == None: return
        if self.node.key == key:
            if not self.node.left.node and not self.node.right.node: self.node = None
            elif not self.node.left.node: self.node = self.node.right.node
            elif not self.node.right.node: self.node = self.node.left.node
            else:
                suc = self.node.right.node  
                while suc and suc.left.node: suc = suc.left.node
                if suc: self.node.key = suc.key; self.node.right.delete(suc.key)
        elif key < self.node.key: self.node.left.delete(key)
        elif key > self.node.key: self.node.right.delete(key)
        self.rebalance()

    def rebalance(self):
        self.update_heights(False); self.update_balance(False); self.update_size(False)
        while not -1 <= self.balance <= 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights(); self.update_balance(); self.update_size()
                self.rotate_right()
            elif self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.update_heights(); self.update_balance()
                self.rotate_left()
            self.update_heights(); self.update_balance(); self.update_size()
        
    def update_heights(self, recursive=True):
        if self.node: 
            if recursive: 
                if self.node.left: self.node.left.update_heights()
                if self.node.right: self.node.right.update_heights()
            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else: self.height = -1
    
    def update_balance(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left: self.node.left.update_balance()
                if self.node.right: self.node.right.update_balance()
            self.balance = self.node.left.height - self.node.right.height
        else: self.balance = 0

    def update_size(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left: self.node.left.update_size()
                if self.node.right: self.node.right.update_size()
            self.size = self.node.left.size + self.node.right.size + 1
        else: self.size = 0
    
    def rotate_right(self):
        new_root = self.node.left.node; new_left_sub = new_root.right.node
        old_root = self.node; self.node = new_root
        old_root.left.node = new_left_sub; new_root.right.node = old_root

    def rotate_left(self):
        new_root = self.node.right.node; new_left_sub = new_root.left.node
        old_root = self.node; self.node = new_root
        old_root.right.node = new_left_sub; new_root.left.node = old_root
    
    def inorder(self):
        # Use this to debug
        result = []
        if not self.node: return result
        result.extend(self.node.left.inorder())
        L = self.node.left.node.key if self.node.left.node else None
        R = self.node.right.node.key if self.node.right.node else None
        result.append((self.node.key, L, R, self.size))
        result.extend(self.node.right.inorder())
        return result