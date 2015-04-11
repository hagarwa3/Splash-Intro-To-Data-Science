

import csv

class campaign:
    
    def __init__(self, name, id, adnet, dsp, direct, total, adnp, dspp, dirp):
        self.name=name
        self.id=id
        self.adnet=float(adnet)
        self.dsp=float(dsp)
        self.direct=float(direct)
        self.total=self.adnet+self.dsp+self.direct
        self.adnp=self.adnet/float(self.total) if self.total!=0 else 0.0
        self.dspp=self.dsp/float(self.total) if self.total!=0 else 0.0
        self.dirp=float(self.direct/float(self.total)) if self.total!=0 else 0.0
        
        
    def pr(self):
        print "["+self.name+", "+self.id+", "+str(self.adnet)+", "+str(self.dsp)+", "+str(self.direct)+", "+str(self.total)+", "+str(self.adnp)+", "+str(self.dspp)+", "+str(self.dirp)+"]"
        
        

class site(campaign):
    def __init__(self, name, camps, total):
        self.name=name
        self.camps=camps
        self.total=total
    def pri(self,i):
        print self.camps[i].name

#store campaigns
adn=site("adnet",[],0)
ds=site("dsp", [], 0)
dire=site("dire", [], 0)
tot=site("total", [], 0)
empty=site("empty", [], 0)

#store all campaigns
pains=[]

with open('C:\Users\Harshit Agarwal\Desktop\Splash course material\Adomicdata.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        pains.append(campaign(row[0], row[1],row[2],row[3], row[4], 0, 0, 0, 0, ))
        
    for i in range(0,len(pains)):
        #pains[i].pr()
        if pains[i].adnet>0:
            adn.camps.append(pains[i])
            adn.total=adn.total+pains[i].adnet
        if pains[i].dsp>0:
            ds.camps.append(pains[i])
            ds.total=ds.total+pains[i].dsp
        if pains[i].direct>0:
            dire.camps.append(pains[i])
            dire.total=dire.total+pains[i].direct
        if pains[i].total>0:
            tot.camps.append(pains[i])
            tot.total=tot.total+pains[i].total
        if pains[i].total==0:
            empty.camps.append(pains[i])
        #print i
    ''' 
    for i in range(0, len(empty.camps)):
       adn.camps[i].pr()
       empty.pri(i)
       print i
    '''
    print tot.total
    print ds.total
    print dire.total
    print adn.total
    