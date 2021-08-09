import requests

print("#########################################################################################################################   ")
print(" ##   _____________      _____________       ______________  ______________  _______________________                    ##   ")
print("##  |    ____     \    |    ____     \     |              ||              ||                       |                   ##   ")
print(" ##  |   |    \     \   |   |    \     \    |   ________   ||   ________   ||________       ________|                   ##   ")
print("##  |   |     \     \  |   |     \     \   |  |        |  ||  |        |  |         |     |  ____________  _______     ##   ")
print(" ##  |   |     /      \ |   |     /      \  |  |        |  ||  |        |  |         |     | |            ||   _   \    ##   ")
print("##  |   |____/       / |   |____/       /  |  |        |  ||  |        |  |         |     | |   _________||  | \   \   ##   ")
print(" ##  |               /  |               /   |  |        |  ||  |        |  |         |     | |  |          |  |  |   \  ##   ")
print("##  |--------------/   |--------------/    |  |        |  ||  |        |  |         |     | |  |          |  |_/    /  ##   ")
print(" ##  |              \   |              \    |  |        |  ||  |        |  |         |     | |  |______    |        /   ##   ")
print("##  |    ____       \  |      ___      \   |  |        |  ||  |        |  |         |     | |   ______|   |     __/    ##   ")
print(" ##  |   |    \       \ |     |   \      \  |  |        |  ||  |        |  |         |     | |  |          |    _   \   ##   ")
print("##  |   |     \      / |     |    \      \ |  |        |  ||  |        |  |         |     | |  |          |   | \   \  ##   ")
print(" ##  |   |     /     /  |     |     |      ||  |________|  ||  |________|  |         |     | |  |_________ |   |  \   \ ##   ")
print("##  |   |____/     /   |     |     |      ||              ||              |         |     | |            ||   |   |   |##   ")
print(" ##  |_____________/    |_____|     |______||______________||______________|         |_____| |____________||___|   |___|##   ")
print("#########################################################################################################################   ")
print(" #########################################################################################################################   ")
print("#########################################################################################################################   ")
print(" ##                                                                                                                     ##   ")
print("## ========> Created by DarkSkull134    =========> Created on 6/8/21                                                   ##   ")
print(" ##                                                                                                                     ##   ")
print("## ========> This code is specially written to help others in enumeraing websites.                                     ##   ")
print(" ##                                                                                                                     ##   ")
print("## ********> Disclaimer : The creator is not responsible for any illegal activities by any user.                       ##   ")
print(" ## ********> The user is wholly responsible for his own actions.                                                       ##   ")
print("## ********> Note : This tool is opensource, meaning that anyone can use this tool.                                    ##   ")
print(" ##                                                                                                                     ##   ")                                                                                                                    
print("#########################################################################################################################   ")
print("#########################################################################################################################   ")


domain = input("\n\n\n\nType domain to enumerate (http(s)://www.exampleurl.com):          ")

# checking .com and adding it
if "." not in domain:
  domain = domain + ".com"
  print(domain)

# checking http(s) and adding it
if "http://" not in domain and "https://" not in domain:
  domain ="http://" + domain

print("\nStarting attack on target : {}".format(domain))
print("\n\nThis may take a while...")
print("\n\n")

# reading from wordlist and storing in content

wordlist = input('Type location to wordlist file:    ') 

with open(wordlist) as f:
    contents = f.read()
    content = contents.split('\n')

# checking all wordlists
for num, subdir in enumerate(content):
  url = domain + "/{}".format(content[num]) 
  
  r = requests.get(url)

  if r.status_code != 404:
    print(f"url {url} found ; status code : {r.status_code}")
