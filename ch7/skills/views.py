from django.shortcuts import render

def showdj(request):
    seates = 10
    skilldetails = {
                 'sname' : 'Django',
                 'version':'6.1',
                 'st': seates 
                }

    return render(request, 'skills/heyFast.html',context=skilldetails)
    
    #  return render(request, 'skills/heyFast.html',dictname)
    #  return render(request, 'skills/heyFast.html',{'key': 'value'})
    
