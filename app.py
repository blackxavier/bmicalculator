from flask import Flask,render_template,request
import datetime
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def hello():
    now = datetime.datetime.now()
    if request.method == 'POST':
        
        try:
            weight = request.form.get('weight')
            height = request.form.get('height')
            newweight = float(weight)
            newheight = float(height)
            if (newheight and newheight) != str or (newheight or newheight) != str :
                result = round((newweight /((newheight/100) ** 2)),2)
                context = {
                    "now":now,
                    "result":result,
                    
                }
            
                return render_template('index.html',**context)
        


        except ValueError as error:
            result = False
            error = "You inputed the wrong value,kindly input an integer."
            return render_template('index.html',error=error)
    

    elif request.method == 'GET':
        return render_template('base.html')
        
        



if __name__ == "__main__":
    app.run(debug=True)


