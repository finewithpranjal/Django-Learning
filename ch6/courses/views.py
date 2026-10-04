from django.shortcuts import render


def learn_django(request):
    # return render(request, template_name, context=dic_name, content_type=MIME_TYPE, status=None, using=None)
    return render(request, 'courses/django.html')


def learn_fastapi(request):
    return render(request, 'courses/fastapi.html')