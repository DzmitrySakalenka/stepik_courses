import re
import requests


url1, url2 = input(), input()
hrefs = lambda url: re.findall(r'<a .*?\bhref="(.*?)"', requests.get(url).text)
print('Yes' if any(b == url2 for a in hrefs(url1) for b in hrefs(a)) else 'No')