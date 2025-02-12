---

# **Hybrid Caesar & Rail Fence Cipher Encryption in Python**

## **Overview**
This Python script implements a **hybrid encryption algorithm** combining the **Caesar Cipher** and **Rail Fence Cipher** to enhance security. The encryption process first applies the **Caesar Cipher**, followed by the **Rail Fence Cipher**, and the decryption process reverses this order.

## **Features**
- ✅ **Caesar Cipher**: A simple substitution cipher that shifts letters forward or backward by a given key.
- ✅ **Rail Fence Cipher**: A transposition cipher that rearranges the characters of the text in a zigzag pattern.
- ✅ **Hybrid Encryption**: Enhances security by combining both ciphers.
- ✅ **Supports Spaces and Special Characters**: Non-alphabetic characters remain unchanged in the encryption process.
- ✅ **Two-Step Encryption & Decryption**: Ensures better security than a single encryption method.

## **How to Run the Code**

### **1. Prerequisites**
Ensure you have **Python 3.x** installed on your system. You can download it from the official Python website:  
[Download Python](https://www.python.org/downloads/)

### **2. Clone the Repository**
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/Pratheeka-29/Hybrid_cipher.git
```

### **3. Navigate to the Project Folder**
After cloning, navigate to the folder where the project is located:
```bash
cd Hybrid_cipher
```

### **4. Run the Code**
To run the hybrid encryption script:
```bash
python hybrid.py
```

## **How It Works**
### **Encryption Process**
**Step 1: Caesar Cipher Encryption**
- Each letter in the plaintext is shifted forward by the specified key.
- Non-alphabetic characters remain unchanged.

**Step 2: Rail Fence Cipher Encryption**
- The Caesar-encrypted text is further encrypted using the Rail Fence cipher.
- The characters are arranged in a zigzag pattern across a specified number of rails and then read row-wise.

### **Decryption Process**
**Step 1: Rail Fence Cipher Decryption**
- Reconstructs the zigzag pattern and reads it row-wise to recover the intermediate text.

**Step 2: Caesar Cipher Decryption**
- The intermediate text is decrypted by shifting letters backward by the same key used during encryption.
- Non-alphabetic characters remain unchanged.

## **Example Execution**

### **Input:**
```bash
Plaintext: HELLOHYBRID
Caesar Shift Key: 3
Rail Fence Depth: 3
```

### **Encryption Steps:**
**Caesar Cipher Output:**
```bash
KRUHOKELOBG
```
**Rail Fence Cipher Output (Final Encrypted Text):**
```bash
KRUHOKELOBG
```

### **Decryption Steps:**
**Rail Fence Decryption Output:**
```bash
HELLOHYBRID
```
**Caesar Decryption Output (Final Decrypted Text):**
```bash
HELLOHYBRID
```

## **Code Explanation**

### **Functions**
1. `caesar_cipher(text, key, encrypt=True)`:
   - Encrypts or decrypts text using the **Caesar Cipher**.
   - The shift is **forward for encryption** and **backward for decryption**.
   - Only alphabetic characters are modified.

2. `rail_fence_encrypt(text, rails)`:
   - Encrypts text using the **Rail Fence Cipher**.
   - Arranges the text in a **zigzag pattern** and reads it row-wise.

3. `rail_fence_decrypt(text, rails)`:
   - Decrypts text encrypted with the **Rail Fence Cipher**.
   - Reconstructs the **zigzag pattern** and retrieves the original sequence.

4. `hybrid_encrypt(text, caesar_key, rail_rails)`:
   - Applies **Caesar Cipher Encryption** followed by **Rail Fence Encryption**.

5. `hybrid_decrypt(text, caesar_key, rail_rails)`:
   - Applies **Rail Fence Decryption** followed by **Caesar Cipher Decryption**.

## **Customization**
- Change the **Caesar key** to modify the shift applied to each letter.
- Adjust the **Rail Fence depth** to alter the transposition complexity.
- Enhance security by adding **more encryption layers** or modifying the sequence of encryption.

## **Requirements**
- **Python 3.x**

## **Additional Information**
This **hybrid encryption method** strengthens security by combining **substitution (Caesar Cipher)** and **transposition (Rail Fence Cipher)** techniques. It can be further improved by using **dynamic shifting keys** or integrating additional cipher methods.

---

