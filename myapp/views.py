import os
from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.db.models import Q

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


from myapp.models import *

def login_page(request):
    return render(request,"login.html")

def update_pass(request):
    ob=User.objects.get(id=7)
    ob.password=make_password("user")
    ob.save()
    return HttpResponse("ok")

def login_post(request):
    print(request.POST)
    uname=request.POST['username']
    pwrd=request.POST['password']
    user=authenticate(request,username=uname,password=pwrd)
    if user is not None:
        if user.groups.filter(name="admin").exists():
            login(request,user)
            return redirect('/myapp/admin_home/')
        elif user.groups.filter(name="college").exists():
            col=college_table.objects.get(LOGIN=user.id)
            if col.status == "College":
                login(request,user)
                return redirect('/myapp/college_home/')
            else:
                return redirect('/myapp/login_page/')
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('/myapp/login_page/')
    return redirect('/myapp/login_page/')

def logoutq(request):
    logout(request)
    return redirect('/myapp/login_page/')

#===================================ADMIN================================================

@login_required(login_url='/myapp/login_page')
def admin_home(request):
    return render(request, "admin/admin_index.html")

@login_required(login_url='/myapp/login_page')
def manage_department(request):
    ob=department_table.objects.all()
    return render(request, "admin/manage department.html",{'data':ob})

@login_required(login_url='/myapp/login_page')
def add_department(request):
    return render(request, "admin/add department.html")

@login_required(login_url='/myapp/login_page')
def DepartmentPost(request):
    department=request.POST['department']
    details=request.POST['details']
    ob=department_table()
    ob.department=department
    ob.details=details
    ob.save()
    return redirect('/myapp/manage_department/#main')

@login_required(login_url='/myapp/login_page')
def DeleteDepartment(request,id):
    ob=department_table.objects.get(id=id)
    ob.delete()
    return redirect('/myapp/manage_department/#main')

@login_required(login_url='/myapp/login_page')
def manage_course(request,id):
    request.session['eid']=id
    ob=course_table.objects.filter(department_id=id)
    return render(request, "admin/manage course.html",{'data':ob})

@login_required(login_url='/myapp/login_page')
def add_course(request):
    return render(request, "admin/add course.html")

@login_required(login_url='/myapp/login_page')
def course_POST(request):
    course=request.POST['course']
    details=request.POST['details']
    fees=request.POST['fees']
    ob=course_table()
    ob.course=course
    ob.details=details
    ob.fee=fees
    ob.department_id_id=request.session['eid']
    ob.save()
    k=request.session['eid']
    return redirect(f'/myapp/manage_course/{k}#main')

@login_required(login_url='/myapp/login_page')
def edit_course(request,id):
    request.session['cid']=id
    ob=course_table.objects.get(id=id)
    return render(request, "admin/edit course.html",{'data':ob})

@login_required(login_url='/myapp/login_page')
def editCoursePost(request):
    course = request.POST['course']
    details = request.POST['details']
    fees = request.POST['fees']
    ob = course_table.objects.get(id=request.session['cid'])
    ob.course = course
    ob.details = details
    ob.fee = fees
    ob.department_id_id = request.session['eid']
    ob.save()
    k=request.session['eid']
    return redirect(f'/myapp/manage_course/{k}#main')

@login_required(login_url='/myapp/login_page')
def DeleteCourse(request,id):
    ob=course_table.objects.get(id=id)
    ob.delete()
    k = request.session['eid']
    return redirect(f'/myapp/manage_course/{k}#main')

@login_required(login_url='/myapp/login_page')
def manage_article(request):
    ob=article_table.objects.all()
    return render(request, "admin/manage article.html",{"data":ob})

@login_required(login_url='/myapp/login_page')
def add_article(request):
    return render(request, "admin/add article.html")

@login_required(login_url='/myapp/login_page')
def add_article_post(request):
    Article_title=request.POST['article_title']
    Article_subject=request.POST['article_subject']
    ob=article_table()
    ob.article_title =Article_title
    ob.article_subject= Article_subject
    ob.Date =datetime.today()
    ob.save()
    return redirect("/myapp/manage_article/#main")

