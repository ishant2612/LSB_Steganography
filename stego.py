#!/usr/bin/python3

from stegano import lsb
import random
import re

def embed_message(input_image, message, password=None):
    if not input_image.endswith('.png'):
        print("Error: Please provide a PNG image file.")
        return

    if not password:
        password = "no_password_given"
    
    embed_data = password + " " + message
    secret = lsb.hide(input_image, embed_data)
    random_number = random.randint(0, 100)
    output_filename = f"secret{random_number}.png"
    secret.save(output_filename)
    print("File Saved as", output_filename)

def extract_message(input_image, password):
    if not input_image.endswith('.png'):
        print("Error: Please provide a PNG image file.")
        return

    if not password:
        print("Error: Please provide a password.")
        return

    try:
        message = lsb.reveal(input_image)
        if password in message:
            extracted_message = message.replace(password, "")
            print("The secret Message is", extracted_message)
        else:
            print("Error: Couldn't reveal the message with the provided password.")
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("\nEnter 'exit' to quit the program.")
        task = input("Enter 'embed' to embed a message or 'extract' to extract a message: ").lower()

        if task == 'exit':
            break

        if task not in ['embed', 'extract']:
            print("Invalid input. Please enter 'embed' or 'extract'.")
            continue

        file_path = input("Enter the file path of the PNG image: ")

        if task == 'embed':
            message = input("Enter the message to embed: ")
            password = input("Enter the password (optional): ")
            embed_message(file_path, message, password)
        elif task == 'extract':
            password = input("Enter the password: ")
            extract_message(file_path, password)

if __name__ == "__main__":
    main()
