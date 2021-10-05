def read_csv(f):
	f=open(f).read().strip().split("\n")
	df={}
	cols=f[0].split(',')
	f=f[1:]
	for i,rows in enumerate(f):
		rows=rows.split(',')
		for col,row in zip(cols,rows):
			df.setdefault(col,[])
			df[col].append(row)
	return df
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
def col_names(df):
	return list(df.keys())
def dict_at(df,i):
	rows=row_at(df,i)
	cols=col_names(df)
	return dict(zip(cols,rows))
def row_at(df,i):
	l=[]
	for col in col_names(df):
		l.append(df[col][i])
	return l
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
		
	
	
	
df=read_csv('blackfriday.csv')
#1.
print(f"{1:=^50}")
uids=group(df,"User_ID")
print(len(uids))
#2.
print(f"{2:=^50}")
genders=group(df,"Gender")
print(len(genders['M']['User_ID']))
print(len(genders['F']['User_ID']))
#3.
print(f"{3:=^50}")
total=0
uids={}
for u,g,p in zip(df['User_ID'],df['Gender'],df['Purchase']):
	if g=='F':
		uids[u]=None
		total+=float(p)
ans=total/len(uids)
print(ans)
#4.
print(f"{4:=^50}")
amount=df["Product_Category_1"]
count={}
for i in amount:
	count.setdefault(i,0)
	count[i]+=1
for k,v in sorted(count.items(),key=lambda x:int(x[0])):
	print(k,v/len(amount)*100)
#4.2
print(f"{5:=^50}")
max_3=sorted(count.items(),key=lambda x:int(x[1]),reverse=True)[0:3]
for k,v in max_3:
	print(k,v)
#5.
print(f"{5:=^50}")
print(sum(max_3))