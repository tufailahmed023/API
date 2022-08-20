from flask import Flask ,request,jsonify
app=Flask(__name__)

@app.route('/abc',methods=['GET','POST'])
def test1():
    if (request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return  jsonify(str(result))
@app.route('/abc1',methods=['GET','POST'])
def test2():
    if (request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return  jsonify(str(result))

@app.route('/abc2',methods=['GET','POST'])
def test6():
    if (request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a-b
        return  jsonify(str(result))


@app.route('/abc3',methods=['GET','POST'])
def test3():
    if (request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a/b
        return  jsonify(str(result))


@app.route('/abc4',methods=['GET','POST'])
def test4():
    if (request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a**b
        return  jsonify(str(result))


@app.route('/abc5',methods=['GET','POST'])
def test5():
    if (request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a//b
        return  jsonify(str(result))

if __name__=='__main__':
    app.run()






def test(a,b):
    return a+b

print(test(4,5))