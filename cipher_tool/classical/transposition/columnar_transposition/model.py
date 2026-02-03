from cipher_tool.core.base import BaseCipher


class ColumnarTranspositionCipher(BaseCipher):
    """
    Columnar Transposition cipher implementation.
    """

    def __init__(self, key: str = "KEY"):
        self.key = key.upper()
        self.key_order = self._get_key_order()

    def encrypt(self, text: str) -> str:
        # Remove spaces and pad if necessary
        text = text.replace(' ', '')
        while len(text) % len(self.key) != 0:
            text += 'X'
        
        # Create grid
        grid = []
        for i in range(0, len(text), len(self.key)):
            grid.append(list(text[i:i + len(self.key)]))
        
        # Read columns in key order
        result = []
        for col_idx in self.key_order:
            for row in grid:
                result.append(row[col_idx])
        
        return ''.join(result)

    def decrypt(self, text: str) -> str:
        cols = len(self.key)
        rows = len(text) // cols
        
        # Create empty grid
        grid = [['' for _ in range(cols)] for _ in range(rows)]
        
        # Fill grid column by column in key order
        idx = 0
        for col_idx in self.key_order:
            for row in range(rows):
                grid[row][col_idx] = text[idx]
                idx += 1
        
        # Read row by row
        result = []
        for row in grid:
            result.extend(row)
        
        return ''.join(result).rstrip('X')

    def _get_key_order(self):
        return sorted(range(len(self.key)), key=lambda i: self.key[i])