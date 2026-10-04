from django.shortcuts import render
from datetime import datetime

# Example 1.1 - Varible

# def learn_django(req):
#     return render(req, 'course/dj.html', context={'name': 'Django'})


# Example 1.2 - Varible

# def learn_django(req):
#     name = 'Django'
#     duration = '5 months'
#     seats = 10
#     course_details = {
#                       'name':name,
#                       'duration': duration,
#                       'seats':seats
#                       }
    
#     return render(req, 'course/dj.html', course_details)

# Example 2 - Filter

# def learn_django(req):
#      return render(req, 'course/dj.html', context={'name': 'Django', 'desc': 'Django is awsome framework'})



# # Example 3 - Date & Time

# def learn_django(req):
#      d = datetime.now()
#      return render(req, 'course/dj.html', context={'dt': d})


# Example 4 - Float Format

# def learn_django(req):
    
#   return render(req, 'course/dj.html', context={'p1': 56.89567, 'p2': 57.000, 'p3': 58.37000} ) 


# Example 5 - If tag : Not filter

# def learn_django(req):
    
#   return render(req, 'course/dj.html', context={'nm':True} ) # If we wrote nm = '' (empty string) so it is concidered as false and if we write a string if would be concider as true by default

# Example 5.2 - If tag : Not filter

# def learn_django(req):
    
#   return render(req, 'course/dj.html', context={'nm':'Django', 'st' : 5} )


# Example 6 - For loop Tag

# def learn_django(req):
#   student = {'names': ['Chandu', 'Nivid', 'Yash', 'Jaya']}
#   return render(req, 'course/dj.html', context=student)


# Example 7

# def learn_django(req):
#   stu = {
#          'stu1': {'name': 'Rahul', 'roll' : 101},
#          'stu2': {'name': 'Ramesh', 'roll' : 102}, 
#          'stu3': {'name': 'Rohit', 'roll' : 103},
#          'stu4': {'name': 'Rakesh', 'roll' : 104},
#         }
  
#   students = {'student': stu}
#   return render(req, 'course/dj.html', context=students)


# Example 8

def learn_django(req):
 student = {'name': 'Rahul', 'roll' : 101}
 return render(req, 'course/dj.html', context={'student': student})

# Example 8

def learn_django(req):
   student = {
         'stu1': {'name': 'Rahul', 'roll' : 101},
         'stu2': {'name': 'Ramesh', 'roll' : 102}, 
         'stu3': {'name': 'Rohit', 'roll' : 103},
         'stu4': {'name': 'Rakesh', 'roll' : 104},
        }
   return render(req, 'course/dj.html', context={'student': student})



