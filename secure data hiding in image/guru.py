import cv2
import os
import string

img_path = r"C:\Users\ramad\Downloads\What-is-Cyber-Security.jpg"  # Correct the image path

img = cv2.imread(img_path)

if img is None:
    print(f"Error: The image at path '{img_path}' could not be loaded. Please check the file path and format.")
    exit()  

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

# Encode the message in the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

# Save and display the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  

# Decryption process
message = ""
n = 0
m = 0
z = 0

# Ask for passcode for decryption
pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
