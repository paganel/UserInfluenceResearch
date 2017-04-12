#coding=utf-8
import pandas as pd
import pynlpir
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# chunks = pd.read_csv('H:\\SMPData\\Weibo.Corpus\\Weibo.data\\merge\\weibodata.csv',iterator = True)
# chunk = chunks.get_chunk(100)
# print
'''
To read data from weibodata.csv and group the weibo txt by user,what's more,write everyone's weibo contents in a single file
'''
loop = True
chunkSize = 10000
chunks = []
index=0
reader=pd.read_csv('H:\\SMPData\\Weibo.Corpus\\Weibo.data\\merge\\weibodata.csv',iterator = True)
while loop:
  try:
    chunk = reader.get_chunk(chunkSize)
    chunks.append(chunk)
    index=index+1
    print "Iteration %d"%(index)
    if index>499 :
      loop = False
  except StopIteration:
    loop = False
    print "Iteration is stopped."
df = pd.concat(chunks, ignore_index=True)
df.columns=['id','reports','comments','source','time','text']
# print df['text'][0:10]
group=df['text'].groupby(df['id'])
# print group.size()
for i,j in group:
  # print i
  # print('-------')
  text=j.values
  # print text
  file_name="F:\\Git Repository\\500w_user_content\\"+str(i)+"_content.txt"
  with open(file_name,"w") as f:
    for x in text:
      f.write(str(x))

# phase=[]
# for i in range(0,11):
#   phase.append(df['text'][i])
# a=' '
# phase=a.join(phase)
# print phase
#
# pynlpir.open()
# result=pynlpir.segment(phase,pos_tagging=False)
# pynlpir.close()
# print result
