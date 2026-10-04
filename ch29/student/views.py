
from django.shortcuts import render, redirect
from student.forms import StudentForm
from django.contrib import messages
 

def demo(req):
    if req.method == 'POST':
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
            # messages.add_message(req, messages.SUCCESS, 'Form submitted successfully!')
            messages.success(req, "Form submitted successfully!")

            return redirect('demo')
    else:
        form = StudentForm()

    return render(req, 'student/demo.html',
                   {
                       'form': form,
                      
                    })