import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from B_plus_tree import BPlusTree
from prefix_tree import Trie
from red_black_tree import RedBlackTree

def visualize_tree(tree):
    G = nx.DiGraph()
    
    # Example visualization logic, you may need to adjust it based on your tree structure
    def add_edges(node, parent=None):
        if parent is not None:
            G.add_edge(parent.data, node.data)
        if node.left != tree.TNULL:
            add_edges(node.left, node)
        if node.right != tree.TNULL:
            add_edges(node.right, node)
    
    if isinstance(tree, RedBlackTree):
        add_edges(tree.root)
    elif isinstance(tree, Trie):
        def add_trie_edges(node, prefix=""):
            if node.is_end_of_word:
                G.add_node(prefix)
            for char, child in node.children.items():
                G.add_edge(prefix, prefix + char)
                add_trie_edges(child, prefix + char)
        
        add_trie_edges(tree.root)
    elif isinstance(tree, BPlusTree):
        # Add logic specific to BPlusTree
        pass
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color="skyblue", font_size=10, font_weight="bold")
    plt.show()

st.title('Tree Visualization')
tree_type = st.selectbox('Select Tree Type', ('Prefix Tree', 'Red-Black Tree', 'B+ Tree'))

if tree_type == 'Prefix Tree':
    trie = Trie()
    words = st.text_input('Insert words (comma separated)').split(',')
    words = [word.strip() for word in words if word.strip()]
    st.write(f"Words to insert: {words}")  # Debug statement
    for word in words:
        trie.insert(word)
    visualize_tree(trie)

elif tree_type == 'Red-Black Tree':
    rbt = RedBlackTree()
    numbers = st.text_input('Insert numbers (comma separated)').split(',')
    # Convert numbers to integers, while handling potential empty strings
    numbers = [int(number.strip()) for number in numbers if number.strip()]
    st.write(f"Numbers to insert: {numbers}")  # Debug statement
    for number in numbers:
        rbt.insert(number)
    visualize_tree(rbt)

elif tree_type == 'B+ Tree':
    bpt = BPlusTree(t=3)  # 3rd-order B+ Tree
    numbers = st.text_input('Insert numbers (comma separated)').split(',')
    # Convert numbers to integers, while handling potential empty strings
    numbers = [int(number.strip()) for number in numbers if number.strip()]
    st.write(f"Numbers to insert: {numbers}")  # Debug statement
    for number in numbers:
        bpt.insert(number)
    visualize_tree(bpt)
