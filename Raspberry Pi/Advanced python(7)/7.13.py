import re
import urllib.request

regular_expression = '(#[/d,]+) in Books'
url = 'https://www.amazon.com/Raspberry-Pi-Cookbook-Software-Solutions/dp/1492043222/'

print("The Amazon rank of Raspberry pi cookbook is: ")
text = urllib.request.urlopen(url).read().decode('utf-8')
print(re.search(regular_expression,text).group())
