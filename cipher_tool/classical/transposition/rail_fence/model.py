from cipher_tool.core.base import BaseCipher


class RailFenceCipher(BaseCipher):
    """
    Rail Fence cipher implementation.
    """

    def __init__(self, rails: int = 3):
        if rails < 2:
            raise ValueError("Number of rails must be at least 2")
        self.rails = rails

    def encrypt(self, text: str) -> str:
        if len(text) <= 1:
            return text
        
        fence = [[] for _ in range(self.rails)]
        rail = 0
        direction = 1
        
        for char in text:
            fence[rail].append(char)
            rail += direction
            
            if rail == self.rails - 1 or rail == 0:
                direction = -direction
        
        return ''.join([''.join(rail) for rail in fence])

    def decrypt(self, text: str) -> str:
        if len(text) <= 1:
            return text
        
        # Calculate positions
        fence = [[] for _ in range(self.rails)]
        rail = 0
        direction = 1
        
        for i in range(len(text)):
            fence[rail].append(i)
            rail += direction
            
            if rail == self.rails - 1 or rail == 0:
                direction = -direction
        
        # Fill the fence with characters
        result = [''] * len(text)
        idx = 0
        
        for rail in fence:
            for pos in rail:
                result[pos] = text[idx]
                idx += 1
        
        return ''.join(result)