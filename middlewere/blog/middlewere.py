from django.shortcuts import HttpResponse, render
def my_fun_middlewere(get_response):
    print("One time configuration")


    def my_func(req):
        print("Before view")
        responce = get_response(req)
        print("After view")
        return responce 
    return my_func


# def my_fun_middlewere(get_response):
#     print("One time configuration")


#     def my_func(request):
#         print("Before view")
#         # responce = HttpResponse("Responce from my_fun_middlewere")
#         responce = render(request, 'blog/uc.html')
#         print("After view")
#         return responce 
#     return my_func

class MyClMiddlewere:
    def __init__(self, get_response):
       self.get_response = get_response 
       print("One time configuration of class middlewere")

    def __call__(self, request):
        print("Before view")
        responce = self.get_response(request)
        print("After view")
        return responce

class MyClMiddlewere2:
    def __init__(self, get_response):
       self.get_response = get_response 
       print("One time configuration of class middlewere2")

    def __call__(self, request):
        print("Before view of class middlewere2")
        responce = self.get_response(request)
        print("After view of class middlewere2")
        return responce


class MyClMiddlewere3:
    def __init__(self, get_response):
       self.get_response = get_response 
       print("One time configuration of class middlewere3")

    def __call__(self, request):
        print("Before view of class middlewere3")
        responce = self.get_response(request)
        print("After view of class middlewere3")
        return responce
       

