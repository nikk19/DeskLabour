# from django.contrib import admin
from django.urls import path
# from .views import EnggSignup,home,LabourSignup
# from .views import home,results,SignupLabr,SignupEngg,MyView
from .views import UpdateProfile_view, home,results,two_view,login_view,search_labour_view,hire_view,logout_view,change_password,UpdateProfileEngineer


urlpatterns = [
    path('',home,name="home"),
    # path('labeng',MyView.as_view(),name='labeng'),
    # path('eng_reg',EnggSignup.as_view(),name="eng_reg"),
    # path('labour',SignupLabr,name='labour'),
    # path('engineer',SignupEngg,name='engineer'),
    path('eng_lab',two_view,name='eng_lab'),
    path('results',results,name='results'),
    # path('findlab',findlabour,name='findlabr'),
    path('findlabr',search_labour_view,name='findlabr'),
    path('login/',login_view,name='login'),
    path('logout',logout_view,name='logout'),
    path('hire',hire_view,name= 'hire'),
    path('edit_prof',UpdateProfile_view,name='edit_prof'),
    path('change_pswrd',change_password,name='change_pswrd'),
    path('edit_prof_eng',UpdateProfileEngineer,name='edit_prof__eng'),



    # path('regengg',EnggSignup.as_view(),name="regengg"),
    # path('regengg2',LabourSignup.as_view(),name="regengg2"),
   

    
    
]

