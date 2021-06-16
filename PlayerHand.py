#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import import_ipynb
from Card import Card


# # PlayerHand.py
# The PlayerHand.py file will contain the definition of a PlayerHand class. This will keep track of the cards a player has in their hand, implemented as a BST. The PlayerHand will manage Card objects based on their suit and rank.
# 
# * __init__(self) - the constructor for the PlayerHand will simply initialize the empty BST.
# In addition to the construction of the BST in this class, the following methods are required to be implemented:
# 
# * getTotalCards(self) - returns the total number of cards in hand
# * getMin(self) - returns the card with the lowest value from the player’s hand. Returns None if there is no card in the hand
# * getSuccessor(self, suit, rank) - attempts to finds the Card with the suit and rank, and returns the card with the next greatest value Returns None if there is no card with the specified suit and rank, or if the Card is the maximum and has no successor
# * put(self, suit, rank) - this adds a card with the specified suit and rank to the BST. If that Card already exists in the BST, increment the count for that Card
# * delete(self, suit, rank) - attempts to find the Card with the specified suit and rank, and decrements the Card count. If the count is 0 after decrementing the count, remove the node from the BST entirely. Returns True if the Card was successfully removed or decremented, and False if the card is not present in the BST
# * isEmpty(self) - returns True if there are no cards in the BST and returns False otherwise
# * get(self, suit, rank) - attempts to find the Card with the specified suit and rank, and returns the Card object if it exists. Otherwise, return None
# * inOrder(self) - returns a string with the in-order traversal of the BST. Printing the in-order traversal should help check that the cards are in the correct order in the tree
# * preOrder(self) - returns a string with the pre-order traversal of the BST. BSTs with the same structure should always have the same pre-order traversal, so this can be used to verify that everything was inserted correctly

# In[31]:


