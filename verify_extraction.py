from PIL import Image
import numpy as np

img = Image.open("stego_1lsb_blue_unknown.png").convert("RGB")
arr = np.array(img)
flat = arr.reshape(-1, 3)
bits = [flat[i, 2] & 1 for i in range(len(flat))]
data = bytearray()
for i in range(0, len(bits), 8):
    byte = 0
    for bit_index in range(8):
        if i + bit_index < len(bits):
            byte |= (bits[i + bit_index] & 1) << bit_index
    data.append(byte)
if len(data) >= 4:
    l = int.from_bytes(data[:4], "little")
    msg = data[4:4+l].decode("utf-8", errors="replace")
    print("----- Hidden Message -----")
    print(msg)
    print("---------------------------")
else:
    print("No data found.")