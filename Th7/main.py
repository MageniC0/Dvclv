import json,re
with open("0.json","r") as file: n = json.load(file)

while True:
    inp = input(str(n)+"_")
    
    if match := re.match(r"(\w+)\s+(\w+)\s+(\d+)", inp):
        name, IP, follow = match.groups()
        follow = int(follow)
        with open(str(n)+".json","w") as file : json.dump({"name":name,"IP":IP,"follow":follow},file)
        
        n = n + 1
        with open("n","w") as file: json.dump(n,file)
    
    else:
        break

print("done.")
