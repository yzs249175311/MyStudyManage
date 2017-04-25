import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
}
# old_stdout = sys.stdout
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

response = requests.get("http://www.qiushibaike.com", headers=headers)
soup = BeautifulSoup(response.text, "lxml")
lists1 = soup.find_all('div', 'content')
# print(lists1)

f = open("c:/Users/yuanzishuai-pc/Desktop/f.txt", "w", encoding="utf-8")
print(lists1[0])
count = 1
for i in lists1:
    f.write(str(count))
    count += 1
    f.write(i.text)

f.close()
# lists2 = soup.find_all()
# print(lists2)
