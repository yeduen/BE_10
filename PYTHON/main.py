import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from animals import Dog, Eagle

def main():
    dog = Dog("Buddy", "Golden Retriever")
    eagle = Eagle("Sky", 200)

    print(dog.info())
    print(eagle.info())

if __name__ == "__main__":
    main()