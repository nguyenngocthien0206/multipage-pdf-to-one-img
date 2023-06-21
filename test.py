# import module
from pdf2image import convert_from_path
from PIL import Image
import glob

def get_concat_v(images):
    wid = images[0].width
    height = 0
    for img in images:
        height = height + img.height
        
    dst = Image.new('RGB', (wid, height))
    h = 0
    for img in images:
        dst.paste(img, (0, h))
        h += img.height
        
    return dst

def get_concat_h(images):
    height = images[0].height
    wid = 0
    for img in images:
        wid = wid + img.width
        
    dst = Image.new('RGB', (wid, height))
    w = 0
    for img in images:
        dst.paste(img, (w, 0))
        w += img.width
        
    return dst

# Store Pdf with convert_from_path function
poppler_path = r'poppler-23.05.0\Library\bin'

print("Parse 1 file or whole folder?")
print("1. File")
print("2. Folder")
choice = int(input("Your choice: "))

if choice == 1:
    pdf_path = input("Enter pdf path: ")
    images = convert_from_path(pdf_path=pdf_path,poppler_path=poppler_path)
    get_concat_v(images).save(f'{pdf_path[0:len(pdf_path)-4]}.jpg')
    
else:
    folder = input("Enter folder path: ")
    output = input("Enter output folder: ")

    for filename in glob.iglob(f'{folder}/*'):
        images = convert_from_path(pdf_path=filename,poppler_path=poppler_path)
        img_name = filename[len(folder)+1:len(filename)-3] + 'jpg'
        get_concat_v(images).save(f'{output}/{img_name}')


# images = convert_from_path(pdf_path=pdf_path,poppler_path=poppler_path)




# get_concat_v(images).save('test_v.jpg')
# get_concat_h(images).save('test_h.jpg')