@login_required(login_url='/myapp/login_page')
def delete_article(request,id):
    ob=article_table.objects.get(id=id)
    ob.delete()
    return redirect('/myapp/manage_article/#main')

@login_required(login_url='/myapp/login_page')
def view_scholership(request):
    ob=scholership_table_new.objects.all()
    return render(request, "admin/view scholership.html",{'data':ob})

@login_required(login_url='/myapp/login_page')
def add_scholership(request):
    return render(request, "admin/add scholership.html")

@login_required(login_url='/myapp/login_page')
def add_scholershippost(request):
    name=request.POST['name']
    details=request.POST['details']
    file=request.FILES['file']
    fs=FileSystemStorage()
    img=fs.save(file.name,file)

    ob=scholership_table_new()
    ob.Name=name
    ob.Details=details
    ob.Documents=img
    ob.Date=datetime.today()
    ob.save()
    return redirect("/myapp/view_scholership/#main")

@login_required(login_url='/myapp/login_page')
def delete_scholership(request,id):
    ob=scholership_table_new.objects.get(id=id)
    ob.delete()
    return redirect("/myapp/view_scholership/#main")

@login_required(login_url='/myapp/login_page')
def edit_scholership(request,id):
    request.session['sid']=id
    ob=scholership_table_new.objects.get(id=id)
    return render(request, "admin/edit scholership.html",{"data":ob})

@login_required(login_url='/myapp/login_page')
def edit_scholership_post(request):
    name=request.POST['name']
    details=request.POST['details']

    ob=scholership_table_new.objects.get(id=request.session['sid'])
    ob.Name=name
    ob.Details=details
    if 'file' in request.FILES:
        file = request.FILES['file']
        ob.Documents=file
    ob.Date=datetime.today()
    ob.save()
    return redirect("/myapp/view_scholership/#main")

@login_required(login_url='/myapp/login_page')
def manage_notification(request):
    ob=notification_table.objects.all()
    return render(request,'admin/sent notification.html',{"notifications":ob})

@login_required(login_url='/myapp/login_page')
def add_notification(request):
    return render(request,'admin/add notification.html')

@login_required(login_url='/myapp/login_page')
def add_notification_post(request):
    noti=request.POST['notification']
    details=request.POST['details']
    ob=notification_table()
    ob.Notification=noti
    ob.details=details
    ob.Date=datetime.now().date()
    ob.save()
    return redirect("/myapp/manage_notification/#main")

@login_required(login_url='/myapp/login_page')
def edit_notification(request,id):
    request.session['nid']=id
    ob=notification_table.objects.get(id=id)
    return render(request,'admin/edit_notification.html',{"data":ob})

@login_required(login_url='/myapp/login_page')
def edit_notification_post(request):
    noti=request.POST['notification']
    details=request.POST['details']
    ob=notification_table.objects.get(id=request.session['nid'])
    ob.Notification=noti
    ob.details=details
    ob.save()
    return redirect("/myapp/manage_notification/#main")

@login_required(login_url='/myapp/login_page')
def delete_notification(request,id):
    ob=notification_table.objects.get(id=id)
    ob.delete()
    return redirect("/myapp/manage_notification/#main")

@login_required(login_url='/myapp/login_page')
def verify_users(request):
    ob=user_table.objects.all()
    return render(request, "admin/verify users.html",{"val":ob})

@login_required(login_url='/myapp/login_page')
def verify_college(request):
    ob=college_table.objects.all()
    return render(request,'admin/verify_college.html',{"val":ob})

@login_required(login_url='/myapp/login_page')
def accept_college(request,id):
    ob=college_table.objects.get(id=id)
    ob.status="College"
    ob.save()
    return redirect("/myapp/verify_college/#main")

@login_required(login_url='/myapp/login_page')
def reject_college(request,id):
    ob=college_table.objects.get(id=id)
    ob.status="Rejected"
    ob.save()
    return redirect("/myapp/verify_college/#main")

@login_required(login_url='/myapp/login_page')
def view_complaint(request):
    ob=complaint_table.objects.all()
    return render(request, "admin/view complaint.html",{"data":ob})

