from bs4 import BeautifulSoup

# 原始 HTML 程式碼
html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

# 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(html_doc, 'html.parser')

#去蕪存菁，先去網路上面檢查
titile_lists = soup.select('div,r-ent div.title a')
#print(soup.prettify())
#print(soup.find_all('a'))
