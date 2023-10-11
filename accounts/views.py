from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
# from django.views import generic
# from django.urls import reverse_lazy

from .forms import EngineerSignUpForm, LabourSignUpForm, FilterForm, LoginForm, CheckboxesForm, UpdateProfileForm, UpdateUserForm,EngProfileform
from django.views.generic import TemplateView
from .models import Engineer, Labour, Hired, User
# Create your views here.


# Previous template saved on ->>> https://searchresults.htmlsave.net/
# admin ->> mobileno- 9209253983 password-123456
def home(request):
    # user_type = user = User.objects.get(pk=request.user.id)
    # user_eng = user_type.is_engineer
    # user_labour = user.is_labour
    # context = {'engineer':user_eng,'labour':user_labour}
    #'user_id':user_id
    return render(request, 'index2.html')


# def EditProfView(request):
#     check = Labour.objects.filter(user__id=request.user.id)
#     if len(check)>0:
#         data = Labour.objects.get(user__id=request.user.id)
#     if request.method=='POST':
#         form = UpdateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your profile has been updated!")
#             return redirect('home')

#     else:
#         form = UpdateProfileForm()
#     return render(request,'update_profile.html',{'data':data,'form':form})


def UpdateProfile_view(request):
    user = User.objects.get(pk=request.user.id)
    labr = Labour.objects.get(user=request.user.id)
    # engg = Engineer.objects.get(user=request.user)
    print("This is user id >>> ", user.id)
    print('-----------',labr,"------------")
    # form = UpdateProfileForm(instance=labr)
    labour_id = labr.id
    print("This is labour id :", labour_id)
    if labour_id and user.id:

        if request.method == 'POST':
            p_form = UpdateProfileForm(request.POST, instance=labr)
            u_form = UpdateUserForm(request.POST, instance=user)
            if p_form.is_valid() and u_form.is_valid():
                p_form.save()
                u_form.save()
                messages.success(request, "Your profile has been updated!")
                return redirect('home')
        else:
            p_form = UpdateProfileForm(instance=labr)
            u_form = UpdateUserForm(instance=user)
    context = {'u_form': u_form, 'p_form': p_form,'labr_id':labour_id,'labr_uid':user.id}
    return render(request, 'update_profile.html', context)


def UpdateProfileEngineer(request):
    user = User.objects.get(pk=request.user.id)
    engg = Engineer.objects.get(user = request.user.id)
    engg_id = engg.id
    print("Engineer  ID : {}".format(engg_id))
    print("Engineer user ID : {}".format(engg.id))
    if engg and engg_id:
        if request.method=='POST':
            e_form = EngProfileform(request.POST,instance=engg)
            ue_form = UpdateUserForm(request.POST,instance=user)
            if e_form.is_valid() and ue_form.is_valid():
                e_form.save()
                ue_form.save()
                messages.success(request, "Your profile has been updated! {}".format(request.user))
                return redirect('home')
        else:
            e_form = EngProfileform(instance=engg)
            ue_form = UpdateUserForm(instance=user)
    context = {'e_form':e_form,'ue_form':ue_form,'engg':engg,'engg_id':engg_id}
    return render(request, 'update_profile.html', context)

    # return HttpResponse('<h1>Engineer Edit Profile</h1>')


def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,"your password is changed succesfully!!")
            return redirect('home')
        else:
            return redirect('change_pswrd')
    else:
        form = PasswordChangeForm(user=user)
    context = {'form': form}
    return render(request, 'change_password.html', context)


# class EnggSignup(CreateView):
#     model =Engineer
#     form_class = EngineerSignUpForm
#     template_name='regg_engg.html'

#     def form_valid(self,form):
#         user = form.save()
#         login(self.request,user)
#         return redirect('home')

# class LabourSignup(CreateView):
#     model = Labour
#     lab_form_class = LabourSignUpForm
#     template_name='regg_engg.html'

#     def form_valid(self,form):
#         user = form.save()
#         login(self.request,user)
#         return redirect('home')


# class two_forms(TemplateView):
#     engg_form_class=EngineerSignUpForm
#     labr_form_class=LabourSignUpForm
#     template_name='reg_engg.html'

#     def post(self,request):
#         post_data=request.POST or None
#         engg_form =self.engg_form_class(post_data,prefix = 'eng_post')
#         labb_form = self.labr_form_class(post_data,prefix = 'lab_post')

