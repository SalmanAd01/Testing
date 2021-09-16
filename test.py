from dotenv import load_dotenv
import os
os.environ['TEST']='TESTING'
load_dotenv()
user_name=os.environ.get('TOKEN')
print(user_name)
print(os.environ['TEST'])
