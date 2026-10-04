from django.shortcuts import render
from student.models import Profile
def showdata(req): 
    #modelclassname.objects.all()  # This line is commented out,but it is used to fetch all the records from the database for the specified model class. 
    #modelclassname.objects.get(pk = ) this line is commented out, but it is used to fetch a single record from the database based on the primary key (pk) value provided.(id) will work the same way as pk.
    #modelclassname.objects.get(colname=value) this line is commented out, but it is used to fetch a single record from the database based on the specified column name and its corresponding value.
    all_students = Profile.objects.all()
    print(all_students)
    return render(req, 'student/data.html', {'students': all_students})
