import imagehash
from PIL import Image

types = ['', 'blurred', 'border', 'rotated', 'scaled', 'sheared', 'tint', 'watermark', 'joker']
directory = '/Users/yixin/Downloads/'

for i in [0]:
    for j in range(len(types)):
        a = Image.open(directory + 'the-dark-knight-19-' + types[i] + '.jpg')
        b = Image.open(directory + 'the-dark-knight-19-' + types[j] + '.jpg')
        pha = imagehash.phash(a)
        phb = imagehash.phash(b)
        # print('phash')
        # print(types[i] + ' ' + types[j])
        # print (pha - phb)
        # # total = ha - hb
        aha = imagehash.average_hash(a)
        ahb = imagehash.average_hash(b)
        # print('average')
        # print(types[i] + ' ' + types[j])
        # print (aha - ahb)
        # # total += ha - hb
        dha = imagehash.dhash(a)
        dhb = imagehash.dhash(b)
        # print('dhash')
        # print(types[i] + ' ' + types[j])
        # print (dha - dhb)
        if (pha-phb < aha-ahb) or (dha-dhb > aha-ahb):
            print(types[i], types[j])
