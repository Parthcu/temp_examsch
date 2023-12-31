from django.urls import path, include
from rest_framework import routers
from exam_sch.views import user_table_create,subject_list,subject_detail,program_list,program_detail
from exam_sch.views import roles_create, create_gender,program_level_detail,program_level_list,roles_detail
from exam_sch.views import user_login,session_list,session_detail,user_table_detail,dept_detail,dept_list
from . import views
from exam_sch.views import semester_detail,semester_list,slot_list,slot_detail,program_search_api,subject_search_api
from rest_framework.decorators import api_view

router = routers.DefaultRouter()
router.register(r'roles', views.roles_create, basename='roles')
router.register(r'user_table', views.user_table_create, basename='user_table')
router.register(r'departments', views.dept_list, basename='department')
router.register(r'session', views.session_list, basename='session')
router.register(r'programe_level', views.program_level_list, basename='programe_level')
router.register(r'gender',views.create_gender,basename= 'gender')
router.register(r'Subject',views.subject_list, basename = 'Subject')
router.register(r'Program',views.program_list, basename = 'Program')
router.register(r'Semester',views.semester_list, basename = 'semester')
router.register(r'Slot',views.slot_list,basename= 'slot')
#urlpatterns = [
#    path('', include(router.urls)),
#    # Add other URL patterns if needed
#]


urlpatterns = [
    # Your existing URL patterns
    path('api/user_table/create', views.user_table_create, name='user_table'),
    path('api/user_table/<int:pk>/', user_table_detail, name='user_table-detail'),
    path('api/roles_create/',views.roles_create,name= 'roles'),
    path('api/roles/<int:pk>/', views.roles_detail, name='roles-detail'),
    path('api/login', views.user_login, name='user-login'),
    path('api/genders_create/', views.create_gender, name='gender-list'),
    path('api/genders/<int:pk>/', views.gender_detail, name='gender-detail'),
    path('api/program_level_list/', views.program_level_list, name='program_level-list'),
    path('api/program_level_detail/<int:pk>/', views.program_level_detail, name='program_level_detail'),
    path('api/program_list/', views.program_list, name='program-list'),
    path('api/program_detail/<int:pk>/', views.program_detail, name='program-detail'),
    path('api/depts_list/', views.dept_list, name='dept-list'),
    path('api/depts_detail/<int:pk>/', views.dept_detail, name='dept-detail'),
    path('api/sessions_list/', views.session_list, name='session-list'),
    path('api/sessions_detail/<int:pk>/', views.session_detail, name='session-detail'),
    path('api/subject_list/', views.session_list, name='subject-list'),
    path('api/subject_detail/<int:pk>/', views.session_detail, name='subject-detail'),
    path('api/semester_list/', views.semester_list, name='semester-list'),
    path('api/semester_detail/<int:semester_id>/', views.semester_detail, name='semester-detail'),
    path('api/slots_list/', views.slot_list, name='slot-list'),
    path('api/slots_detail/<int:slot_id>/', views.slot_detail, name='slot-detail'),
    path('api/program-search/', program_search_api, name='program-search-api'),
    path('api/subject-search/', subject_search_api, name='subject-search-api'),

]


 