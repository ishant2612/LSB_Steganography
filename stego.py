#!/usr/bin/python3

from stegano import lsb
import argparse
import sys
import random
import re
import time

def embed_message(input_image, message, password=None):
    if not input_image.endswith('.png'):
        print("Error: Please provide a PNG image file.")
        sys.exit(1)

    if not password:
        password = "no_password_given"
    
    embed_data = password + " " + message
    secret = lsb.hide(input_image, embed_data)
    random_number = random.randint(0, 100)
    output_filename = f"secret{random_number}.png"
    secret.save(output_filename)
    print("File Saved as", output_filename)
    time.sleep(4)

def extract_message(input_image, password):
    if not input_image.endswith('.png'):
        print("Error: Please provide a PNG image file.")
        sys.exit(1)

    if not password:
        print("Error: Please provide a password.")
        sys.exit(1)

    try:
        message = lsb.reveal(input_image)
        if password in message:
            extracted_message = message.replace(password, "")
            print("The secret Message is", extracted_message)
            time.sleep(4)
        else:
            print("Error: Couldn't reveal the message with the provided password.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Steganography\n[+] Use .png files only")
    parser.add_argument('-f', help="Input .png image file")
    parser.add_argument('-e', help="Embed a message in the image")
    parser.add_argument('-x', action="store_true", help="Extract the message from the image")
    parser.add_argument('-p', nargs="?", const="no_password_given", help="Optional password")
    args = parser.parse_args()

    if not args.f:
        print("Error: Please provide an input image file.")
        sys.exit(1)

    if args.e and args.x:
        print("Error: Choose either embedding (-e) or extraction (-x), not both.")
        sys.exit(1)

    if args.e:
        embed_message(args.f, args.e, args.p)
    elif args.x:
        extract_message(args.f, args.p)
    else:
        print("Error: Choose either embedding (-e) or extraction (-x).")
        sys.exit(1)
