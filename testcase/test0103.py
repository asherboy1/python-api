import requests,json

def printres(response):
    print("------start--------")
    print(response.status_code)
    print('')

    for i,j in response.headers.items():
        print(f'{i} : {j}')
    
    print(json.loads(response.content.decode('utf8')))




data = {
    "action" : "list_customer",
    "pagesize" : 10,
    "pagenum" : 1
}

session = requests.Session()
response1 = session.post("http://127.0.0.1/api/mgr/signin",
                            data={
                                "username" : "byhy",
                                "password" : "88888888"
                            })

printres(response1)

response2 = session.get("http://127.0.0.1/api/mgr/customers",params=data)
printres(response2)