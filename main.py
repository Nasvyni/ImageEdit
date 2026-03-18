from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('original.jpg') as pic:
    print('Ukuran:', pic.size)
    print('Format:', pic.format)
    print('Jenis warna:', pic.mode)
    pic.show()

    pic_bw = pic.convert('L')
    pic_bw.save('grey.jpg')
    pic_bw.show()

    #pic.filter(ImageFilter.BLUR)
    #jangan lupa disave
    #jangan lupa ditampilkan

    #pic.transpose(Image.ROTATE_180)

    pic_a = pic.filter(ImageFilter.BLUR)
    pic_a.save('blured.jpg')
    pic_a.show()

    pic_b = pic.transpose(Image.ROTATE_180)
    pic_b.save('up.jpg')
    pic_b.show()

    pic_c = Image.FLIP_LEFT_RIGHT ("flip left and right places")
    pic_c.save(mirrow.jpg)
    pic_c.show()

    pic_k = ImageEnhance.Contrast(pic_original)
    pic_k = pic_contrast.enhance(1.5)
    pic_k.save(contr.jpg)
    pic_k.show()

#connect PIL modules 

#create ImageEditor class

    #create class constructor 

    #create "open and show" method

    #create methods to edit the original

#create object of the ImageEditor class with the data of original-pictures

#edit the image and save the result