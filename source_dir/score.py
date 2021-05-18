import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
from azureml.core.model import Model
np.seterr(divide = 'ignore')

maxlen=53
start_stop_chars=['@','$']

def X_from_str(txt,tokens,start_stop_chars,maxlen):
  A=[]
  for t in txt:
    X=[tokens[start_stop_chars[0]]]
    for c in t:
      X.append(tokens[c])
    A.append(X)
  return pad_sequences(A,maxlen)

def str_from_X(X,tokenchar):
  wordparts=[]
  for a in X:
    wordparts.append(''.join([tokenchar[i] for i in a[a>0]][1:]))
  return wordparts

def sampler(x,method='standard',temperature=1.0):
  if method=='standard':
    thetoken=np.argmax(x)
  if method == 'temperature':
    x = np.log(x) / temperature
    exp_x = np.exp(x)
    x = exp_x / np.sum(exp_x)
    thetoken=np.argmax(np.random.multinomial(1,x*0.99999,1))
  return thetoken

def autocomplete(txt,tokens,tokenchar,start_stop_chars,maxlen,samplingmethod='standard',temperature=1.0,debug=True):
  placenames=[]
  for sn in txt:
    nextchar=''
    while nextchar != start_stop_chars[1]:
      output=model.predict(X_from_str([sn],tokens,start_stop_chars,maxlen))[0]
      nextchar=tokenchar[sampler(output,method=samplingmethod,temperature=temperature)]
      sn+=nextchar
      if debug:
        print(sn)
    sn=sn[:-1]
    placenames.append(sn)
  return placenames


def init():
    global model
    global tokens
    global tokenchar
    tfmodelfn = Model.get_model_path('stadnamn_model1')
    print(tfmodelfn)
    model=keras.models.load_model(tfmodelfn)
    tokenfn=tfmodelfn+"/assets/tokens.json"
    with open(tokenfn,'r') as fh:
        tokens=json.load(fh)
    tokenchar=dict([(v,k) for k,v in tokens.items()])

def run(data):
    datad = json.loads(data)
    texts=datad.get('texts',[])
    samplingmethod=datad.get('samplingmethod','standard')
    temperature=datad.get('temperature',1.0)
    placenames=autocomplete(texts,tokens,tokenchar,start_stop_chars,maxlen,samplingmethod=samplingmethod,temperature=temperature,debug=False)
    return(json.dumps({'placenames':placenames},ensure_ascii=False))
