from node import Node
from collections import OrderedDict

class HuffmanTree:
    def __init__(self, nodes: list[Node]):
        self.root = self._build_huffman_tree(nodes)

    def encode(self, text: str) -> str:
        codebook = self.build_huffman_codes()
        print(codebook)
        encoded_text = ''.join(str(codebook[char]) for char in text)
        return encoded_text
    
    def decode(self, encoded_text: str) -> str:
        decoded_text = ''
        current = self.root
        for bit in encoded_text:
            if bit == '0':
                current = current.left
            else:
                current = current.right
            if not current.left and not current.right:
                decoded_text += current.char
                current = self.root
        return decoded_text

    def parse_tree_preorder(self) -> dict:
        tree = OrderedDict()
        return self._parse_tree_preorder(self.root, tree)
    
    # Busca recursiva na árvore em pré-ordem
    def _parse_tree_preorder(self, node: Node, tree: dict) -> dict:
        if node:
            tree[node.char] = node.freq
            self._parse_tree_preorder(node.left, tree)
            self._parse_tree_preorder(node.right, tree)
        return tree
    
    def build_huffman_codes(self) -> dict:
        return self._build_huffman_codes(self.root)
    
    def _build_huffman_codes(self, node: Node, prefix: str = "", codebook: dict = {}) -> dict:
        if node:
            if not node.left and not node.right:
                codebook[node.char] = prefix
            self._build_huffman_codes(node.left, prefix + "0", codebook)
            self._build_huffman_codes(node.right, prefix + "1", codebook)
        return codebook

    def _build_huffman_tree(self, nodes: list) -> Node:
        while len(nodes) > 1:
            left = nodes.pop(0)
            right = nodes.pop(0)
            new_node = Node(None, left.freq + right.freq)
            new_node.left = left
            new_node.right = right
            nodes.append(new_node)
        return nodes[0]