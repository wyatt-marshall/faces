import os
from PIL import Image

def main():
    # i = 1
    # for count, filename in enumerate(os.listdir("/Users/wyattmarshall/Desktop/faces/blah/")):
    for i in range(1, 5001):

        # dst = str(i) + '.jpg'
        # src = "/Users/wyattmarshall/Desktop/faces/real/" + filename
        # dst = "/Users/wyattmarshall/Desktop/faces/real/" + dst
        # os.rename(src, dst)
        f = "/Users/wyattmarshall/Desktop/faces/archive/" + str(i) + ".jpg"
        im = Image.open(f)
        new_im = im.resize((256, 256))
        new_im.save("a" + str(i-1) + '.jpg')
        im.close()

        # i += 1

main()
print("done")