import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from B_plus_tree import BPlusTree
from prefix_tree import Trie
from red_black_tree import RedBlackTree

def visualize_tree(tree):
    G = nx.DiGraph()
    # Add nodes and edges to the graph based on the tree structure
    # You need to implement this part based on the tree's traversal
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()

st.title('Tree Visualization')
tree_type = st.selectbox('Select Tree Type', ('Prefix Tree', 'Red-Black Tree', 'B+ Tree'))

if tree_type == 'Prefix Tree':
    trie = Trie()
    words = st.text_input('Insert words (comma separated)').split(',')
    # Filter out any empty strings from the input list
    words = [word.strip() for word in words if word.strip()]
    for word in words:
        trie.insert(word)
    visualize_tree(trie)

elif tree_type == 'Red-Black Tree':
    rbt = RedBlackTree()
    numbers = st.text_input('Insert numbers (comma separated)').split(',')
    # Filter out any empty strings and convert to integers
    numbers = [int(number) for number in numbers if number.strip()]
    for number in numbers:
        rbt.insert(number)
    visualize_tree(rbt)

elif tree_type == 'B+ Tree':
    bpt = BPlusTree(t=3)  # 3rd-order B+ Tree
    numbers = st.text_input('Insert numbers (comma separated)').split(',')
    # Filter out any empty strings and convert to integers
    numbers = [int(number) for number in numbers if number.strip()]
    for number in numbers:
        bpt.insert(number)
    visualize_tree(bpt)
