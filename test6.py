# -*- coding: UTF-8 -*-
from xml.dom import minidom
import xml.etree.ElementTree as ET

def save_xml():
  annotation = ET.Element('annotation')
  folder = ET.SubElement(annotation, 'folder')
  folder.text = 'XXX'
  filename = ET.SubElement(annotation, 'filename')
  filename.text = 'XXX'
  source = ET.SubElement(annotation, 'source')
  owner = ET.SubElement(annotation, 'owner')
  size = ET.SubElement(annotation, 'size')
  segmented = ET.SubElement(annotation, 'segmented')
  segmented.text = '0'
  object = ET.SubElement(annotation, 'object')
  
  # 子ノードを追加
  database = ET.SubElement(source, 'database')
  database.text = 'XXX' 
  annotation_child = ET.SubElement(source, 'annotation')
  annotation_child.text = 'XXX' 
  image = ET.SubElement(source, 'image')
  image.text = 'XXX' 
  flickrid = ET.SubElement(source, 'flickrid')
  flickrid.text = 'XXX' 

  # 子ノードを追加
  flickrid_child = ET.SubElement(owner, 'flickrid')
  flickrid_child.text = 'XXX'
  name = ET.SubElement(owner, 'flickrid')
  name.text = 'XXX' 

  # 子ノードを追加
  width = ET.SubElement(size, 'width')
  width.text = 'XXX'
  height = ET.SubElement(size, 'height')
  height.text = 'XXX'
  depth = ET.SubElement(size, 'depth')
  depth.text = 'XXX'

  # 子ノードを追加
  name = ET.SubElement(object, 'name')
  name.text = 'XXX'
  pose = ET.SubElement(object, 'pose')
  pose.text = 'XXX'
  truncated = ET.SubElement(object, 'truncated')
  truncated.text = '0'
  difficult = ET.SubElement(object, 'difficult')
  difficult.text = '1'
  bndbox = ET.SubElement(object, 'bndbox')

  # 子ノードを追加
  xmin = ET.SubElement(bndbox, 'xmin')
  xmin.text = 'XXX'
  ymin = ET.SubElement(bndbox, 'ymin')
  ymin.text = 'XXX'
  xmax = ET.SubElement(bndbox, 'xmax')
  xmax.text = 'XXX'
  ymax = ET.SubElement(bndbox, 'ymax')
  ymax.text = 'XXX'

  # インデントを付けて保存
  doc = minidom.parseString(ET.tostring(annotation, 'utf-8'))
  with open('test.xml','w') as f:
    doc.writexml(f, encoding='utf-8', newl='\n', indent='', addindent='  ')

save_xml()