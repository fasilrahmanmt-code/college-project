"""
URL configuration for smarteduconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('update_pass/', views.update_pass),
    path('logoutq/', views.logoutq),
    path('login_page/', views.login_page),
    path('admin_home/', views.admin_home),
    path('add_course/', views.add_course),
    path('add_article/', views.add_article),
    path('delete_article/<id>', views.delete_article),
    path('add_article_post/', views.add_article_post),
    path('add_department/', views.add_department),
    path('add_scholership/', views.add_scholership),
    path('course_request/', views.course_request),
    path('view_course_request/', views.view_course_request),
    path('accept_request/<id>/', views.accept_request),
    path('reject_request/<id>/', views.reject_request),
    path('manage_notification/', views.manage_notification),
    path('add_notification/', views.add_notification),
    path('add_notification_post/', views.add_notification_post),
    path('edit_notification/<id>/', views.edit_notification),
    path('edit_notification_post/', views.edit_notification_post),
    path('delete_notification/<id>/', views.delete_notification),
    path('edit_scholership/<id>', views.edit_scholership),
    path('edit_scholership_post/', views.edit_scholership_post),
    path('manage_article/', views.manage_article),
    path('manage_course/<id>/', views.manage_course),
    path('edit_course/<id>/', views.edit_course),
    path('manage_department/', views.manage_department),
    path('send_reply/<id>/', views.send_reply),
    path('verify_users/', views.verify_users),
    path('verify_college/', views.verify_college),
    path('accept_college/<id>/', views.accept_college),
    path('reject_college/<id>/', views.reject_college),
    path('view_complaint/', views.view_complaint),
    path('send_reply_post/', views.send_reply_post),
    path('view_scholership/', views.view_scholership),
    path('add_scholershippost/', views.add_scholershippost),
    path('delete_scholership/<id>', views.delete_scholership),
    path('manage_job/', views.manage_job),
    path('add_job/', views.add_job),
    path('jobpost/', views.jobpost),
    path('deletejob/<id>/', views.deletejob),
    path('edit_job/<id>/', views.edit_job),
    path('edit_jobpost/', views.edit_jobpost),

    path('college_home/', views.college_home),
    path('admission/', views.admission),
    path('college_view_profile/', views.college_view_profile),
    path('college_edit_profile/', views.college_edit_profile),
    path('college_edit_profile_post/', views.college_edit_profile_post),
    path('college_register/', views.college_register),
    path('college_reg_post/', views.college_reg_post),
    path('data_set_form/', views.data_set_form),
    path('add_dataset_post/', views.add_dataset_post),
    path('manage_data_set/<id>', views.manage_data_set),
    path('delete_dataset/<id>', views.delete_dataset),
    path('manage_result/', views.manage_result),
    path('mark/', views.mark),
    path('edit_marks/<id>/', views.edit_marks),
    path('edit_mark_post/', views.edit_mark_post),
    path('add_mark_post/', views.add_mark_post),
    path('request_for_course/', views.request_for_course),
    path('request_course/<id>/', views.request_course),
    path('score_result/', views.score_result),
    path('View_course/', views.view_course),
    path('view_notification/', views.view_notification),
    path('view_request/', views.view_request),
    path('view_users/', views.view_users),

    path('login_post/', views.login_post),
    path('DepartmentPost/', views.DepartmentPost),
    path('DeleteDepartment/<id>/', views.DeleteDepartment),
    path('course_POST/', views.course_POST),
    path('editCoursePost/', views.editCoursePost),
    path('DeleteCourse/<id>/', views.DeleteCourse),



    path('user_login/', views.user_login),
    path('user_reg/', views.user_reg),
    path('send_complaint/', views.send_complaint),
    path('user_view_complaint/', views.user_view_complaint),
    path('user_changepassword/', views.user_changepassword),
    path('user_update_profile/', views.user_update_profile),
    path('user_view_profile/', views.user_view_profile),
    path('stud_view_scholership/', views.stud_view_scholership),




    path('admson_view_course/', views.admson_view_course),
    path('admission_prediction/', views.admission_prediction),
    path('chatbot_response/', views.chatbot_response),
    path('stud_view_colleges/', views.stud_view_colleges),
    path('stud_view_courses/', views.stud_view_courses),
    path('stud_view_jobinfo/', views.stud_view_jobinfo),





]
