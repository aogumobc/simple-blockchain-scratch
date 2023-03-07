import hashlib

class Block:
    block_number:int = 0
    data:str = None
    next_block = None
    nonce:int = 0
    previous_hash:int = 0x0

    def __init__(
        self,
        _data
    ) -> None:
        self.data = _data

    def hash(self) -> str:
        h = hashlib.sha256()
        h.update(
            str(self.block_number).encode('utf8') +
            str(self.data).encode('utf8') +
            str(self.nonce).encode('utf8') +
            str(self.previous_hash).encode('utf8')
        )
        
        return h.hexdigest()

    def __str__(self) -> str:
        return \
            "\n" +\
            "Block Number: " + str(self.block_number) + "\n" +\
            "Bloch Hash  : " + str(self.hash()) + "\n" +\
            "Nonce       : " + str(self.nonce) + "\n" +\
            "--------------------------------------------------"