# Crypt Command Line Application

The CLA includes traditional ciphers such as the Caesar Cipher, Autokey Cipher, and Railfence Cipher, as well as modern ciphers like AES, DES, and the asymmetrical cipher RSA.

## How to:

#### Clone this repo.

#### Install cryptodome if not installed already.

##### Note: $ is to denote terminal commands. Do not include it as part of the command.

```sh
$ pip install pycryptodome
```

- Python 3.x

```sh
$ pip3 install pycryptodome
```

#### Run the application.

```sh
$ python main.py
```

Python 3.x

```sh
$ python3 main.py
```

#### Follow the instructions given in the command-line application.

##### Note: RSA will output keys and encrypted data to the subdirectory /rsa

# Symmetric Encryption

## Traditional Ciphers

### Caesar Cipher

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

#### Encryption:

Each letter in the plaintext is shifted by a fixed number, known as the key. For example, with a key of 3, 'A' would be encrypted to 'D', 'B' to 'E', and so on.

#### Decryption:

Each letter in the ciphertext is shifted back by the same fixed number.

##### Example:

- Plaintext: HELLO
- Key: 3
- Ciphertext: KHOOR

### Autokey Cipher

The Autokey Cipher is a polyalphabetic substitution cipher that uses a keyword followed by the plaintext itself to create the key.

#### Encryption:

A keyword is chosen and appended to the plaintext (after removing the keyword length) to create a running key. Each letter of the plaintext is shifted by the corresponding letter of the running key, where 'A' represents a shift of 0, 'B' a shift of 1, and so on.

#### Decryption:

The keyword is used to decipher the first part of the message. The plaintext itself is then used to decipher the remaining part.

##### Example:

- Plaintext: HELLO
- Keyword: KEY
- Ciphertext: RIJSS

### Railfence Cipher

The Railfence Cipher is a transposition cipher that arranges the plaintext in a zigzag pattern across multiple "rails" and then reads it off row by row.

#### Encryption:

The plaintext is written in a zigzag pattern across a fixed number of rails. The ciphertext is obtained by reading the pattern row by row.

#### Decryption:

The ciphertext is written in the zigzag pattern and read off in the original order.

##### Example:

- Plaintext: HELLO WORLD
- Number of Rails: 3
- Ciphertext: HOLELWRDLO

## Modern Ciphers

### AES (Advanced Encryption Standard)

AES is a symmetric key encryption standard adopted by the U.S. government. It supports key sizes of 128, 192, and 256 bits and operates on 128-bit blocks.

#### Encryption:

The plaintext is divided into 128-bit blocks. Each block undergoes multiple rounds of substitution, permutation, mixing, and key addition.

#### Decryption:

The process is reversed using the same key to retrieve the original plaintext.

#### Key Features:

- Strong security
- Widely used in various applications

### DES (Data Encryption Standard)

DES is a symmetric key encryption algorithm that uses a 56-bit key and operates on 64-bit blocks.

#### Encryption:

The plaintext is divided into 64-bit blocks. Each block undergoes 16 rounds of permutation and substitution based on the key.

#### Decryption:

The process is reversed using the same key to retrieve the original plaintext.

#### Key Features:

- Less secure by modern standards due to short key length
- Superseded by AES

# Asymmetric Encryption

## RSA (Rivest–Shamir–Adleman)

RSA is an asymmetric key encryption algorithm that uses a pair of keys: a public key for encryption and a private key for decryption.

#### Encryption:

The plaintext is encrypted using the recipient's public key. Only the recipient can decrypt the ciphertext using their private key.

#### Decryption:

The ciphertext is decrypted using the recipient's private key.

#### Key Features:

- Based on the mathematical difficulty of factoring large prime numbers
- Widely used for secure data transmission
