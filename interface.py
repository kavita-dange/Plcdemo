from flask import Flask, jsonify, render_template, request
import config
from utils import placement

app = Flask(__name__)

@app.route('/')
def placement_model():
    print('Welcome to Job Placement Model')
    return render_template('home.html')
    #return 'my web page'


@app.route('/prediced_placement',methods = ['GET','POST'])
def get_predicted_placement():
    if request.method == 'POST':
        print('We are using POST Method')
        data = request.form
        print(data,'mydata')
        
        gender =data['gender']
        print('gender',gender)

        ssc_percentage = eval(data['ssc_percentage'])
        print('ssc_percentage',ssc_percentage)

        ssc_board =data['ssc_board']
        print('ssc_board',ssc_board)

        hsc_percentage = eval(data['hsc_percentage'])
        print('hsc_percentage',hsc_percentage)

        hsc_board =data['hsc_board']
        print('hsc_board',hsc_board)

        hsc_subject =data['hsc_subject']
        print('hsc_subject',hsc_subject)

        degree_percentage = data['degree_percentage']
        print('degree_percentage',degree_percentage)

        undergrad_degree = data['undergrad_degree']
        print('undergrad_degree',undergrad_degree)

        work_experience = data['work_experience']
        print('work_experience',work_experience)

        emp_test_percentage = eval(data['emp_test_percentage'])
        print('emp_test_percentage',emp_test_percentage)

        specialisation = data['specialisation']
        print('specialisation',specialisation)

        mba_percent = data['mba_percent']
        print('mba_percent',mba_percent)
              
        print(f'gender >> {gender}, ssc_percentage >> {ssc_percentage}, ssc_board >> {ssc_board}, hsc_percentage >> {hsc_percentage}, hsc_board >> {hsc_board}')
        med_ins = placement(gender, ssc_percentage, ssc_board, hsc_percentage, hsc_board,hsc_subject, degree_percentage,
        undergrad_degree,work_experience, emp_test_percentage, specialisation,mba_percent)
        plc = med_ins.get_predicted_placement()
        #return jsonify({'Result':f"Predicted student placement is: {plc}"})
        return render_template('index.html',plc = med_ins.get_predicted_placement())

    else:
        print('We are in POST Method')
        input_data = request.form
        print('INPUT DATA >> ', input_data)
        gender =input_data['gender']
        ssc_percentage = input_data['ssc_percentage']
        ssc_board = input_data['ssc_board']
        hsc_percentage = input_data['hsc_percentage']
        hsc_board =input_data['hsc_board']
        hsc_subject =input_data['hsc_subject']
        degree_percentage = input_data['degree_percentage']
        undergrad_degree = input_data['undergrad_degree']
        work_experience = input_data['work_experience']
        emp_test_percentage = input_data['emp_test_percentage']
        specialisation = input_data['specialisation']
        mba_percent = input_data['mba_percent']
        #print(f'age >> {age}, sex >> {sex}, bmi >> {bmi}, children >> {children}, smoker >> {smoker}, region >> {region}  ')
        med_ins1 = placement(gender, ssc_percentage, ssc_board, hsc_percentage, hsc_board,hsc_subject, degree_percentage,
        undergrad_degree,work_experience, emp_test_percentage, specialisation,mba_percent)
        plc = med_ins1.get_predicted_placement()
        #return jsonify({'Result':f"Predicted student placement is: {plc1}"})
        return render_template('index.html',plc = med_ins1.get_predicted_placement())



if __name__ == '__main__':
   app.run(host='0.0.0.0', port = config.PORT_NUMBER, debug= True) 
   #app.run(debug=False)   