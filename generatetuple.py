# -*- coding: UTF-8 -*-
matching_company_stud_dict={
'Company 1':[
'Alex',
'Bob',
'Caroline',
'Doris',

],

'Company 2':[
'Alex',
'Caroline',
'Fredrik',
],

'Company 3':[
'Alex',
'Bob',
'Edward',
]
}

normal_times=['09:00','10:00','11:00']

company_3_special_times=['10:00','11:00','13:00']

interviewtimes={}
interviewtimes={
'Company 1':normal_times,
'Company 2':normal_times,
'Company 3':company_3_special_times
}

students_special_time={
'Alex':['10:00','11:00','13:00']
}

f = open("ks.txt","w+")
for company in matching_company_stud_dict:
    for student in matching_company_stud_dict[company]:
        if student in students_special_time:
            for time in students_special_time[student]:
                f.write("('"+student+"'," + "'"+company+"'," +"'" +time+"'),\n")
        else:
            for time in interviewtimes[company]:
                f.write("('"+student+"'," + "'"+company+"'," +"'" +time+"'),\n")


f.close()
