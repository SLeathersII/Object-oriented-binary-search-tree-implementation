#!/usr/bin/env python
# coding: utf-8

# # Card.py
# The Card.py file will contain the definition of a Card class. The Card class will hold information about the cards (suit and rank), and for simplicity, it will also double as a node in our PlayerHand BST. We will define the Card attributes as follows:
# 
# * suit - string value that distinguishes what suit that card is: C (club), D (diamond), H (heart), or S (spade)
# * rank - string value to distinguish the rank of the card (in ascending value): A (ace), 2, 3, 4, 5, 6, 7, 8, 9, J (Jack), Q (Queen), K (King). Assume there is no Joker
# * parent - a reference to the parent node of a card in the BST, None if it has no parent (aka, it is the root)
# * left - a reference to the left child of a card in the BST, None if it has no left child
# * right - a reference to the right child of a card in the BST, None if it has no right child
# * count - an integer representing the amount of times this card appears in the BST. 1 by default, but it can be greater since your implementation should support duplicate cards
# 
# You will write a constructor that allows the user to construct a Card object by passing in values for the suit and rank. Your constructor should also create the count attribute and initialize it to 0, as well as create the parent, left, and right attributes initialized to None.

# In[51]:


class Card:
    
    def __init__(self, suit, rank, left = None, right = None, parent = None):
        # try and capitilize suit
        if type(suit) == str:
            self.suit = suit.upper()
        # Could limit only C, D, H, S but will assume they are the only inputs
        
        if type(rank) == str:
            self.rank = rank.upper()   
        
        # could change ranks of letters to numbers for sorting but would affect getRank output which may fail test
        # Cap rank if str
        
        #try:
            #self.rank = int(rank) # store as integer for comparisons later
        #except ValueError:
            #self.rank = rank.upper() # capitlize string if not able to be integer
        #### The above method created too many errors with put_() comparing strings and integers    
         
        # Binary search tree node items
        self.left = left
        self.parent = parent
        self.right = right
        self.count = 1 # 1 by default, should increment up if duplicates found 
        
        # create sorted rank function to use for sorting/ put_()
        if self.rank == 'A':
            self.rankSort = 1
        elif self.rank == 'J':
            self.rankSort = 11
        elif self.rank == "Q":
            self.rankSort = 12
        elif self.rank == 'K':
            self.rankSort = 13
        else:
            self.rankSort = int(self.rank) # convert non face cards to integers
        
    # getter/ setter methods
    def getSuit(self):
        return self.suit
    def setSuit(self, suit):
        self.suit = suit
        
    def getRank(self):
        return self.rank
    def setRank(self, rank):
        self.rank = rank
        
    def getCount(self):
        return self.count
    def setCount(self, count):
        # used to count duplicates
        self.count = count
        
    def getParent(self):
        return self.parent
    def setParent(self, parent):
        self.parent = parent
        
    def getLeft(self):
        return self.left
    def setLeft(self, left):
        self.left = left
        
    def getRight(self):
        return self.right
    def setRight(self, right):
        self.right = right
        
    # overload string settings
    def __str__(self):
        """
        For example, it should return the string "S A | 1\n" 
        if the Card is an Ace of Spades and has no duplicates
        """
        return f'{self.suit} {self.rank} | {self.count}\n'
    
    def __lt__(self, other):
        """ 
        Order by rank, then suit
        treat A (Ace) as the smallest, and K (King) as the largest.
        C (Club) < D (Diamond) < H (Heart) < S (Spade)
        """ 
        if self.rank != other.rank:  # Ensures the ranks are not the same ## Could consider using 'not in' if we assigned strings to caps to avoid various errors
            return self.rankSort < other.rankSort # use sorted method
        
        else: # self and other are equivalent in rank, sort by class: Less than | Note: if they are equal it should return false
            if self.suit == 'S':
                return False # Spade is the highest
            elif other.suit == 'S': # would already be false if both are Spades
                return True
            elif other.suit == 'C':
                return False # Club is the lowest
            elif self.suit == 'C': # would already be false if both are clubs
                return True
            # if both are none of the values above,  'D' < 'H' == True in python: False if the same
            elif self.suit != 'S' and self.suit != 'C' and other.suit != 'S' and other.suit != 'C':
                return self.suit < other.suit
            # note: a simple else may be sufficient above
            
    def __eq__(self, other):
        if other == None:
            return False # Card should never equal Nonetype, also need this line to avoid error
            # further for the above what if != be called? 
        
        elif self.rank == other.rank and self.suit == other.suit:
            return True
        else:
            return False
        
       ############################################### 
        
     # Methods used in BST 
    def hasLeftChild(self):
        return self.left # not a boolearn, returns None or item
    
    def isLeftChild(self):
        return self.parent and self.parent.left == self # checks it has a parent and that it is the left child 
    
    def hasRightChild(self):
        return self.right
    
    def isRightChild(self):
        return self.parent and self.parent.right == self
    
    def isLeaf(self):
        return not (self.right or self.left) # returns True if both are None types 
    
    def hasBothChildren(self):
        return self.right and self.left # opposite of above
    
    # if either is something that is not None, returns True (has a child) 
    def hasAnyChildren(self): 
        return self.right or self.left
    
    def replaceNodeData(self, key, value, lc, rc):
        self.rank = key
        self.suite = value
        self.left = lc
        self.right = rc
        
    
    # BST methods below
    
    def findSuccessor(self):
        succ = None
        # Check if node has a right subtree
        if self.hasRightChild():
            # Traverse through left children (min)
            succ = self.right.findMin()
        else:
            if self.parent: # ensure parent is not None
                if self.isLeftChild():
                    succ = self.parent
                        
                else: # has no right subtree, is right child 
                    self.parent.right = None
                    succ = self.parent.findSuccessor()
                    self.parent.right = self # resets child assignment
        return succ    

    
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current
    
    def spliceOut(self):
        # Case 1:
        # If node to be removed is leaf, set parent's left or right child ref to None
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        # Case 2: not a leaf node
        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeftChild(): # if it has and right child, and is a left child, set link
                    self.parent.left = self.right
                    
                else: # does not have right child
                    self.parent.right = self.right
                self.right.parent = self.parent # set deleted nodes child as parent
                
    
        


# k = Card('s','2')
# l = Card('s','3')
# n = Card('s','a')
# m = Card('s','k')
# a = Card('s','j')
# b = Card('c','q')
# v = Card('h','2')
# f = Card('h','2')

# In[37]:




