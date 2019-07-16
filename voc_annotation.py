import xml.etree.ElementTree as ET
from os import getcwd

#sets=['train', 'val']
sets=['train']

class_name = open('/home/style/PycharmProjects/VOCMine/VOCMine_other/className.txt').read().split()

def convert_annotation(image_id, list_file):
    in_file = open('/home/style/PycharmProjects/VOCMine/VOCMine_other/Annotations/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in class_name or int(difficult)==1:
            continue
        cls_id = class_name.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()
for set in sets:
    image_ids = open(
        '/home/style/PycharmProjects/VOCMine/VOCMine_other/ImageSets/Main/%s.txt' % (set)).read().strip().split()
    list_file = open('other/%s.txt' % (set), 'w')
    for image_id in image_ids:
        # list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg' % (wd, year, image_id))
        list_file.write('/home/style/PycharmProjects/VOCMine/VOCMine_other/JPEGImages/%s.jpg' % (image_id))
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()

