[![Version 1.6](https://i.ibb.co/6PknZws/1-3-6.png "Version 1.6")](https://fxgdev.site/restapialip.html)
[![LICENSE](https://i.ibb.co/drh936c/1-3-1.png "LICENSE")](https://github.com/alipbudiman/RestapiAlip/blob/main/LICENSE)
[![Supported python versions: 3.x](https://i.ibb.co/YDhJ8DC/1-3-2.png "supported python versions: 3.x")](https://www.python.org/downloads/)
[![Contact Author](https://i.ibb.co/HX6ts1F/1-3-4.png "contact author")](https://fxgdev.site/alifbudiman.html)

# RestapiAlip
Free Rest API for Bot, Website & anything
This API is Free to use under [CC Lisence](https://github.com/alipbudiman/RestapiAlip/blob/main/LICENSE)

You can [contact me](https://fxgdev.site/alifbudiman.html) for help this project or ask some question

Last update: 05/09/22

Version: 1.7

Host: https://fxgapi.azurewebsites.net


# Give Donation
https://saweria.co/alipbudiman

### STATUS API ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.StatusApi()
client.JsonPrint(ret)
```

### FIND IP ADRESS ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.GetIPAdress("your ip adress")
client.JsonPrint(ret)
```

### RANDOM PROFILE ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.RandomProfile()
client.JsonPrint(ret)
```
### POKEMON DATABASE ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.PokemonData()
client.JsonPrint(ret)
```

### RANDOM HENTAI ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.RandomHentai()
client.JsonPrint(ret)
```

### RANDOM CAT ASCII ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.RandomCat()
client.JsonPrint(ret)
```

### RANDOM CAT FACT ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.RandomFact()
client.JsonPrint(ret)
```

### NEKOS RANDOM IMAGE ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.NekosRandomImage()
client.JsonPrint(ret)
```

### RANDOM PROXY ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.RandomProxy()
client.JsonPrint(ret)
```

### TEBAK GAMBAR ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.TebakGambar()
client.JsonPrint(ret)
```

### RANDOM QUOTES ID ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.RandomQuotesID()
client.JsonPrint(ret)
```

### RANDOM QUOTES EN ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.RandomQuotesEN()
client.JsonPrint(ret)
```

### DOUJIN NEWS ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.DoujinNews()
client.JsonPrint(ret)
```

### DOUJIN DOWNLOADER ###

```PY
from RestApiFXG import *
client = RestfulAPI()
links = "input link nhentai here"
ret = client.DoujinDownloader(links)
client.JsonPrint(ret)
```

### FXG COSTUMIZE URL ###

```PY
from RestApiFXG import *
client = RestfulAPI()
FX_query = "input path name for your link here (query)"
FX_links = "input url link here (must http or https)"
ret = client.CostumizeUrl(FX_query,FX_links)
client.JsonPrint(ret)
```

### NEW ANIME SUB INDO ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.NewAnime()
client.JsonPrint(ret)
```

### DETAIL ANIME SUB INDO ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ani_name = "input anime name here"
ret = client.DetailAnime(ani_name)
client.JsonPrint(ret)
```

### LIST ANIME SUB INDO ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ret = client.ListAnime()
client.JsonPrint(ret)
```

### DOWNLOAD ANIME SUB INDO ###

```PY
from RestApiFXG import *
client = RestfulAPI()
ani_name = "input link anime indo here"
ret = client.DownloadAnime(ani_name)
client.JsonPrint(ret)
```

### SIMI-SIMI CHAT ###

```PY
from RestApiFXG import *
client = RestfulAPI()
chat = "input chat message (query)"
language = "input language here"
ret = client.SimiSimiChat(chat,language)
client.JsonPrint(ret)
```

### @LINE AUTHKEY CONVERTER ###

```PY
from RestApiFXG import *
client = RestfulAPI()
auth = "input your authkey here"
ret = client.LineAuthKeyCon(auth)
client.JsonPrint(ret)
```

### PUSH PINCODE NOTIFICATION TO WEBSITE ###

```PY
### RANDOM PATH
from RestApiFXG import *
client = RestfulAPI()
pincode = "input your pincode for upload to website here"
ret = client.pushPin(pincode)
client.JsonPrint(ret)
```

```PY
### REQUEST PATH
from RestApiFXG import *
client = RestfulAPI()
pincode = "input your pincode for upload to website here"
path = "input your path request here (query)"
ret = client.pushPin(pincode,path)
client.JsonPrint(ret)
```

### HARRASS WORD ###

```PY
### Request harras word for input into server
from RestApiFXG import *
client = RestfulAPI()
word = "input request harras word here"
reason = "input your reason why wa need input it into our server"
ret = client.postHarrasword(word,reason)
client.JsonPrint(ret)
```

```PY
### Get harras word data from server
from RestApiFXG import *
client = RestfulAPI()"
ret = client.getHarrasword()
client.JsonPrint(ret)
```

### GAMES FAMILY 100 ###

```PY
from RestApiFXG import *
client = RestfulAPI()"
ret = client.getFamily100Quiz()
client.JsonPrint(ret)
```


# ![logo](https://i.ibb.co/zJvVhJ3/Untitled-design-88.png)
Regards FXG-Dev

[www.fxgdev.site](https://fxgdev.site/)

[www.fxgdev.site/restapialip.html](https://fxgdev.site/restapialip.html)
