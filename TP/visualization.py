import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from B_plus_tree import BPlusTree
from prefix_tree import Trie
from red_black_tree import RedBlackTree

def visualize_tree(tree):
    G = nx.DiGraph()

    # Helper function to add edges for the Trie
    def add_trie_edges(node, prefix=""):
        if node.is_end_of_word:
            G.add_node(prefix, color='lightgreen')
        for char, child in node.children.items():
            child_prefix = prefix + char
            G.add_node(child_prefix)
            G.add_edge(prefix, child_prefix)
            add_trie_edges(child, child_prefix)

    # Helper function to add edges for Red-Black Tree
    def add_rbt_edges(node):
        if node != tree.TNULL:
            if node.left != tree.TNULL:
                G.add_edge(node.data, node.left.data)
                add_rbt_edges(node.left)
            if node.right != tree.TNULL:
                G.add_edge(node.data, node.right.data)
                add_rbt_edges(node.right)

    # Visualization logic based on the type of tree
    if isinstance(tree, Trie):
        add_trie_edges(tree.root)
    elif isinstance(tree, RedBlackTree):
        add_rbt_edges(tree.root)
    elif isinstance(tree, BPlusTree):
        # Implement visualization for BPlusTree based on its structure
        pass

    # Draw the graph
    pos = nx.spring_layout(G)
    colors = [G.nodes[node].get('color', 'skyblue') for node in G.nodes]
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color=colors, font_size=10, font_weight="bold")
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
    numbers = [int(number.strip()) for number in numbers if number.strip()]
    st.write(f"Numbers to insert: {numbers}")  # Debug statement
    for number in numbers:
        rbt.insert(number)
    visualize_tree(rbt)

elif tree_type == 'B+ Tree':
    bpt = BPlusTree(t=3)  # 3rd-order B+ Tree
    numbers = st.text_input('Insert numbers (comma separated)').split(',')
    numbers = [int(number.strip()) for number in numbers if number.strip()]
    st.write(f"Numbers to insert: {numbers}")  # Debug statement
    for number in numbers:
        bpt.insert(number)
    visualize_tree(bpt)
