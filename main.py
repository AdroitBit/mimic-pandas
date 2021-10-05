def convertive(a):#convert string to something reasonable.can be disable in read_csv
	try:
		try:
			return int(a)
		except:
			return float(a)
	except:
		return a
def read_csv(f):
	#pandas' dataframe is similar to dictionary
	#1.kept key as column
	#2.value of key is list of data
	"""{
		'gender':['Male','Male'],
		'name':['Ricardo','Kazuya']
	}
	"""
	f=open(f).read().strip().split('\n')
	df={}
	cols=f[0].split(',')
	f=f[1:]
	for i,rows in enumerate(f):
		rows=rows.split(',')
		for col,row in zip(cols,rows):
			df.setdefault(col,[])
			df[col].append(convertive(row))
	return df
def col_names(df):#equivalent to df.header()
	return list(df.keys())
def col_size(df):#len(df.header())
	return len(col_names(df))
def row_size(df):#=len(df.index)=df.shape[0]=df[df.columns[0]].count()
	return len(df[col_names(df)[0]])
def group(df,by_col):#=df.groupby(...)
	#df={'gender':['F','M','F','M','F','F'],'name':['A','B','C','D','E','F']}
	#g=group(df,by_col='gender')
	#g will be
	"""
		{
			'F':{'gender':['F','F','F','F'],'name':['A','C','E','F']},
			'M':{'gender':['M','M'],'name':['B','D']}
		}
	"""
	cols=col_names(df)
	r={}
	for i,gk in enumerate(df[by_col]):
		r.setdefault(gk,{})
		for col in cols:
			r[gk].setdefault(col,[])
			r[gk][col].append(df[col][i])
	return r
