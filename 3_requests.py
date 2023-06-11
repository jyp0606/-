import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
# print("응답코드 :", res.status_code) #200이면 정상
# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("문제있음.[에러코드",res.status_code,"]")

res.raise_for_status() # 위에 if, else 쓴거랑 같음 
print(len(res.text))
print(res.text)
with open("mygoggle.html","w",encoding="utf8")as f:
    f.write(res.text)
    