from django.conf.urls import url
from basic_app import views

#Template tagging
app_name = 'basic_app'

urlpatterns =[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]

# So basically what this is saying is OK if you're coming to your project page and you see something that
# when we run the application and we are at home page and if we  add /basic_app at the end of the url then
# like says home pay domainname.com/basic_app/ then you're going to come over here(basic_app/urls.py),
# domainname.com/basic_app/relative gives you the relative view
# domain_name.com/basic_app/other and gives you the other view
