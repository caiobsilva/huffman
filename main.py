from node import Node
from huffman_tree import HuffmanTree

def build_frequency_dict(text: str) -> dict:
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


while True:
    print("\n\n")
    print("Compressão de texto com algoritmo de Huffman")

    text = input("Insira um texto: ")

    freq = build_frequency_dict(text)
    nodes = [Node(char, freq) for char, freq in freq.items()]
    nodes = sorted(nodes, key=lambda node: node.freq)

    tree = HuffmanTree(nodes)

    print("\n\n")

    encoded_text = tree.encode(text)
    decoded_text = tree.decode(encoded_text)

    print("Texto original:", text)
    print("Texto codificado:", encoded_text)
    print("Texto decodificado:", decoded_text)
    print("\n")
    print(f"Frequência: {freq}")
    print(f"Tamanho original: {len(text) * 8} bits")
    print(f"Tamanho codificado: {len(encoded_text)} bits")
