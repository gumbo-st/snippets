import os
import json

CURDIR = os.getcwd()
DEVADDON = "/snippets/python/json/"
JSONPATH = CURDIR + DEVADDON
JSONFULLPATH = JSONPATH + "json_test.json"

with open(JSONFULLPATH) as read_file:
    data = json.load(read_file)

firstName = data["firstName"]
print("This dude named: " +firstName)

print("\nHas these rug rats:")
children = data["children"]
for ch in children:
    print(ch["name"] + ", age[" + str(ch["age"]) + "], notes[" + ch["notes"] + "]")

print("\nHow did he fine a woman with these issues?")
issues = data["issues"]
for issue in issues:
    print(issue)

#print(data)

