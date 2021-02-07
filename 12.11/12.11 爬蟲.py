import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Stock/index.html'
r = requests.get(url)
#print(r) 
#<Response [200] 
#可查詢http狀態碼(200-299都是成功)
# print(r.text) 
#會吐回網頁原始碼(但是沒有整理)
#<class str>

#透過BeautifulSoup，將字串解析成HTML格式
soup = BeautifulSoup(r.text,'html.parser')
#<class 'bs4.BeautifulSoup'>
#print(soup.prettify())
print(soup.select('.title a'))
titles = (soup.select('.title a'))
#沒有分段落不易讀取，用for做排序，印出來的是html格式，再用.text轉換成str
for title in titles:
    print(title.text,'\n')

#nrecs是每篇留言的討論人次，先抓出來
#nrecs = soup.select('.nrec') #全部都是html格式
#print(type(nrecs)) #<class 'bs4.element.ResultSet'>
    #print(nrec.select('span')) #用select的話就會變成字串，就不能再往下抓資料了

touchs = (soup.select('.hl.f3'))

for touch in touchs:
    print(touch.text)

# #題目 總留言數(nrec)，另外抓取推文、虛文各的總數，並且排列在一行之中