class PlayerHand:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def getTotalCards(self):
        return self.size
    
    def getMin(self):
        # returns the card with the lowest value
        current = self.root
        
        # prevent None.hasLeftChild() error
        if current != None:
            while current.hasLeftChild(): # keeps recursing while there is a left child
                current = current.left
        return current
    
    def isEmpty(self):
        if self.size > 0:
            return False
        else:
            return True

    
    def put(self, suit, rank): # insert (rank, val) was initial coding need to flip
        
        # can use loop but we will use recursion
        if self.root: # if None, evaluates to False and won't execute
            self._put(suit, rank, self.root) # helper function, uses root to traverse structure
        else:
            self.root = Card(suit, rank) # 
        self.size += 1 # increment up by one since we added a value
        # Need to increment card count if they are the same
        
    def _put(self, suit, rank, currentNode):
        # Need to reassign rank values to properly sort with node value
        if type(rank) == str: 
            if rank.upper() == 'A': # may need rank.upper() depending on put inputs
                rankSort = 1
            elif rank.upper() == 'J':
                rankSort = 11
            elif rank.upper() == "Q":
                rankSort = 12
            elif rank.upper() == 'K':
                rankSort = 13
            else: 
                rankSort = int(rank) # convert rank to integer for sorting
        
        
        # Need a check if new node exists to increment previous node
        
        if rank.upper() == currentNode.rank and suit.upper() == currentNode.suit: # may need to make use of .upper() to ensure equality
            currentNode.count += 1 # increment count up by 1 if card is in Hand, no need for new node
        
        # ensure they are not the same value as it will try and erroneously place in the wrong subtree
        elif rank.upper() == currentNode.rank and suit.upper() != currentNode.suit: # need to sort by suit  C (Club) < D (Diamond) < H (Heart) < S (Spade)
            if suit.upper() == 'C': # inserted element is less than
                
                # check if left child exists: won't execute if None
                if currentNode.hasLeftChild():
                    self._put(suit, rank, currentNode.left) # steps down to left child and recurses 
                
                # if the above is None ( No left child) then we assign the left child and set it's parent as the current node
                else:
                    currentNode.left = Card(suit, rank, parent = currentNode) # sets the parent
                    
                    
            elif suit.upper() == 'S': # inserted element is greater than should go to right child
                if currentNode.hasRightChild():
                    self._put(suit, rank, currentNode.right)
                
                else:
                    currentNode.right = Card(suit, rank, parent = currentNode)
                    
            # do the same for CurrentNode but reverse tree branch assignments
            elif currentNode.suit == 'C': # should already be made into caps, will go to right subtree
                if currentNode.hasRightChild():
                    self._put(suit, rank, currentNode.right)
                
                else:
                    currentNode.right = Card(suit, rank, parent = currentNode)
                    
            elif currentNode.suit == 'S': # go to left tree
                # check if left child exists: won't execute if None
                if currentNode.hasLeftChild():
                    self._put(suit, rank, currentNode.left) # steps down to left child and recurses 
                
                # if the above is None ( No left child) then we assign the left child and set it's parent as the current node
                else:
                    currentNode.left = Card(suit, rank, parent = currentNode) # sets the parent
                    
            else: # neither input suit nor currentNode.suit can be the above suits (S C)
                # thus using 'D' < 'H' == True in python
                if suit.upper() < currentNode.suit:
                    # check if left child exists: won't execute if None
                    if currentNode.hasLeftChild():
                        self._put(suit, rank, currentNode.left) # steps down to left child and recurses 
                
                    # if the above is None ( No left child) then we assign the left child and set it's parent as the current node
                    else:
                        currentNode.left = Card(suit, rank, parent = currentNode) # sets the parent
            
                else: # input suit is greater than current node
                    if currentNode.hasRightChild():
                        self._put(suit, rank, currentNode.right)
                
                    else:
                        currentNode.right = Card(suit, rank, parent = currentNode)
                    
                    
                    
                    
        # Use rankSort to find place to put
        elif rankSort < currentNode.rankSort:
            # try to assign to the left
            
            # check if left child exists: won't execute if None
            if currentNode.hasLeftChild():
                self._put(suit, rank, currentNode.left) # steps down to left child and recurses 
                
            # if the above is None ( No left child) then we assign the left child and set it's parent as the current node
            else:
                currentNode.left = Card(suit, rank, parent = currentNode) # sets the parent
                
        # try and assign to right child    
        else:
            if currentNode.hasRightChild():
                self._put(suit, rank, currentNode.right)
                
            else:
                currentNode.right = Card(suit, rank, parent = currentNode)
                
                
                
                
                
                
                
                
                
                
                
                
    def get(self, suit, rank): # returns card if it exists
        # if we are at root
        if self.root:
            res = self._get(suit, rank, self.root) # walk down
            
            if res:
                return res # want to return the card
            else:
                return None # None used as sentinal value to avoid using an exception if the value does not exist
        else:
            return None # returns none if no tree to traverse
            
            
            
            
    def _get(self, suit, rank, currentNode):
        
        # Create dummy card to use for equality check
        dummycard = Card(suit, rank)
        
        
        if not currentNode: # is not none, traversed the tree and have not found it
            return None
        elif currentNode == dummycard:
            return currentNode # in the above function res is this node
            
        elif dummycard < currentNode: # continue looking for node, use dummycard instead of values to avoid missing our card
            return self._get(suit, rank, currentNode.left)
        else:
            return self._get(suit, rank, currentNode.right)
        
        
        
        
        
            
    def getSuccessor(self, suit, rank):
        '''
        attempts to finds the Card with the suit and rank, 
        and returns the card with the next greatest value Returns None 
        if there is no card with the specified suit and rank, 
        or if the Card is the maximum and has no successor
        '''
        succ = None # assume we can't find successor
        dummycard = Card(suit, rank)
        
        # make sure it is not the only element (Max)
        if self.size > 1:
            
            # case 1: card doesn't exist
            if self.get(suit, rank): # returns None if it doesn't exists and does not execute
                # if it has a rightsubtree
                if self.get(suit, rank).hasRightChild():
                    succ = self.get(suit, rank).right
                    # traveres through the leftsubtree of rightchild
                    while succ.hasLeftChild():
                        succ = succ.left # traverse left tree to find succ
                        
                
                # does not have rightsubtree
                else:           
                    if self.get(suit,rank).parent: # if the card sought has a parent: only other place to find sucessor is if you are the rightchild
                        if self.get(suit,rank).isLeftChild: # if it is a left child
                            succ = self.get(suit,rank).parent
                        else: # is right child, no right subtree
                            #
                            self.get(suit,rank).parent.right = None
                            succ = self.get(suit, rank).parent.findSuccessor() # recurse until has rightsubtree or is leftChild
                            self.get(suit, rank).parent.right = self.get(suit, rank) # reset as child
                    
               
        return succ    
    
    
    
    
    
            
    def delete(self, suit, rank):
        """
        attempts to find the Card with the specified suit and rank,
        and decrements the Card count.
        If the count is 0 after decrementing the count, 
        remove the node from the BST entirely. Returns True if the Card was 
        successfully removed or decremented, and False if the card is not
        present in the BST
        
        """
        # default dummy to not finding anything
        dummy = False
        dummycard = Card(suit, rank)
        if self.size > 1: # ensure tree has objects to look for
            nodeToRemove = self._get(suit, rank, self.root)
            if nodeToRemove: # executes if not None/ exists in tree
                self.remove(nodeToRemove) # remove modifies tree
                self.size = self.size - 1
                dummy = True
            else:
                dummy = False # could not be found
                
        elif self.size == 1 and dummycard == self.root: # card is root
            self.root = None
            self.size = self.size - 1
            dummy = True
        else:
            dummy = False # there are no objects in hand     
            
        return dummy   # returns False if nothing found
            
            
            
    # Used to remove node in BST
    def remove(self, currentNode):
        ## Need to increment counts and only remove node if count is 0
        if currentNode.count > 1:
            currentNode.setCount(currentNode.count - 1) # increments count down by 1
            
        elif currentNode.count == 1: # count is equal to 1, need to remove node
            # Case 1: Node to remove is a leaf
            if currentNode.isLeaf(): # if true
                if currentNode == currentNode.parent.left:
                    currentNode.parent.left = None
                else:
                    currentNode.parent.right = None
                
            # Case 3: Node to remove has both chilren
            elif currentNode.hasBothChildren():
                # Need to find the successor, remove successor, and replace currentNode with successor's rank and suit
                succ = currentNode.findSuccessor()
                succ.spliceOut() # deleting the node from the tree
                currentNode.rank = succ.rank
                currentNode.suit = succ.suit
                currentNode.count = succ.count
            
            # Case 2: Node to remove has one child
            else:
                # Node has left
                if currentNode.hasLeftChild():
                    if currentNode.isLeftChild():
                        currentNode.left.parent = currentNode.parent
                        currentNode.parent.left = currentNode.left # set parents left child to left child
                        
                    elif currentNode.isRightChild():
                        currentNode.left.parent = currentNode.parent
                        currentNode.parent.right = currentNode.left
                        
                    else: # currentNode is the Root
                        currentNode.replaceNodeData(currentNode.left.rank, currentNode.left.suit, currentNode.left.left, currentNode.left.right)
                    
                # Node has rightChild
                else:
                    if currentNode.isLeftChild():
                        currentNode.right.parent = currentNode.parent
                        currentNode.parent.left = currentNode.right
                    elif currentNode.isRightChild():
                        currentNode.right.parent = currentNode.parent
                        currentNode.parent.right = currentNode.right
                    else:
                        currentNode.replaceNodeData(currentNode.right.rank, currentNode.right.suit, currentNode.right.left, currentNode.right.right)
                    
                    
                    
                    
                    
    def inOrder(self):
        
        # should start at the root, put root of hand in to parse
        node = self.root
        ret = ""
        ret += self.inOrderHelper(node)
        
        return ret
    
    
    def inOrderHelper(self, node):
        ret = ''
        if node != None:
            ret += self.inOrderHelper(node.left)
            ret += str(node) + ""
            ret += self.inOrderHelper(node.right)
        return ret
    
    def preOrder(self):
        # start at the root of the hand for algo to work
        node = self.root
        ret = ''
        ret += self.preOrderHelper(node)
        
        return ret
    
    def preOrderHelper(self, node):
        ret = ''
        if node != None:
            ret += str(node) + ""
            ret += self.preOrderHelper(node.left)
            ret += self.preOrderHelper(node.right)
        return ret


# In[ ]:





# In[19]:





# In[18]:





# hand = PlayerHand()
# hand.put('D', '9')
# hand.put('S', 'K')
# hand.put('S', '2')
# hand.put('C', 'q')
# hand.put('H', '7')
# hand.put('S', 'K')
# hand.put('C', 'K')

# In[28]:





# hand = PlayerHand()
# hand.put('h','9')
# hand.put('d','9') # left child
# hand.put('s','10')

# print(hand.preOrder())

# In[ ]:





# In[18]:





# In[19]:





# In[21]:





# In[ ]:





# In[ ]:




