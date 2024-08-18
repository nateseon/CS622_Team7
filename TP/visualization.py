import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def visualize_tree(tree):
    G = nx.DiGraph()
    # Add nodes and edges to the graph based on the tree structure
    # Use G.add_node(), G.add_edge() according to the tree data

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()

# Streamlit UI
st.title('Tree Visualization')
tree_type = st.selectbox('Select Tree Type', ('Prefix Tree', Red-Black Tree', 'B+ Tree'))

if tree_type == 'Prefix Tree':
    # Create and visualize the Prefix Tree
    trie = Trie()
    words = st.text_input('Insert words (comma separated)').split(',')
    for word in words:
        trie.insert(word)
    visualize_tree(trie)

elif tree_type == 'Red-Black Tree':
    # Create and visualize the Red-Black Tree
    rbt = RedBlackTree()
    numbers = st.text_input('Insert numbers (comma separated)').split(',')
    for number in numbers:
        rbt.insert(int(number))
    visualize_tree(rbt)

elif tree_type == 'B+ Tree':
    # Create and visualize the B+ Tree
    bpt = BPlusTree(t=3)  # 3rd-order B+ Tree
    numbers = st.text_input('Insert numbers (comma separated)').split(',')
    for number in numbers:
        bpt.insert(int(number))
    visualize_tree(bpt)
