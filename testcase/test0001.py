import requests

def printok(responses):
    print("\n--------")
    print(responses.status_code)

    for i,j in responses.headers.items():
        print(f'{i} : {j}')

    print('')

    print(responses.content.decode('utf8'))

response = requests.post("http://127.0.0.1/api/mgr/signin",
                            data={
                                "username" : "byhy",
                                "password" : "88888888"
                            }
                            )

printok(response)