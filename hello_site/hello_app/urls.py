from hello_app.views import HelloWorldView, HelloView
from django.urls import path

#from hello_site.hello_app.views import HelloView

urlpatterns = [
    path('', view = HelloWorldView.as_view()),
    path('<str:name>', view = HelloView.as_view())
]  
