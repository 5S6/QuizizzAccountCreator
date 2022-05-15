import requests
from requests.structures import CaseInsensitiveDict
import json
import random
import time
import threading

usernameFile = open("usernames.txt", "w")
combofile = open("pass.txt", "w")

def namegen():
    length = random.randint(7, 15) # устанавливаем минимум и максимум (min, max)
    eval = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0",""


    return ''.join(random.choice(eval) for i in range(length))



def create():
  email = "AlekCodes"+ namegen() + "@gmail.com"
  url = "https://quizizz.com/_api/main/user/register"

  headers = CaseInsensitiveDict()
  headers["Content-Type"] = "application/json"

  data =              {"title":"","firstName":"hjkhkjh","lastName":"retretret","password":"ttnerktjerktjker","occupation":"student","preferences":{"communicationAllowed":"true"},"email":email ,"source":{"at":"landing_header"}}


  signup = requests.post(url,data = json.dumps(data),headers=headers)
  signup_data = json.loads(signup.text)
  username = signup_data['data']['user']['local']['username']
  combofile.write(email+ ":ttnerktjerktjker"+ "\n")
  usernameFile.write(username + "\n")
  print(username)
  print(email+ " :ttnerktjerktjker")

threads=[]


for i in range(100000):
  t = threading.Thread(target = create)
  t.Daemon = True
  threads.append(t)

for i in range(100000):
  threads[i].start()
  time.sleep(0.2)

for i in range(100000):
  threads[i].join()