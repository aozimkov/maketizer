#!/usr/bin/env python
# coding: utf-8

import os
import glob

# Mask for choose specific files in folder
FILEMASK = "*.png"

# Read current folder, get sorted list with *.png filnames
def get_images_list():
    path = os.path.dirname(os.path.abspath(__file__))
    return [os.path.basename(filename) for filename in glob.glob("{}/{}".format(path, FILEMASK))]

# Make an easy html file with image
def get_file_body(image, maket_length, current_index):
    index = current_index + 1 if current_index > 0 else ''
    return """<html>
<head>
<title>Test</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Expires" content="0" />
</head>
<body style="padding: 0; margin: 0;">
<a href="index{}.html"><img src="{}" width="100%"/></a>
</body></html>
""".format(index, image)

# construct html-file filename
def get_filename(index):
    index_postfix = '' if index == 0 else index + 1 
    return "index{}.html".format(index_postfix)

#create an html file and put generated html content
def create_html_file(index, body):
    f = open(get_filename(index), "w")
    f.write(body)
    f.close()

images_list = get_images_list()

for index in range(len(images_list)):
    image = images_list[index]
    html  = get_file_body(image, len(images_list), index)
    create_html_file(index, html)
