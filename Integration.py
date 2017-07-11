from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def index():
        render_template('homepage.html')
        
        datafile = request.form['datafile']




        return render_template('datafile.html', datafile=datafile)







if __name__ == "__main__":
    app.run(debug=True)



