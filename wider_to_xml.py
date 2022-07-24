import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

from PIL import Image


class WiderToXML:
    def __init__(self, annotationsPath, xmlPath, imagePath):
        self.annotationsPath = annotationsPath
        self.xmlPath = xmlPath
        self.imagePath = imagePath


def createAnnotationPascalVocTree(folder, basename, path, width, height):
    annotation = ET.Element("annotation")
    ET.SubElement(annotation, "folder").text = folder
    ET.SubElement(annotation, "filename").text = basename
    ET.SubElement(annotation, "path").text = path
    source = ET.SubElement(annotation, "source")
    ET.SubElement(source, "database").text = "Unknown"
    size = ET.SubElement(annotation, "size")
    ET.SubElement(size, "width").text = width
    ET.SubElement(size, "height").text = height
    ET.SubElement(size, "depth").text = "3"
    ET.SubElement(annotation, "segmented").text = "0"
    return ET.ElementTree(annotation)


def createObjectPascalVocTree(xmin, ymin, xmax, ymax):
    obj = ET.Element("object")
    ET.SubElement(obj, "name").text = "face"
    ET.SubElement(obj, "pose").text = "Unspecified"
    ET.SubElement(obj, "truncated").text = "0"
    ET.SubElement(obj, "difficult").text = "0"
    bndbox = ET.SubElement(obj, "bndbox")
    ET.SubElement(bndbox, "xmin").text = xmin
    ET.SubElement(bndbox, "ymin").text = ymin
    ET.SubElement(bndbox, "xmax").text = xmax
    ET.SubElement(bndbox, "ymax").text = ymax
    return ET.ElementTree(obj)


def parseImFilename(self, imFilename):
    im = Image.open(os.path.join(self.imagePath, imFilename))
    folder, basename = imFilename.split("/")
    width, height = im.size
    return folder, basename, imFilename, str(width), str(height)


def convertWFAnnotations(self):
    with open(self.annotationsPath) as f:
        while True:
            imFilename = f.readline().strip()
            if len(imFilename.split(" ")) > 1:
                continue

            if imFilename:
                folder, basename, path, width, height = parseImFilename(imFilename, self.imagePath)
                ann = createAnnotationPascalVocTree(folder, basename, os.path.join(self.imagePath, path), width, height)
                nbBndboxes = f.readline()
                i = 0
                while i < int(nbBndboxes):
                    i = i + 1
                    x1, y1, w, h, _, _, _, _, _, _ = [int(i) for i in f.readline().split()]
                    ann.getroot().append(
                        createObjectPascalVocTree(str(x1), str(y1), str(x1 + w), str(y1 + h)).getroot()
                    )
                if not os.path.exists(self.xmlPath):
                    os.makedirs(self.xmlPath)
                annFilename = os.path.join(self.xmlPath, basename.replace(".jpg", ".xml"))
                o = open(annFilename, "wb")
                o.write(
                    bytes(minidom.parseString(ET.tostring(ann.getroot())).toprettyxml(indent="   ").encode("utf-8"))
                )
                o.close()
                print("{} => {}".format(basename, annFilename))

            else:
                break
    f.close()


if __name__ == "__main__":
    WiderToXML(
        annotationsPath="wider_face_split/wider_face_train_bbx_gt.txt",
        xmlPath="wider_face_split/wider_face_train_bbx_gt",
        imagePath="wider_face_split/WIDER_train/images",
    )