@login_required(login_url='/myapp/login_page')
def send_reply(request,id):
    request.session['cid']=id
    return render(request, "admin/reply.html")

@login_required(login_url='/myapp/login_page')
def send_reply_post(request):
    reply=request.POST['reply']
    ob=complaint_table.objects.get(id=request.session['cid'])
    ob.reply=reply
    ob.save()
    return redirect("/myapp/view_complaint/#main")

@login_required(login_url='/myapp/login_page')
def manage_job(request):
    ob=job.objects.all()
    return render(request, "admin/manage_job.html",{'data':ob})

@login_required(login_url='/myapp/login_page')
def add_job(request):
    return render(request, "admin/add_job.html")

@login_required(login_url='/myapp/login_page')
def jobpost(request):
    job_title=request.POST['job_title']
    company=request.POST['company']
    qualification=request.POST['qualification']
    start_date=request.POST['start_date']
    end_date=request.POST['end_date']
    position=request.POST['position']
    no_vacancy=request.POST['no_vacancy']
    link=request.POST['link']
    ob=job()
    ob.job_title=job_title
    ob.company=company
    ob.qualification=qualification
    ob.start_date=start_date
    ob.last_date=end_date
    ob.position=position
    ob.no_vacancy=no_vacancy
    ob.link=link
    ob.save()
    return redirect('/myapp/manage_job/#main')

@login_required(login_url='/myapp/login_page')
def edit_job(request,id):
    request.session['jid']=id
    ob=job.objects.get(id=id)
    return render(request, "admin/edit_job.html",{"i":ob})

@login_required(login_url='/myapp/login_page')
def edit_jobpost(request):
    job_title=request.POST['job_title']
    company=request.POST['company']
    qualification=request.POST['qualification']
    start_date=request.POST['start_date']
    end_date=request.POST['end_date']
    position=request.POST['position']
    no_vacancy=request.POST['no_vacancy']
    link=request.POST['link']
    ob=job.objects.get(id=request.session['jid'])
    ob.job_title=job_title
    ob.company=company
    ob.qualification=qualification
    ob.start_date=start_date
    ob.last_date=end_date
    ob.position=position
    ob.no_vacancy=no_vacancy
    ob.link=link
    ob.save()
    return redirect('/myapp/manage_job/#main')

@login_required(login_url='/myapp/login_page')
def deletejob(request,id):
    ob=job.objects.get(id=id)
    ob.delete()
    return redirect('/myapp/manage_job/#main')

def course_request(request):
    a=course_request_table.objects.all()
    return render(request, "admin/course request.html",{'data':a})

@login_required(login_url='/myapp/login_page')
def view_course_request(request):
    ob=course_request_table.objects.all()
    return render(request,'admin/view_course_request.html',{"data":ob})

@login_required(login_url='/myapp/login_page')
def accept_request(request,id):
    ob=course_request_table.objects.get(id=id)
    ob.status="accepted"
    ob.save()
    return redirect("/myapp/view_course_request/#main")

@login_required(login_url='/myapp/login_page')
def reject_request(request,id):
    ob=course_request_table.objects.get(id=id)
    ob.status="Rejected"
    ob.save()
    return redirect("/myapp/view_course_request/#main")


############################college##############################

def college_register(request):
    return render(request, "college/college register.html")

def college_reg_post(request):
    name = request.POST['name']
    place = request.POST['place']
    email = request.POST['email']
    phone = request.POST['phone']
    proof = request.FILES['proof']
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.create(username=username, password=make_password(password), email=email, first_name=name)
    user.save()
    user.groups.add(Group.objects.get(name="college"))

    ob = college_table()
    ob.LOGIN = user
    ob.name = name
    ob.email = email
    ob.place = place
    ob.phone = phone
    ob.status = 'pending'
    ob.proof = proof
    ob.save()
    return redirect('/myapp/login_page/')

@login_required(login_url='/myapp/login_page')
def college_home(request):
    return render(request, "college/college_index.html")

