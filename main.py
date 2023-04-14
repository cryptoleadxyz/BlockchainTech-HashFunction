# Author: CryptoLead at https://www.cryptolead.xyz
# Date: 2023-01-10
# Message: Hey there fellow coders! If you found my code helpful and want to show your support, consider buying me a coffee or two. Your donations help me keep improving the code and creating more awesome stuff for the community. Thanks for your support!
# Donation: cryptolead.eth or 0xa2c35DA418f52ed89Ba18d51DbA314EB1dc396d0
 

import string as s
import hashlib

very_long_text = s.ascii_uppercase * 100_000_000
very_long_text = very_long_text[:10000]

string_list = ["cat", "cat", "Cat", "dog", "rabbit", very_long_text]

for string in string_list:
    hash_obj = hashlib.sha256(string.encode())
    hash_val = hash_obj.hexdigest()
    print(f'Hash value for "{string}": {hash_val}')

input_list = [1, 1.0, (0.5 + 0.5), 1.111, (1 + 0.111), (12, 3.534, "dog", "cat")]

for list_item in input_list:
    hash_val = hash(list_item)
    print(f'Hash value for "{list_item}": {hash_val}')


# print(hash([12, 3.534, 'dog', 'cat'])) # TypeError: unhashable type: 'list'
# print(hash({'key1': 1, 'key2': 2})) # Output TypeError: unhashable type: 'dict'


class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.data).encode("utf-8") + str(self.previous_hash).encode("utf-8")
        )
        return sha.hexdigest()


# Example usage
block1 = Block("Peter sends 1 eth to Sally", None)
block2 = Block("Sally sends 2 eth to Sam", block1.hash)
print("block1 hash:", block1.hash)
print("block2 hash:", block2.hash)
