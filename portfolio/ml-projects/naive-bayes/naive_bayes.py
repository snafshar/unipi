from collections import Counter
import math
def train(docs,labels):
 classes=sorted(set(labels)); vocab=set(w for d in docs for w in d.split()); counts={c:Counter() for c in classes}; totals=Counter()
 for d,c in zip(docs,labels): counts[c].update(d.split()); totals[c]+=len(d.split())
 def predict(doc):
  scores={c:math.log(labels.count(c)/len(labels)) for c in classes}
  for c in classes:
   for w in doc.split():scores[c]+=math.log((counts[c][w]+1)/(totals[c]+len(vocab)))
  return max(scores,key=scores.get)
 return predict
if __name__=='__main__':print(train(['good film','bad film'],['pos','neg'])('good'))
