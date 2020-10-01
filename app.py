from flask import Flask, render_template, redirect, request
app =Flask(__name__)



@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/about')
def about():
	name='Rohit'
	number='889-778-9656'
	mylist=['apple','mango','banana']
	mydict = {"brand": "Ford","model": "Mustang","year": 1964}
	return render_template('about.html', name=name,number=number,mylist=mylist,mydict=mydict)

@app.route('/send/<string:name>/<string:number>/<string:mylist>/<string:mydict>')
def collect(name,number,mylist,mydict):
	print()
	print("my data are:")
	print(name)
	print(number)
	print("MY list items are ")
	print(mylist)
	"""for i in  range(0,len(mylist)):
		print(mylist[i],end='')"""

	print("MY dictionary values are ")
	print(mydict)
	"""for i in  mydict:
		print(i,end='')"""

	return render_template('index.html')



if __name__ == '__main__':
	app.run(debug=True)
     