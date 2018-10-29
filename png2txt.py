from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_DB():
    # generate char imgs:
    from PIL import Image, ImageDraw, ImageFont
    IMG_WIDTH = 10
    IMG_HEIGHT = 15
    fnt = ImageFont.truetype('arial.ttf', 15)
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    with open("char_data.txt", 'w') as f:

        for c in chars:
            img = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), color=(255, 255, 255))
            d = ImageDraw.Draw(img)
            d.text((0, 0), c, fill=(0, 0, 0), font=fnt)

            # find out avg color:
            avg = [0,0,0]
            for x in range(IMG_WIDTH):
                for y in range(IMG_HEIGHT):
                    avg[0] += img.getpixel((x, y))[0]
                    avg[1] += img.getpixel((x, y))[1]
                    avg[2] += img.getpixel((x, y))[2]
            avg[0] /= IMG_HEIGHT * IMG_WIDTH
            avg[1] /= IMG_HEIGHT * IMG_WIDTH
            avg[2] /= IMG_HEIGHT * IMG_WIDTH

            print(c, avg)
            f.write(c + ":" + str(avg[0]) + "," + str(avg[1]) + "," + str(avg[2]) + "\n")


if __name__ == '__main__':
    # load the DB:
    DB = {}
    with open("char_data.txt", 'r') as f:
        data = f.readlines()
        for row in data:
            c, rgb_data = row.replace("\n", "").split(":")
            rgb = rgb_data.split(",")
            DB[c] = [float(rgb[0]), float(rgb[1]), float(rgb[2])]
    # print(DB)
    # normalize the DB:
    red_val = [DB[d][0] for d in DB]
    mean = np.sum(red_val)/len(red_val)
    std = np.std(red_val)
    for key in DB:
        DB[key] = [(DB[key][0] - mean)/std, (DB[key][1] - mean)/std, (DB[key][2] - mean)/std]
    #print(DB)

    target = Image.open("Pictures/Abschlussball.png", 'r').convert('LA')
    out_res = (1000, 350)

    target = target.resize(out_res)
    # normalize the target img:
    pixels_as_list = []
    for x in range(out_res[1]):
        for y in range(out_res[0]):
            pixels_as_list.append(target.getpixel((y, x))[0])

    mean = np.sum(pixels_as_list)/(out_res[0]*out_res[1])
    #print(mean)
    std = np.std(pixels_as_list)
    norm_target = np.zeros(shape=out_res)
    for x in range(out_res[1]):
        for y in range(out_res[0]):
            norm_target[y,x] = (target.getpixel((y, x))[0] - mean) / std

    #print(norm_target)
    #from matplotlib import pyplot as plt
    #plt.imshow(target.resize(out_res))
    #plt.show()
    output = ""
    # now find for each pixel the best matching character:
    for x in range(out_res[1]):
        for y in range(out_res[0]):
            t_val = norm_target[y,x]
            diff = 999
            best_char = 'a'
            for key in DB.keys():
                if np.abs(DB[key][0] - t_val) < diff:
                    diff = np.abs(DB[key][0] - t_val)
                    best_char = key
            output += best_char
        output += "\n"
    #print(output)
    with open("png2txt_output.txt", 'w') as f:
        f.write(output)


