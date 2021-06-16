#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import import_ipynb
from Card import Card
from PlayerHand import PlayerHand


# In[63]:


def test_Card():
    
    k = Card('s','2')
    l = Card('s','3')
    n = Card('s','a')
    m = Card('s','k')
    a = Card('s','j')
    b = Card('c','q')
    v = Card('h','2')
    f = Card('h','2')
    # less than
    assert (k < l) == True
    assert (v < l) == True
    assert (v < k) == True # ranked by suit
    assert (a < b) == True
    assert (n < k) == True
    assert (n < b) == True
    
    # ==
    assert v == f
    
    # get
    assert (f.getCount() == 0) == False
    assert (f.getRank() == '2') == True
    assert (f.getSuit() == 'H') == True


# In[69]:


def test_PlayerHand():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    
    # test total cards
    assert hand.size == 7
    assert hand.delete('s','k') == True
    assert hand.size == 6
    assert hand.delete('s','k') == True
    assert hand.delete('s','k') == False
    assert hand.delete('s','j') == False
    assert hand.size == 5
    
    # delete leaf node
    hand = PlayerHand()
    hand.put('h','9')
    hand.put('d','9') # leaf
    hand.put('s','10') # leaf
    assert hand.delete('s','10') == True
    assert hand.delete('d','9') == True
    
    # is empty
    assert hand.delete('h','9') == True # last item
    assert hand.isEmpty() == True
    
    # delete node with 2 children
    hand = PlayerHand()
    hand.put('h','9')
    hand.put('d','9') # leaf
    hand.put('s','10') # leaf
    assert hand.delete('h','9') == True # delete root node/ two children
    
    
    
    # put left children
    hand = PlayerHand()
    hand.put('h','9')
    hand.put('d','9') # left child
    hand.put('s','10') # right child
    assert hand.get('d','9').isLeftChild() == True
    # put right child
    assert hand.get('s','10').isRightChild() == True
    
    
    # 


# test_PlayerHand()
# test_Card()

# hand = PlayerHand()
# hand.put('h','9')
# hand.put('d','9') # leaf
# hand.put('s','10') # leaf
# hand.delete('d','9')
# print(hand.root)

# hand = PlayerHand()
# hand.put('H', '7')
# hand.put('D', '5')
# hand.put('S', '10')
# hand.put('S', '3')
# hand.put('C', '6')
# hand.put('S', '8')
# hand.put('C', 'K')
# hand.put('h','7') # make duplicate to see what happens when deleted

# print(hand.root)

# # delete a card and check structure of order
# hand.delete('c','6')

# print(hand.preOrder())

# # delete card with no right subtree and check structure
# hand.delete('c','k')

# print(hand.preOrder())

# print(hand.root.right)

# hand = PlayerHand()
# hand.put('H', '7')

# hand.delete('h','7')

# hand.isEmpty()

# hand = PlayerHand()
# hand.put('c','7')
# hand.put('c','5')
# hand.put('c','j')
# hand.put('c','9')
# hand.put('c','8')
# hand.put('c','10')
# hand.put('c','3')
# hand.put('c','6')

# print(hand.preOrder())

# print(hand.root.right)

# hand.delete('c','j') # no right subtree

# print(hand.preOrder())

# print(hand.root.right.right)

# print(hand.inOrder())

# hand = PlayerHand()
# hand.put('c','7')
# hand.put('c','9')
# hand.put('c','8')

# print(hand.root)

# dummycard = Card('c', '7')

# dummycard == hand.root

# # inOrder test
# hand = PlayerHand()
# hand.put('D', 'A')
# hand.put('S', 'K')
# hand.put('S', '2')
# hand.put('C', 'Q')
# hand.put('H', '7')
# hand.put('S', 'K')
# hand.put('C', 'K')
# hand.inOrder() == \
# "D A | 1\n\
# S 2 | 1\n\
# H 7 | 1\n\
# C Q | 1\n\
# C K | 1\n\
# S K | 2\n"

# #preOrder() test
# hand = PlayerHand()
# hand.put('D', 'A')
# hand.put('S', 'K')
# hand.put('S', '2')
# hand.put('C', 'Q')
# hand.put('H', '7')
# hand.put('S', 'K')
# hand.put('C', 'K')
# 
# hand.preOrder() == \
# "D A | 1\n\
# S K | 2\n\
# S 2 | 1\n\
# C Q | 1\n\
# H 7 | 1\n\
# C K | 1\n"

# In[ ]:





# 

# In[ ]:





# In[ ]:




