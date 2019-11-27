from PIL import Image
from tesserocr import PyTessBaseAPI, RIL, iterate_level
import pandas as pd


def scale_image(img):

    width, height = img.size
    new_size = width*6, height*6
    img = img.resize(new_size, Image.LANCZOS)
    img = img.convert('L')
    resized = img.point(lambda x: 0 if x < 128 else 255, '1')
    return resized



def find_word_attribute(image,tessdata_3_path):

    #Reading image
    raw_img = Image.open(image)

    #Scaling image
    img = scale_image(raw_img)

    #Initializing parameters
    word_arr = [];bold_arr = []

    #Using TessBaseAPI to read the fond attribute
    with PyTessBaseAPI(path= tessdata_3_path) as api:
            api.SetImage(img)
            api.Recognize(0)

            #print(api.GetUTF8Text())
            ri = api.GetIterator()
            level = RIL.WORD
            for r in iterate_level(ri, level):
                bb = r.BoundingBox(level)
                if bb != None :
                    word = r.GetUTF8Text(level)
                    #word_arr.append(word)

                    font_name = r.WordFontAttributes()
                    #attr.append(font_name)

                    if word!=None and font_name!=None:
                        word_arr.append(word)
                        bold_arr.append(font_name)

                    Lang_name = r.WordRecognitionLanguage()
                    bool_value = r.WordIsFromDictionary()
                    conf = r.Confidence(level)

            df1 = pd.DataFrame(word_arr)
            df2 = pd.DataFrame(bold_arr)
            df = pd.concat([df1, df2], axis=1)
            df.rename(columns={ df.columns[0]: "Word" }, inplace = True)

    return(df)


print(find_word_attribute("1.png", "C:\\Program Files\\Tesseract-OCR\\tessdata_version\\tessdata-3.04.00"))
