import urllib.request,urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url=input('ENTER XML LINK-')
# html=urllib.request.urlopen(url,context=ctx).read()
# soup=BeautifulSoup(html,'html.parser')
#
# sum=0
# tags=soup('count')
# for tag in tags:
#     sum+=int(tag.contents[0])
# print(sum)

sum=0
url=input('ENTER XML LINK-')
html=urllib.request.urlopen(url,context=ctx).read()
tree=ET.fromstring(html)

lst=tree.findall('comments/comment')
for i in lst:
    sum +=int(i.find('count').text)
print(sum)