#         context = self.get_context_data(engg_form=engg_form,labb_form=labb_form)

#         if engg_form.is_valid():
#             self.form_save(engg_form)
#         if labb_form.is_valid():
#             self.form_save(labb_form)

#         return render(None,'regg_engg.html',context)

#     def form_save(self,form):
#         obj = form.save()
#         # messages.success(self.request, "{} saved successfully".format(obj))
#         return obj
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)

# def two_forms(request):
#     if request.method == 'POST':
#         if 'engineer' in request.POST:
#             engg_form = EngineerSignUpForm(request.POST, prefix='engg')
#             if engg_form.is_valid():
#                 engg_form.save()
#             labb_form =LabourSignUpForm(prefix='labb')
#         elif request.method=="POST":
#             if 'labour' in request.POST:
#                 labb_form = LabourSignUpForm(request.POST, prefix='labb')
#                 if labb_form.is_valid():
#                     labb_form.save()
#                 labb_form =EngineerSignUpForm(prefix='engg')
#     else:
#         engg_form = EngineerSignUpForm(prefix='engg')
#         labb_form = LabourSignUpForm(prefix='labb')
#         return render(request,'regg_engg.html')


# ----------------------- ---------------------------
# def SignupEngg(request):
#     if request.method=="POST":
#         engg_form=EngineerSignUpForm(request.POST)
#         if engg_form.is_valid():
#             engg_form.save()
#             return redirect('')
#         else:
#             context={'engg_form':engg_form,'labr_form': LabourSignUpForm()}
#             return render(request, 'reg_engg.html',context)
#     else:
#         return render(request,'regg_engg.html')


# def SignupLabr(request):
#     if request.method=="POST":
#         labr_form=LabourSignUpForm(request.POST)
#         if labr_form.is_valid():
#             labr_form.save()
#             return redirect('')
#         else:
#             context={'labr_form':labr_form,'engg_form': EngineerSignUpForm()}
#             return render(request, 'reg_engg.html',context)
#     else:
#         return render(request,'regg_engg.html')


# ----------------------- ---------------------------


#---------------FINAL TRY-----------------------#
def two_view(request):
    if request.method == "POST":
        if 'location' in request.POST:
            print('Labour Form')
            labr_form = LabourSignUpForm(request.POST)
            if labr_form.is_valid():
                labr_form.save()
                messages.success(request,"Your details are successfully Submitted")
                return redirect('home')
            else:
                template = 'regg_engg.html'
                context = {'engg_form': EngineerSignUpForm(),
                           'labr_form': labr_form}
                return render(request, template, context)

        else:
            print('Engineer Form')
            engg_form = EngineerSignUpForm(request.POST)
            if engg_form.is_valid():
                engg_form.save()
                messages.success(request,"Your details are successfully Submitted")
                return redirect('home')
            else:
                template = 'regg_engg.html'
                context = {'engg_form': engg_form,
                           'labr_form': LabourSignUpForm()}
                return render(request, template, context)
    else:
        template = 'regg_engg.html'
        context = {'engg_form': EngineerSignUpForm(),
                   'labr_form': LabourSignUpForm}
        return render(request, template, context)


#---------------FINAL TRY-----------------------#

# def findlabour(request):
#     if request.method=="POST":
#         category=request.get.POST('category')
#         city=request.get.POST('city')
#         lab_obj =Labour.objects.filter(category=category,location=city)
#         lab_obj.save()
#     return render(request,'find_labour.html',{'labr':lab_obj})

# ------------- USING DJANGO FILTERS------------------
# def search_labour(request):
#     reslt=Labour.objects.all()
#     res_filter=SearchFilter(request.POST,queryset=reslt)
#     print(res_filter)
#     return render(request,'find_labour.html',{'filter':res_filter})


# ------------- USING DJANGO FILTERS------------------


# --------------APJ VIEWS----------------
# def my_view(request):
#     if request.method == 'POST':
#         form = FilterForm(request.POST)

#         if form.is_valid():
#             category = form.cleaned_data['Category']
#             city = form.cleaned_data['City']
#             labours = Labour.objects.filter(category=category, location__icontains=city)
#             return render(request, 'results2.html', {'data': labours})
#     else:
#         form = FilterForm()
#     return render(request, 'find_labour.html', {'form': form})

