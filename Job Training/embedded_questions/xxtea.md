#  XXTEA

## Meaning

Extended Tiny Encryption Algorithm is a block cipher encryption

## Block Cipher

- Can encrypt and decrypt of any length
- 128 bit key used for encryption and decryption
- number of rounds to encrypt and decrypt

## Plain text

- actual data we going to encrypt to cipher text

## Cipher text

- data going to decrypt

## AAD

- Additional authentication data
- Used to verify if the image blocks have been tampered with
- Encryption process generates a tag that authenticates both the ciphertext and the aad  

- xxtea key and aad is provided as input along with plain text for encryption
- check the integrity of the aad using the tag generated during encryption if the aad do not match the original
image has been tampered with

## how it works

- data split into 32 bit blocks
- otherwise padding
- have a checksum
