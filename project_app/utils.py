import pickle
import json
# import config
import numpy as np


class placement():
    

    def __init__(self,gender, ssc_percentage, ssc_board ,hsc_percentage,hsc_board,hsc_subject, degree_percentage,
                        undergrad_degree,work_experience, emp_test_percentage, specialisation,mba_percent):
        self.gender = gender
        self.ssc_percentage = ssc_percentage
        self.ssc_board = ssc_board
        self.hsc_percentage = hsc_percentage
        self.hsc_board = hsc_board
        self.hsc_subject = hsc_subject
        self.degree_percentage =  degree_percentage
        self.undergrad_degree =  undergrad_degree
        self.work_experience =  work_experience
        self.emp_test_percentage =  emp_test_percentage
        self.specialisation =  specialisation
        self.mba_percent =  mba_percent
        

    def load_model(self):
        with open(r'D:\Phython\Student\project_app\Logistic_Model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        
        with open(r'D:\Phython\Student\project_app\project_data.json', 'r') as f:
            self.json_data = json.load(f)

    def get_predicted_placement(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))
       # print('Test Array',test_array)
        test_array[0] = self.json_data['gender'][self.gender]
       # print('test_array[0]',test_array[0])
        test_array[1] = self.ssc_percentage
       # print('test_array[1]',test_array[1])
        test_array[2] = self.json_data['ssc_board'][self.ssc_board]
       # print('test_array[2]',test_array[2])
        test_array[3] = self.hsc_percentage
      #  print('test_array[3]',test_array[3])
        test_array[4] = self.json_data['hsc_board'][self.hsc_board]
       # print('test_array[4]',test_array[4])
        test_array[5] = self.json_data['hsc_subject'][self.hsc_subject]
       # print('test_array[5]',test_array[5])
        test_array[6] = self.degree_percentage
       # print('test_array[6]',test_array[6])
        test_array[7] = self.json_data['undergrad_degree'][self.undergrad_degree]
      #  print('test_array[7]',test_array[7])
        test_array[8] = self.json_data['work_experience'][self.work_experience]
      #  print('test_array[8]',test_array[8])
        test_array[9] = self.emp_test_percentage
      #  print('test_array[9]',test_array[9])
        test_array[10] = self.json_data['specialisation'][self.specialisation]
       #print('test_array[10]',test_array[10])
        test_array[11] = self.mba_percent
       # print('test_array[11]',test_array[11])
       # print('Test Array :', test_array)

        prediced_placement = self.model.predict([test_array])[0]
       # print('Student', prediced_placement)
        return prediced_placement

if __name__ == '__main__':
    gender='F'
    ssc_percentage=70
    ssc_board='Central'
    hsc_percentage=78
    hsc_board='Central'
    hsc_subject='Arts'
    degree_percentage=55
    undergrad_degree='Comm&Mgmt'
    work_experience='No'
    emp_test_percentage=66
    specialisation='Mkt&Fin'
    mba_percent=67
    med_ins = placement(gender, ssc_percentage, ssc_board, hsc_percentage, hsc_board,hsc_subject, degree_percentage,
    undergrad_degree,work_experience, emp_test_percentage, specialisation,mba_percent)
    get_predicted_placement()