def search_labour_view(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['Category']
            city = form.cleaned_data['City']
            # labours = Labour.objects.filter(location = "Nagpur").values('id')[0]
            labours = Labour.objects.filter(
                category=category, location__icontains=city, is_hired=False)
            print("Labour's id :", labours.values('id'))
            engg = Engineer.objects.all()
            print("Engineer's id : ", engg.values('id'))
            # for v in labours:
            #     print(v.user.id)
            #     print(v.user.full_name)
            # lbr= Labour.objects.get('location')
            # print(lbr.id)
        # new_form = CheckboxesForm(category, city)
        # return render(request,'results2.html',{'form': new_form, 'category':category,'city':city,'data':labours})  #-- 'data':labours}
        return render(request, 'new_method.html', {'data': labours})
    else:
        form = FilterForm()
    return render(request, 'final_results.html', {'form': form})


def hire_view(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        eng = Engineer.objects.get(user=user)
        data = request.POST.getlist('labr')
        # form = CheckboxesForm(category,city, request.POST)
        # if form.is_valid():
        #     data = form.cleaned_data['checkboxes']
        #     print("Valid : ")
        for i in data:
            labr = Labour.objects.get(id=int(i))
            Hired.objects.create(labr_id=labr, eng_id=eng)
            print(i)
            print(eng)
            labr.is_hired = True
            labr.save()
        return redirect("home")
    return HttpResponse("<h1><Method not allowed</h1>")


# --------------APJ VIEWS----------------
# id --- 789456205 password  --- 123025
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mobile_no = form.cleaned_data['phone_no']
            password = form.cleaned_data['password']
            print(mobile_no)
            print(password)
            user = authenticate(phone_no=mobile_no, password=password)
            is_exists = User.objects.filter(phone_no=mobile_no).exists()
            pswrd_exist = User.objects.filter(password=password).exists()
            if user is not None:
                login(request, user)
                # ,extra_tags='home'
                messages.success(request,'You are successfully Logged in',extra_tags='login')
                return redirect('home')
            else:
                if is_exists == False:
                    print("phone number not exists")
                    messages.error(request, 'phone number not exists')
                    return redirect('login')
                if pswrd_exist == False:
                    print("Password is Not Valid")
                    # extra_tags='login'
                    messages.error(request, 'Password is not Valid')
                    return redirect('login')
                # if password != User.objects.get('password'):
                #     print("Password is not correct")
                #     messages.info(request,'Incorrect Password ')
                #     return redirect('login')
                if len(password) > 6:
                    print("Length of password must be more than SIX")
                    messages.info(
                        request, 'Length of password must be less than 6')
                    return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'Login.html', {'form': form})


def results(request):
    engg = Engineer.objects.all()
    labour_detail = Labour.objects.all()
    return render(request, 'results.html', {'labour_detail': labour_detail, 'engg': engg})


def logout_view(request):
    logout(request)
    messages.success(request,"You have successfully logged out")
    return redirect('home')

# def hiring_labour_view(request):
#     engineer = request.user
#     labour_id = Labour.user.id
#     hired = Hired.objects.create(eng_id=engineer,lab_id=labour_id)


# def get_form(request,formcls, prefix):
#     data = request.POST if prefix in request.POST else None
#     return formcls(data, prefix=prefix)


# class MyView(TemplateView):
#     template_name = 'reg_engg.html'

#     def get(self, request, *args, **kwargs):
#         return self.render_to_response(request,{'aform': EngineerSignUpForm(prefix='aform_pre'), 'bform': LabourSignUpForm(prefix='bform_pre')})

#     def post(self, request, *args, **kwargs):
#         aform = get_form(request, EngineerSignUpForm, 'aform_pre')
#         bform = get_form(request, LabourSignUpForm, 'bform_pre')
#         if aform.is_bound and aform.is_valid():
#             return self.render_to_response(request,{'aform': EngineerSignUpForm(prefix='aform_pre')})
#             # Process aform and render response
#         elif bform.is_bound and bform.is_valid():
#             return self.render_to_response(request,{'bform': LabourSignUpForm(prefix='bform_pre')})
#             # Process bform and render response
#         return self.render_to_response(request,{'aform': aform, 'bform': bform})
