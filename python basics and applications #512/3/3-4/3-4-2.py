import requests
import re


urls = set(re.findall(r"(?:.*)?(?:<a(?:.*)? href=[\"\'])(?:\w+://)?(\w[\w\.-]*)", requests.get(input()).text))
print('\n'.join(sorted(urls)))