import requests,json

class Webapi:

    def _printres(slef,response):
        print("------start--------")
        print(response.status_code)
        print('')

        for i,j in response.headers.items():
            print(f'{i} : {j}')
        
        print(json.loads(response.content.decode('utf8')))


    def login(self,username="byhy",password="88888888"):
        response = requests.post("http://127.0.0.1/api/mgr/signin",
                            data={
                                "username" : username,
                                "password" : password
                            }
                            )
        
        self._printres(response)  

        return response


    def sessionright(self):
       
        self.session = requests.Session()
        response = self.session.post("http://127.0.0.1/api/mgr/signin",
                                    data={
                                        "username" : "byhy",
                                        "password" : "88888888"
                                    })

        self._printres(response)
        return response
    
    def get_customer(self,pagesize=10,pagenum=1):

        data = {
            "action" : "list_customer",
            "pagesize" : pagesize,
            "pagenum" : pagenum,
        }

        response = self.session.get("http://127.0.0.1/api/mgr/customers",params=data)
        self._printres(response)
        return response

    def customer_add(self,name="湖北武汉",phonenumber="153134321",address="china!"):
        jsondata = {
            "action":"add_customer",
            "data":{
                "name": name,
                "phonenumber": phonenumber,
                "address": address
    }    
        }
        response = self.session.post("http://127.0.0.1/api/mgr/customers",json=jsondata)
        self._printres(response)
        return response
    

    




api = Webapi()      #直接内部实例化