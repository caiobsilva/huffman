class Node:
    def __init__(self, char: str = '', freq: str = ''):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return self.char