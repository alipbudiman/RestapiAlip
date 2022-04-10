from RestApiFXG import *

client = RestfulAPI()
ret = client.RandomProfile()
client.JsonPrint(ret)