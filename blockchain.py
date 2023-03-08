from block import Block

class Blockchain:
    block:Block
    head:Block
    
    difficulty:int
    max_nonce:int = 2 << (32-1)
    target:int

    def __init__(
        self,
        _difficulty:int
    ) -> None:
        self.difficulty = _difficulty
        self.target = 2 << (256 -self.difficulty -1)
        
        self.block = Block("Genesis Block")
        _ = head = self.block
        self.head = head

    def add(
        self,
        _block:Block
    ) -> None:
        _block.block_number = self.block.block_number +1
        _block.previous_hash = self.block.hash()
        
        self.block.next_block = _block
        self.block = self.block.next_block

    def mine(
        self,
        _block:Block
    ) -> None:
        for _ in range(self.max_nonce):
            if int(_block.hash(), 16) <= self.target:
                self.add(_block)
                print(_block)
                break
            
            else:
                _block.nonce +=1