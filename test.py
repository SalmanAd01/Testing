# from dotenv import load_dotenv
import os
os.environ['TEST']='TESTING'
# load_dotenv()
user_name=os.getenv('VAR')
print(user_name)
print(os.environ['TEST'])