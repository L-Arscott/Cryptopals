# Cryptopals
Completing the [Cryptopals](https://cryptopals.com/) challenges

## Organisation
### EasyByte class
The challenge requires the manipulation of strings representing bytes in different formats (bytes, hex, bas64, ...). This class was created to easily store and manipulate data of different formats by storing all data as byte strings, so that all methods may be written for byte strings. The class can then translate the byte strings to required formats:
```python
my_bytes = EasyByte('59454c4c4f57205355424d4152494e45', 'hex')  # Store hex string
print(my_bytes.b)  # Prints b'YELLOW SUBMARINE': the above hex string is stored in byte format as self.b
print(my_bytes.convert('b64'))  # Prints 'WUVMTE9XIFNVQk1BUklORQ==', data in base 64
```
For example, it is then easy to XOR our data with data of any format:
```python
my_bytes2 = EasyByte('9454c4c4f57205355424d4152494e455', 'hex')  # Store hex string
xored_easybyte = my_bytes2.xor('zRGIiLolJWYBZplUdt2qEA==', 'b64')  # Obtain my_bytes2 XORed with a string in base64
print(xored_easybyte.convert('text'))  # Obtain result as text, in this case prints 'YELLOW SUBMARINE'
```
