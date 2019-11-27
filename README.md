# PyTessBaseAPI-Word-Attribute

Requirement:
a.Install Tesseract 4.x (link : https://github.com/tesseract-ocr/tesseract/wiki/4.0-with-LSTM )
b.Downlaod Tessdata 3.04 (link: https://github.com/tesseract-ocr/tessdata )

Save it to a folder

Then download or clone this repository and open detect_word_attribute.py,

The main function is detect_word_attribute()
This function takes 2 agrguments
1. The image file path
2. The Tessdata 3.04 path 

Go to the last line of the file and make changes to the function call parameters and run the code.

The function returns a dataframe of word attributes detected in the image passed.
