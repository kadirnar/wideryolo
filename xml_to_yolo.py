import argparse
from xml.dom import minidom
import os
import glob


def convert_coordinates(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def remove_xml(path):
    txt_files = glob.glob(path+'*.xml')
    for file in txt_files:
        os.remove(file)


def convert_xml2yolo(path):
    lut = {"accessory": 0, "top": 1, "bottom": 2, "bag": 3, "shoes": 4}
    for fname in glob.glob(path+"./*.xml"):
        xmldoc = minidom.parse(fname)
        fname_out = (fname[:-4] + '.txt')

        with open(fname_out, "w") as f:
            itemlist = xmldoc.getElementsByTagName('object')
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)

            for item in itemlist:
                classid = (item.getElementsByTagName('name')[0]).firstChild.data

                if classid in lut:
                    label_str = str(lut[classid])

                else:
                    label_str = "0"
                    print("warning: label '%s' not in look-up table" % classid)

                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width, height), b)
                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

        print("wrote %s" % fname_out)
    remove_xml(path)


def main():
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--path', type=str, default='./', help='.xml dosyaları .txt formatına çevirme')
    ARGS = PARSER.parse_args()
    convert_xml2yolo(ARGS.path)


if __name__ == '__main__':
    main()
