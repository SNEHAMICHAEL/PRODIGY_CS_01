# Task-01

A Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

# Caesar Cipher

The earliest known use of a substitution cipher, and the simplest, was by Julius Caesar. The Caesar cipher involves replacing each letter of the alphabet with the letter standing three places further down the alphabet.

For example,

plain: meet me after the toga party

cipher: PHHW PH DIWHU WKH WRJD SDUWB

Note that the alphabet is wrapped around, so that the letter following Z is A. We can define the transformation by listing all possibilities, as follows:

plain: a b c d e f g h i j k l m n o p q r s t u v w x y z

cipher: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

The algorithm can be expressed as follows. For each plaintext letter p, substitute the ciphertext letter C:

We define a mod n to be the remainder when a is divided by n. For example, 11 mod 7 = 4.

C= E(3, p) = (p+ 3) mod 26

A shift may be of any amount, so that the general Caesar algorithm is

C= E(k, p) = (p+ k) mod 26

where k takes on a value in the range 1 to 25. The decryption algorithm is simply

p= D(k, C) = (Ck) mod 26

# Examples

Enter your message: APPLE

Enter the shift value: 3

Encrypted text is DSSOH

Decrypted text is APPLE
