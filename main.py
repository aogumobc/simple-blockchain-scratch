from block import Block
from blockchain import Blockchain

def main():
    repetations:int = int(input("Repetations? Enter the number: "))
    difficulty:int  = int(input("Difficulty?  Enter the number: "))

    blockchain:Blockchain = Blockchain(difficulty)

    for n in range(repetations):
        blockchain.mine(Block("Block " + str(n +1)))
        
    while blockchain.head != None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next_block

if __name__ == "__main__":
    main()