@login_required(login_url='/myapp/login_page')
def request_for_course(request):
    ob=course_table.objects.all()
    return render(request, "college/request for course.html",{"data":ob})

@login_required(login_url='/myapp/login_page')
def request_course(request, id):
    college_login_id = request.user.id
    college_obj = college_table.objects.get(LOGIN=college_login_id)

    exists = course_request_table.objects.filter(COLLEGE=college_obj,COURSE__id=id).exists()
    if exists:
        messages.warning(request, "You have already requested this course.")
    else:
        ob = course_request_table()
        ob.COLLEGE = college_obj
        ob.COURSE = course_table.objects.get(id=id)
        ob.status = 'pending'
        ob.Date = datetime.today().date()
        ob.save()
        messages.success(request, "Course request submitted successfully!")
    return redirect('/myapp/request_for_course/#main')


@login_required(login_url='/myapp/login_page')
def view_request(request):
    ob=course_request_table.objects.filter(COLLEGE__LOGIN_id=request.user.id)
    return render(request, "college/view request.html",{"data":ob})

@login_required(login_url='/myapp/login_page')
def view_notification(request):
    ob=notification_table.objects.all()
    return render(request, "college/view notification.html",{"data":ob})

@login_required(login_url='/myapp/login_page')
def college_view_profile(request):
    ob=college_table.objects.get(LOGIN=request.user.id)
    return render(request, 'college/college_view_profile.html',{"data":ob})

@login_required(login_url='/myapp/login_page')
def college_edit_profile(request):
    ob = college_table.objects.get(LOGIN=request.user.id)
    return render(request, 'college/college_update_profile.html',{"data":ob})

@login_required(login_url='/myapp/login_page')
def college_edit_profile_post(request):
    name = request.POST['name']
    place = request.POST['place']
    email = request.POST['email']
    phone = request.POST['phone']
    ob = college_table.objects.get(LOGIN=request.user.id)
    if 'proof' in request.FILES:
        proof = request.FILES['proof']
        ob.proof = proof
    ob.name = name
    ob.email = email
    ob.place = place
    ob.phone = phone
    ob.save()
    return redirect('/myapp/college_view_profile/#main')

@login_required(login_url='/myapp/login_page')
def admission(request):
    ob=last_admission_table.objects.filter(COLLEGE__LOGIN=request.user.id)
    return render(request, "college/admission.html",{"data":ob})

@login_required(login_url='/myapp/login_page')
def mark(request):
    ob=course_request_table.objects.filter(COLLEGE__LOGIN=request.user.id,status="accepted")
    return render(request, "college/mark.html",{"data":ob})

@login_required(login_url='/myapp/login_page')
def add_mark_post(request):
    print(request.POST,"****************")
    course=request.POST['course']
    min_mrk=request.POST['strt_mrk']
    max_mrk=request.POST['endmrk']
    year=request.POST['year']
    ob=last_admission_table()
    ob.COLLEGE=college_table.objects.get(LOGIN=request.user.id)
    ob.COURSE_REQUEST=course_request_table.objects.get(id=course)
    ob.year=year
    ob.mark_starting=min_mrk
    ob.mark_ending=max_mrk
    ob.Date=datetime.now().today()
    ob.save()
    return redirect('/myapp/admission/#main')

@login_required(login_url='/myapp/login_page')
def edit_marks(request,id):
    request.session['mid']=id
    ob=course_request_table.objects.filter(COLLEGE__LOGIN=request.user.id,status="Approved")
    obj=last_admission_table.objects.get(id=id)
    return render(request, "college/edit_mark.html",{"data":ob,"val":obj})

@login_required(login_url='/myapp/login_page')
def edit_mark_post(request):
    course=request.POST['course']
    min_mrk=request.POST['strt_mrk']
    max_mrk=request.POST['endmrk']
    year=request.POST['year']
    ob=last_admission_table.objects.get(id=request.session['mid'])
    ob.COLLEGE=college_table.objects.get(LOGIN=request.user.id)
    ob.COURSE_REQUEST=course_request_table.objects.get(id=course)
    ob.year=year
    ob.mark_starting=min_mrk
    ob.mark_ending=max_mrk
    ob.Date=datetime.now().today()
    ob.save()
    return redirect('/myapp/admission/#main')


