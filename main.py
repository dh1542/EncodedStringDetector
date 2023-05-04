import base64
import re


# Ask user for input string
#input_string = input("To be decoded string: ")

input_string = "IRXW22LONFVQ===="

# base64 
pattern = re.compile("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$")
if(pattern.match(input_string) != "None"):
    print("Input is in encoded in BASE64. Decoding in progress.")
    print(base64.b64decode(input_string))

# base32
pattern = re.compile("^(?:[A-Z2-7]{8})*(?:[A-Z2-7]{2}={6}|[A-Z2-7]{4}={4}|[A-Z2-7]{5}={3}|[A-Z2-7]{7}=)?$")
if(pattern.match(input_string) != "None"):
    print("Input is encoded in BASE32. Decoding in progress.")
    print(base64.b32decode(input_string))

