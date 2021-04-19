from github import Github
import urllib
import datetime as dt
import json


url = "https://gist.githubusercontent.com/agbragin/47e66aaa1232d2cc6478821d18203e90/raw/b428fdb651c93c3eb9a03fa8da9a57a7aa24e835/Awsome%2520Pipeline%2520Repositories"
f = urllib.request.urlopen(url)
addrs = ['/'.join(line.decode("utf-8").replace("\n", "").split('/')[-2:]) for line in f]

with open("user.json", "r") as user_file:
    user = json.load(user_file)
g = Github(user['token'])

cnts = 0
start = dt.datetime(year=2016, month=1,day=1,hour=0,minute=0)
end = dt.datetime(year=2016, month=12,day=31,hour=23,minute=59)

for i, addr in enumerate(addrs):
    try:
        repo = g.get_repo(addr)
        cnts += repo.get_commits(sha="master", since=start, until=end).totalCount
        print("Progress: {}; counts: {}.".format(float(i+1)/len(addrs), cnts), end="\r")
    except Exception as e:
        print("#  {}".format(e))
        print("#  {} was not processed.".format(addr))
        pass

print("Counts: {}.".format(cnts))