@login_required(login_url='/myapp/login_page')
def view_users(request):
    ob=user_table.objects.all()
    return render(request,'college/view_users.html',{"data":ob})

@login_required(login_url='/myapp/login_page')
def manage_data_set(request,id):
    request.session['reqid']=id
    print(id)
    ob=data_set_table.objects.filter(COURSE_REQ=id)
    return render(request, "college/manage data set.html",{"data":ob})

@login_required(login_url='/myapp/login_page')
def data_set_form(request):
    return render(request, "college/data set form.html")

@login_required(login_url='/myapp/login_page')
def add_dataset_post(request):
    question=request.POST['question']
    answer=request.POST['answer']
    k=request.session['reqid']
    ob=data_set_table()
    ob.COURSE_REQ=course_request_table.objects.get(id=k)
    ob.question=question
    ob.answer=answer
    ob.save()
    return redirect(f'/myapp/manage_data_set/{k}#main')

@login_required(login_url='/myapp/login_page')
def delete_dataset(request,id):
    ob=data_set_table.objects.get(id=id)
    ob.delete()
    k = request.session['reqid']
    return redirect(f'/myapp/manage_data_set/{k}#main')






def manage_result(request):
    return render(request, "college/manage result.html")

def score_result(request):
    return render(request, "college/score result.html")

def view_course(request):
    return render(request, "college/view course.html")




#===============================================================================================================================
#=====================================================USER======================================================================
#===============================================================================================================================
#===============================================================================================================================
#===============================================================================================================================
@csrf_exempt
def user_reg(request):
    name = request.POST['name']
    gender=request.POST['gender']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    email=request.POST['email']
    phone=request.POST['phone']
    photo = request.FILES["photo"]
    fs = FileSystemStorage()
    path=fs.save(photo.name, photo)

    proof = request.FILES["proof"]
    fs = FileSystemStorage()
    proof_path = fs.save(proof.name, proof)

    username = request.POST['username']
    pswd = request.POST['password']
    ab=User.objects.create(username=username,password=make_password(pswd),email=email,first_name=name,last_name=" ")
    ab.save()
    ab.groups.add(Group.objects.get(name='User'))

    ob=user_table()
    ob.LOGIN=ab
    ob.name=name
    ob.gender=gender
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.phone=phone
    ob.email=email
    ob.image=path
    ob.proof=proof_path
    ob.save()
    return JsonResponse({"status": "ok"})

@csrf_exempt
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    ob = authenticate(username=username, password=password)
    if ob is not None:
        if ob.groups.filter(name='user').exists():
            login(request, ob)
            lid = str(ob.id)
            return JsonResponse({'type':'user','lid': lid,'status':'ok'})
        else:
            return JsonResponse({'status': 'fail'})
    else:
        return JsonResponse({'status': 'fail'})

@csrf_exempt
def send_complaint(request):
    lid=request.POST['lid']
    complaint=request.POST['complaint']
    var = complaint_table()
    var.USERID = user_table.objects.get(LOGIN_id=lid)
    var.complaint = complaint
    var.Date = datetime.now().date()
    var.reply = "pending"
    var.save()
    return JsonResponse({'status':'ok'})

@csrf_exempt
def user_view_complaint(request):
    lid=request.POST['lid']
    l=[]
    var=complaint_table.objects.filter(USERID__LOGIN_id=lid)
    for i in var:
        l.append({
            'id': str(i.id),
            'complaint':str(i.complaint),
            'date':str(i.Date),
            'reply':str(i.reply),
        })
    return JsonResponse({'status':'ok','data':l})

@csrf_exempt
def user_changepassword(request):
    lid=request.POST['lid']
    current_password = request.POST['current_password']
    new_password = request.POST['new_password']

    user = User.objects.get(id=lid)
    if not user.check_password(current_password):
        return JsonResponse({
            "status": "error",
            "message": "Current password is incorrect."
        }, status=401) # Unauthorized

    user.set_password(new_password)
    user.save()

    return JsonResponse({
        "status": "ok",
        "message": "Password updated successfully. Please log in with your new password."
    })


