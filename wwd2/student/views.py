from django.shortcuts import render
from student.models import Student

def home(request):
    student_data = Student.objects.get(pk=1) # Return a single object
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('roll_number').first()
    # student_data = Student.objects.last()
    # student_data = Student.objects.order_by('roll_number').last()
    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.latest('pass_date', 'id') # Return the latest object based on pass_date and id ordering according to id DESC
    # student_data = Student.objects.earliest('pass_date')
    # student_data = Student.objects.all()
    # print(student_data.exists())
    # student_data = Student.objects.create(
    #     name = 'Nigga', roll = 18, city = 'Khandwa', marks=78, pass_date = '2026-05-07'
    # )
    # student_data, created = Student.objects.get_or_create(
    #     name = 'Nigga', roll = 18, city = 'Khandwa', marks=78, pass_date = '2026-05-07'
    # )
    # print(created)
    # student_data = Student.objects.filter(id=5).update(name='Nigga Tirole')
    # student_data, created = Student.objects.update_or_create(
    #     id=5,
    #     defaults={'name': 'HK Tirole', 'roll' : 22}
    # )
    # print(created)
    # print("Student Data:", student_data)
    # objs = [
    #     Student(name='John', roll = 12, city='NewYourk', marks=80, pass_date='2026-7-1'),
    #     Student(name='Danish', roll=34, city='Mumbai', marks=85, pass_date='2026-8-2'),
    #     Student(name='Aamir', roll=7, city='Delhi', marks=78, pass_date='2026-5-12'), 
    # ]
    # student_data = Student.objects.bulk_create(objs)  for bulk creation

    # for bulk updation
    # all_stu_data = Student.objects.all()
    # for stu in all_stu_data:
    #     stu.city = 'Indore'
    # student_data = Student.objects.bulk_update(all_stu_data, ['city'])

    #for bulk in
    # student_data = Student.objects.in_bulk([1, 3])
    # print(student_data[3].name)

    # student_data = Student.objects.get(pk=7).delete()
    # student_data = Student.objects.filter(marks=78).delete()
    print(Student.objects.all().count())
    return render(request, 'student/home.html', {'student': student_data})
