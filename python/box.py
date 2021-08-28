import docx, os
os.chdir("C:/Users/userava/Desktop/crtat/python")
doc = docx.Document('crtat.docx')

#Добавление 3 предложений crtat и rus в переменную

#CRTAT
all_paras = doc.paragraphs
clear_text = ""
for para in all_paras:
    clear_text += para
print(clear_text)