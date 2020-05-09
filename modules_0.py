
import datetime
from time import time
today = datetime.date.today()
print('Curr Date is ', today)

t = time()
print('Curr Time is ', t)

# do pip3 install camelcase
# import installed module

import camelcase
camel = camelcase.CamelCase()
text = 'hello, how are u doing'

print(camel.hump(text))



