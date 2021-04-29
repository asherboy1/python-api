import requests,json

def printok1(response):
    print('-----start------\n')
    print(response.status_code)

    print('')

    for i,j in response.headers.items():
        print(f'{i} : {j}')
    
    print(response.content.decode('utf8'))
    if json.loads(response.content.decode('utf8'))["msg"] == "未登录":
        print('pipei')



jsondata = {
    "action" : "list_customer",
    "pagesize" : 3,
    "pagenum" : 1
}

session = requests.Session()

response = session.get("http://127.0.0.1/api/mgr/customers",params=jsondata)
printok1(response)