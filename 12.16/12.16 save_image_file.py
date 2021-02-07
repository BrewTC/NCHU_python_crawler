import requests

response = requests.get("https://i.imgur.com/ExdKOOz.png")

file = open("sample_image.png", "wb") #wb(write binary(圖片用))，w會覆蓋過以前的資歷
file.write(response.content)
file.close()

#另一種寫法,不用加close()
#with open("sample_image.png", "wb") as file:
#        file write(response.content)

#老師範例
# import requests

# response = requests.get("https://1.bp.blogspot.com/-VuG1F1OMijQ/XlPexuQgLzI/AAAAAAAABNs/6cyJ-15WBQU8Y6sXXltFoLDymg1jo2NjQCLcBGAsYHQ/s640/python_selenium.jpg")

# #w->wirte ; b->Binary(圖片用) ;t->text(一般文字用)
# # file = open("sample_image.png", "wb")
# # file.write(response.content)
# # file.close()

# #簡短的file處理方式，使用with，好處是最後不用close
# with open("sample_image.png", "wb") as file:
#     file.write(response.content)