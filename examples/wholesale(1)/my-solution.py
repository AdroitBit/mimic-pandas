def read_csv(f):
	f=open(f).read().strip().split("\n")
	df={}
	cols=f[0].split(',')
	f=f[1:]
	for i,rows in enumerate(f):
		rows=rows.split(',')
		for col,row in zip(cols,rows):
			df.setdefault(col,[])
			df[col].append(float(row))
	return df
def col_names(df):
	return list(df.keys())
	
def dict_from(df):
	d=[]
	for i in range(row_size(df)):
		d.append(dict_at(df,i))
	return d
def df_from(l):#list of dict
	df={}
	for d in l:
		for k,v in d.items():
			df.setdefault(k,[])
			df[k].append(v)
	return df
def col_size(df):
	return len(col_names(df))
def row_size(df):
	return len(df[col_names(df)[0]])
def group(df,by_col):
	cols=col_names(df)
	r={}
	for i,gk in enumerate(df[by_col]):
		#gk group key
		r.setdefault(gk,{})
		for col in cols:
			r[gk].setdefault(col,[])
			r[gk][col].append(df[col][i])
	return r
	
	
def dict_at(df,i):
	rows=row_at(df,i)
	cols=col_names(df)
	return dict(zip(cols,rows))
def row_at(df,i):
	l=[]
	for col in col_names(df):
		l.append(df[col][i])
	return l


df=read_csv("wholesale.csv")
#create total sale column
df['total sale']=[]
sale_column='Fresh Milk Grocery Frozen Detergents_Paper Delicassen'.split()
for i in range(row_size(df)):
	df['total sale'].append(0)
	for col in sale_column:
		df['total sale'][i]+=df[col][i]



#1.แปลง
print(f"{1:=^50}")
for i in range(row_size(df)):
	mapper={
		1.0:'Horeca',
		2.0:'Retail'
	}
	df['Channel'][i]=mapper[df['Channel'][i]]
	mapper={
		1.0:'Lisnon',
		2.0:'Oporto',
		3.0:'Other'
	}
	df['Region'][i]=mapper[df['Region'][i]]
#2.หายอดขายรวม
print(f"{2:=^50}")
for col in sale_column:
	print(col,sum(map(int,df[col])))
#3.
print(f"{3:=^50}")
g=group(df,'Region')
for gk,ndf in g.items():
	s=0
	for col in sale_column:
		s+=sum(map(int,ndf[col]))
	print(gk,s)
#4.
print(f"{4:=^50}")
g=group(df,'Region')
for gk,ndf in g.items():
	print(gk)
	gi=group(ndf,'Channel')
	print('Horeca',sum(gi['Horeca']['total sale']))
	print('Retail',sum(gi['Retail']['total sale']))
	print()
#5.
print(f"{5:=^50}")
g=group(df,'Channel')
ndf=g['Horeca']
ans=0
for i in range(row_size(ndf)):
	if ndf['Fresh'][i]+ndf['Frozen'][i]<=1000:
		ans+=1
print(ans)
#6.
print(f"{6:=^50}")
g=group(df,'Region')
for gk,ndf in g.items():
	g[gk]=(sum(ndf['Milk']),ndf)
max_key=max(g,key=g.get)
print(max_key,g[max_key][0])
ndf=g[max_key][1]
ans=0
for i,j in zip(ndf['Milk'],ndf['Fresh']):
	if i>j:
		ans+=1
print(ans)