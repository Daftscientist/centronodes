# centronodes api
## How to install:
```py
Windows:
py -m pip install -U https://github.com/Daftscientist/centronodes/archive/0.3.tar.gz
```
```py
Linux/MacOS:
python3 -m pip install -U https://github.com/Daftscientist/centronodes/archive/0.3.tar.gz
```
## example
```py
import centronodes
from centronodes import Fun, UserInfo

ram = UserInfo.ram(user_id=491630879085559808)
print(ram)

disk = UserInfo.disk(user_id=491630879085559808)
print(disk)

cores = UserInfo.cores(user_id=491630879085559808)
print(cores)

servers = UserInfo.servers(user_id=491630879085559808)
print(servers)

coins = UserInfo.coins(user_id=491630879085559808)
print(coins)

duck = Fun.duck()
print(duck)```