@csrf_exempt
def user_update_profile(request):
    print(request.POST,"**************************")
    lid = request.POST['lid']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    gender = request.POST['gender']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    try:
        user = user_table.objects.get(LOGIN_id=lid)
    except user_table.DoesNotExist:
        return JsonResponse({"status": "error", "error": "User not found"}, status=404)
    user.name=name
    user.email=email
    user.phone=phone
    user.gender=gender
    user.place=place
    user.post=post
    user.pin=pin
    user.save()
    if 'photo' in request.FILES:
        try:
            if user.photo:
                old_path = user.photo.path
                if os.path.exists(old_path):
                    os.remove(old_path)
        except Exception:
            pass
        user.photo = request.FILES['photo']

    if 'proof' in request.FILES:
        try:
            if user.proof:
                old_path = user.proof.path
                if os.path.exists(old_path):
                    os.remove(old_path)
        except Exception:
            pass
        user.proof = request.FILES['proof']

    user.save()
    photo_url = user.photo.url if getattr(user, 'photo', None) else ""
    proof_url = user.proof.url if getattr(user, 'proof', None) else ""

    return JsonResponse({
        "status": "ok",
        "name": str(user.name),
        "email": str(user.email),
        "phone": str(user.phone),
        "gender": str(user.gender),
        "place": str(user.place),
        "post": str(user.post),
        "pin": str(user.pin),
        "photo": photo_url,
        "proof": proof_url,
    })

@csrf_exempt
def user_view_profile(request):
    lid=request.POST['lid']
    obj=user_table.objects.get(LOGIN=lid)
    print(obj)
    return JsonResponse({"status":"ok",
                         'name':str(obj.name),
                         'phone':str(obj.phone),
                         'image':str(obj.image.url),
                         'proof':str(obj.proof.url),
                         'gender':str(obj.gender),
                         'place': str(obj.place),
                         'post': str(obj.post),
                         'pin': str(obj.pin),
                         'email': str(obj.email),
                         })

@csrf_exempt
def stud_view_scholership(request):
    l=[]
    ob=scholership_table_new.objects.all()
    for i in ob:
        l.append({
            'id': str(i.id),
            'Name': str(i.Name),
            'Details': str(i.Details),
            'Date': str(i.Date),
            'Documents': str(i.Documents.url),
        })
    return JsonResponse({"status":"ok","data":l})


@csrf_exempt
def stud_view_jobs(request):
    l=[]
    ob=job.objects.all()
    for i in ob:
        l.append({
            'id': str(i.id),
            'job_title': str(i.job_title),
            'company': str(i.company),
            'qualification': str(i.qualification),
            'start_date': str(i.start_date),
            'last_date': str(i.last_date),
            'position': str(i.position),
            'no_vacancy': str(i.no_vacancy),
            'link': str(i.link),
        })
    return JsonResponse({"status":"ok","data":l})


@csrf_exempt
def stud_view_colleges(request):
    l=[]
    ob=college_table.objects.all()
    for i in ob:
        l.append({
            'id': str(i.id),
            'name': str(i.name),
            'place': str(i.place),
            'email': str(i.email),
            'phone': str(i.phone),
            'status': str(i.status)
        })
    return JsonResponse({"status":"ok","data":l})

@csrf_exempt
def stud_view_colleges(request):
    l=[]
    ob=college_table.objects.all()
    for i in ob:
        l.append({
            'id': str(i.id),
            'name': str(i.name),
            'place': str(i.place),
            'email': str(i.email),
            'phone': str(i.phone),
            'status': str(i.status)
        })
    return JsonResponse({"status":"ok","data":l})

@csrf_exempt
def stud_view_courses(request):
    cid=request.POST['cid']
    l=[]
    ob=course_request_table.objects.filter(COLLEGE__LOGIN_id=cid)
    for i in ob:
        l.append({
            'id': str(i.id),
            'department': str(i.COURSE.department_id.department),
            'course': str(i.COURSE.course),
            'details': str(i.COURSE.details),
            'fee': str(i.COURSE.fee)
        })
    return JsonResponse({"status":"ok","data":l})

