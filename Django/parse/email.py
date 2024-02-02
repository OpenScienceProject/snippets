import email
from email import policy
from email.parser import BytesParser
import glob

file_list = glob.glob('*.eml') # returns list of files
with open(file_list[0], 'rb') as fp: # select a specific email file from the list
    msg = BytesParser(policy=policy.default).parse(fp)
    print(msg['From'])
    print(msg['To'])
    print(msg['Subject'])
    print(msg['Date'])
    