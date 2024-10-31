# Visual Cryptography

## Overview
A command-line program developed in Python that implements Naor-Shamir visual cryptography and its variants. This project implements five methods for image encryption in Python. Each method divides a two-colored image into two shares, which only reveal the original image when overlaid. However, two of these methods exhibit data leaks, making the original image partially visible before the shares are overlaid.
## Technologies Used
- **Programming Language**: Python
- **Image Processing**: Python Imaging Library (PIL)

## Features
- **Secure Image Distribution**: Implements Naor-Shamir visual cryptography, allowing users to securely distribute images by generating multiple shares.
- **Multiple Share Generation**: Capable of producing two shares from a single image, enhancing security and privacy.
- **Tile Generation Methods**: Utilizes various tile generation techniques to create unique shares from the original image, including:

## Tile Generation Methods
1. **Naor-Shamir Scheme**: A set of six balanced tiles, where the number of white and black pixels on each tile is equal.
2. **Fully Random Method**: A collection of sixteen different tiles.
3. **Partially Random Method 1**: A collection of fifteen tiles, excluding a completely black tile.
4. **Partially Random Method 2**: A collection of fifteen tiles, excluding a completely white tile.
5. **Partially Random Method 3**: A collection of fourteen tiles, excluding both completely black and completely white tiles.

## Original Image
![image](https://github.com/user-attachments/assets/22ce6ab3-cc9b-449a-821f-02c7da2ce2fd)

## Naor-Shamir Scheme
### Share 1
![image](https://github.com/user-attachments/assets/be203c21-86f7-4383-86e7-695653c7a5f8)

### Share 2
![image](https://github.com/user-attachments/assets/6ff609a0-eb92-4d8f-b6b4-5f104d49f4c1)

### Overlaid Shares
![image](https://github.com/user-attachments/assets/2155fe23-9b8f-465c-b132-e1b345540c75)

## Fully Random Method
### Share 1
![image](https://github.com/user-attachments/assets/a6a47f3c-d892-487e-bb44-1c45671569b2)

### Share 2
![image](https://github.com/user-attachments/assets/296a769f-fe52-47d4-9aaf-6c8a3d87d550)

### Overlaid Shares
![image](https://github.com/user-attachments/assets/c5895c48-9997-43d3-9639-661039b50ec2)

## Partially Random Method 1 - Data Leaks
### Share 1
![image](https://github.com/user-attachments/assets/06d450b8-c1c2-4ee9-841c-43ae47286ec4)

### Share 2 - Data Leaks Visible
![image](https://github.com/user-attachments/assets/ac9dac55-870d-4db5-b244-5f19ac4336fa)

### Overlaid Shares
![image](https://github.com/user-attachments/assets/2a87559b-21f7-4377-8757-880103f50f42)

## Partially Random Method 2 - Data Leaks
### Share 1
![image](https://github.com/user-attachments/assets/7ccc2736-1cd5-4377-a8bf-e5e6e232d9b4)

### Share 2 - Data Leaks Visible
![image](https://github.com/user-attachments/assets/960cfbad-80a5-4221-bb92-c848e008ae1f)

### Overlaid Shares
![image](https://github.com/user-attachments/assets/369681e4-6b09-40f0-ab56-f4bd7a8ffb7e)

## Partially Random Method 3
### Share 1
![image](https://github.com/user-attachments/assets/40db53d6-e4ba-4136-8397-7a3ea8593521)

### Share 2
![image](https://github.com/user-attachments/assets/af671b75-74b0-4d25-bbcf-967a7ed2cb40)

### Overlaid Shares
![image](https://github.com/user-attachments/assets/0279451c-d60a-4203-b546-1c817ce83155)
