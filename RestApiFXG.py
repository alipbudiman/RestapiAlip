import requests, json

class RestfulAPI():
    def __init__(self, apikey=None):
        self.host       = 'https://fxgapi.azurewebsites.net/'
        self.github     = 'https://github.com/alipbudiman/RestApiFXG'
        self.ver        = '1.6'
        self.getreq     = requests.get
        self.postreq    = requests.post
        self.apikey     = apikey
        self.CheckUpdate()
    
    def JsonPrint(self, data):
        print(json.dumps(data, indent=4, sort_keys=True))

    def CheckUpdate(self):
        path = "/apiver.html"
        try:
            x = json.loads(self.getreq("https://fxgdev.site"+path).text)
            if self.ver != x["Version"]:
                print("UPDATE AVAILABLE !!! \n| Current version : "+self.ver+"\n| Available version : "+x["Version"]+f"\n| Visit github : {self.github}")
            else:
                print(" WELCOME TO FXG FREE REST API\n | Current version : "+x["Version"])
                if self.apikey != None:
                    print(" | Login as PRremium users")
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def getHarrasword(self):
        path = "/harrasword"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def postHarrasword(self, word, reason):
        path = "/harrasword/add"
        try:
            params = {
                'push':word,
                'reason':reason
            }
            x = self.postreq(self.host+path, params=params).json()
            return x
        except Exception as e:
            print(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def pushPin(self, pin, request_auth=False):
        path = "/pushpin"
        try:
            params = {
                "data":pin
            }
            if request_auth != False:
                params["request_auth"] = str(request_auth)
            x = self.postreq(self.host+path, params=params).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def LineAuthKeyCon(self, key):
        path = "/authkey2primary"
        try:
            params = {
                'authkey':key
            }
            x = self.postreq(self.host+path, params=params).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def SimiSimiChat(self, chat, language):
        path = "/simi"
        try:
            params = {
                'chat':chat,
                'language':language
            }
            x = self.postreq(self.host+path, params=params).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def DownloadAnime(self, link):
        path = "/animeindovideo"
        try:
            params = {
                "link":link
            }
            x = self.getreq(self.host+path, params=params).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def ListAnime(self):
        path = "/listanimeindo"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def DetailAnime(self, query):
        path = "/detailanimeindo"
        try:
            params = {
                "query":query
            }
            x = self.getreq(self.host+path, params=params).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def NewAnime(self):
        path = "/newanimeindo"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def CostumizeUrl(self, query, urllink):
        path = "/costumizeurl"
        try:
            params = {
                "query":query, 
                "urllink":urllink 
            }
            x = self.getreq(self.host+path, params=params).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def DoujinDownloader(self, links):
        path = "/doujindownloader"
        try:
            params = {
                "links":links
            }
            x = self.getreq(self.host+path, params=params).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def DoujinNews(self):
        path = "/doujinnews"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def RandomQuotesEN(self):
        path = "/randomquotesen"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def RandomQuotesID(self):
        path = "/randomquotesid"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def RandomQuotesID(self):
        path = "/randomquotesid"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def TebakGambar(self):
        path = "/tebakgambar"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def RandomProxy(self):
        path = "/randomproxy"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def NekosRandomImage(self):
        path = "/nekosrandomimage"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    def RandomFact(self):
        path = "/randomfact"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def RandomCat(self):
        path = "/randomcatascii"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def RandomHentai(self):
        path = "/randomhentai"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def PokemonData(self):
        path = "/pokemondata"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def RandomProfile(self):
        path = "/randomprofile"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")
    
    def StatusApi(self):
        path = "/status"
        try:
            x = self.getreq(self.host+path).json()
            return x
        except Exception as e:
            raise Exception(f"Api Exception Error: [map] {path} [detail] {e}")