@csrf_exempt
def stud_view_jobinfo(request):
    l=[]
    ob=job.objects.all()
    for i in ob:
        l.append({
            'id': str(i.id),
            'job_title': str(i.job_title),
            'qualification': str(i.qualification),
            'company': str(i.company),
            'start_date': str(i.start_date),
            'last_date': str(i.last_date),
            'position': str(i.position),
            'no_vacancy': str(i.no_vacancy),
            'link': str(i.link)
        })
    return JsonResponse({"status":"ok","data":l})

#===========================================================================
#===========================================================================
#======================================ADMISSION PREDICTION================================
#===========================================================================


@csrf_exempt
def admson_view_course(request):
    l=[]
    ob=course_table.objects.all()
    for i in ob:
        l.append({
            'id': str(i.id),
            'course': str(i.course)
        })
    return JsonResponse({"status":"ok","data":l})

@csrf_exempt
def admission_prediction(request):
    cid=request.POST['course_id']
    marks=request.POST['marks']
    lid=request.POST['lid']
    course_obj=course_request_table.objects.filter(COURSE=cid,status='accepted')
    college=[]
    for i in course_obj:
        #
        admison_details=last_admission_table.objects.filter(COLLEGE=i.COLLEGE.id).order_by("year")
        x=[]
        y=[]
        for j in range(0,len(admison_details)):
            x.append(j+1)
            y.append(admison_details[j].mark_ending)

        print(admison_details,"***********************************")
        res=forecast_fn(x,y)
        print(res,"**************")
        if float(res)<float(marks):
            college.append({"college_id": i.COLLEGE.id,
                            "college":i.COLLEGE.name,
                            "place":i.COLLEGE.place,
                            "email":i.COLLEGE.email,
                            "phone":i.COLLEGE.phone},)
    print(college)
    return JsonResponse({"status":"ok","predictions":college})


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def forecast_fn(x, y, degree=1, n_future=1):
    df = pd.DataFrame({'Time': x, 'Value': y})
    X = df[['Time']].values.reshape(-1, 1)
    Y = df['Value'].values

    # Transform features+

    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, Y)

    resultlist = []
    for ii in range(1, n_future + 1):
        future_time = X[-1, 0] + ii
        print(future_time,"future_time")
        ft_poly = poly.transform(np.array([[future_time]]))
        pred = model.predict(ft_poly)
        resultlist.append(pred[0])
    return resultlist[0]


#=======================================================++++++++++++++++++++++++
#============================================CHATBOT====++++++++++++++++++++++++
#=======================================================++++++++++++++++++++++++
#=======================================================++++++++++++++++++++++++


import json
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
GOOGLE_API_KEY = 'AIzaSyCkddab6h9NifGh_S0nAV7BZShnxGXg7uE'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            user_message = body.get('message', '').strip()
            INITIAL_QUESTION =  body.get('qus', '').strip()
            lid =  body.get('lid', '')

            if not user_message or user_message.upper() == "START_CHAT":
                return JsonResponse({
                    'status': 'ok',
                    'reply': INITIAL_QUESTION
                })
            print(user_message)
            obj = chatbot_table.objects.filter(USER__LOGIN=lid, Date=datetime.now().date())
            if len(obj)>3:
                for i in obj:
                    i.delete()
                response = model.generate_content( INITIAL_QUESTION+" is the question and reply is "+ user_message+" i need to   recommend course and career jobs for the user.")

            else:
                response = model.generate_content(
                    INITIAL_QUESTION + " is the question and reply is " + user_message + " i need to generate next question for generate for recommend course and career for the user as a short question with in one para")

            ob = chatbot_table()
            ob.USER = user_table.objects.get(LOGIN=lid)
            ob.question = INITIAL_QUESTION
            ob.answer = response.text
            ob.Date = datetime.now().date()
            ob.save()



            return JsonResponse({
                'status': 'ok',
                'reply': response.text
            })

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)