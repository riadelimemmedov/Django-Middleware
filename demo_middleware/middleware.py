from django.db.models import F
from .models import *

#!What Django Middleware
# In Django, middleware is a lightweight plugin that processes during request and response execution. 
# Middleware is used to perform a function in the application.
# The functions can be a security, session, csrf protection, authentication etc


class DemoMiddleware(object):#*”object” is a kind of placeholder, letting Python know you don't want to inherit the properties of some other class.
    def __init__(self,get_response):#*This function is passed to our middleware by the Django framework, and its purpose is to pass the request object over to the next middleware, and the get the value of the response.
        print('Working __init__')
        self.get_response = get_response
        self.num_requests = 0
        self.num_exceptions = 0
        self.context_message = {
            "message":{
                "info":"Please request again this page"
            }
        }
        
        
    def listOperatingSystemData(self,os_info):
        if 'Windows' in os_info:
            print('noldu amk buna')
            NewStats.objects.all().update(win=F('win')+1)
        if 'Mac' in os_info:
            NewStats.objects.all().update(mac=F('mac')+1)
        if 'Iphone' in os_info:
            NewStats.objects.all().update(iph=F('iph')+1)
        if 'Android' in os_info:
            NewStats.objects.all().update(android=F('android')+1)
        else:
            #this block each request working and save to database keeped own data
            NewStats.objects.all().update(oth=F('oth')+1)

    def __call__(self,request):#*This is where we put our actual middleware logic. This method is called by the Django framework to invoke our middleware.__class__ is an attribute on the object that refers to the class from which the object was created.
        # Code that is executed in each request <before> the view is called,when we called view,first get_response(request) and request data send to view and then return response data line 17
        print('__call__ working')
        self.num_requests+=1
        response = self.get_response(request)
        
                
        a = NewStats.objects.all().values('win','mac','iph','android','oth')
        b = NewStats.objects.all().annotate().values('win','mac','iph','android','oth')
        
        if 'admin' not in request.path:
            #?call listOperatingSystemData function each request
            self.listOperatingSystemData(str(request.META['HTTP_USER_AGENT']))
        
        # print('Request path : ', request.path)
        # print('Request headers host : ', request.headers['HOST'])
        # print('Request headers accept-language : ', request.headers['Accept-Language'])
        # print('Request headers method : ', request.META['REQUEST_METHOD'])
        # print('Request domain adress ', request.META['REMOTE_ADDR'])REMOTE_ADDR refers to the IP address of the client.
        
        
        print('return response __call__ attribute')
        # Code that is executed in each request <after> the view is called
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        #This code is executed just before the view is called
        #This method is called each time Django receives a request and routes it to a view
        #Logic execute before a call to view
        #Gives access to the view itself & arguments
        #process_view allow to us connect to view before request,working before request to view
        print('Worked view_name ', view_func.__name__)
        print('View value name ', view_kwargs)
        print('Working process_view function')
        
        
    def process_exception(self,request,exception):
        # This code is executed if an exception is raised
        #This method is called whenever a view raises an exception that isn't caught within the view itself. 
        # Hence, process_exception is invoked after the request has reached and returned from the view.
        print('process_exception run...')
        self.num_exceptions+=1
        print('Summery of exception when running server django ', self.num_exceptions)
        
        
    def process_template_response(self,request,response):
        #This method is also invoked after the view has finished executing. 
        # It is only called if the resultant response contains a render() method, which indicates a template is being rendered. 
        # You can use this method to alter the content of the template, including its context data, if required.
        #This methods starting working,when view return to response client
        print('Working process_template_response view')
        print('response... ', response)
        print('response context_data... ', response.context_data) 
        response.context_data['new_message'] = self.context_message
        return response