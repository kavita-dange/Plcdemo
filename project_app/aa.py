from flask import Flask, jsonify, render_template, request
# import config

app = Flask(__name__)

@app.route('/')
def placement_model():
    print('Welcome to Job Placement Model')
    # return render_template('home.html')
    return 'my web page'


@app.route('/prediced_placement',methods = ['GET','POST'])
def get_predicted_placement():
    if request.method == 'GET':
        print('We are using POST Method')
        data = request.form
        print(data,'mydata')
        return 'ABCD'
    
    else:
        print('We are in post method')
        return 'EFGH'
if __name__ == "__main__":
    app.run()