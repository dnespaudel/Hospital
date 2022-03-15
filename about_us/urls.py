from django.urls import path
from about_us.views import *

app_name = "about_us"

urlpatterns = [
    path('hospital-image', HospitalImageListCreateView.as_view()),
    path('hospital-image/all', HospitalImageListView.as_view()),
    path('hospital-image/<pk>', HospitalImageDetailView.as_view()),
    path('about-hospital', AboutHospitalListCreateView.as_view()),
    path('about-hospital/all', AboutHospitalListView.as_view()),
    path('about-hospital/<pk>', AboutHospitalDetailView.as_view()),
    path('record', RecordListCreateView.as_view()),
    path('record/all', RecordListView.as_view()),
    path('record/<pk>', RecordDetailView.as_view()),
    path('department-image', DepartmentImageListCreateView.as_view()),
    path('department-image/all', DepartmentImageListView.as_view()),
    path('department-image/<pk>', DepartmentImageDetailView.as_view()),
    path('department', DepartmentListCreateView.as_view()),
    path('department/all', DepartmentListView.as_view()),
    path('department/<pk>', DepartmentDetailView.as_view()),
    path('doctor-image', DoctorImageListCreateView.as_view()),
    path('doctor-image/all', DoctorImageListView.as_view()),
    path('doctor-image/<pk>', DoctorImageDetailView.as_view()),
    path('doctor', DoctorListCreateView.as_view()),
    path('doctor/all', DoctorListView.as_view()),
    path('doctor/<pk>', DoctorDetailView.as_view()),
    path('doctor-details', DoctorDetailsListCreateView.as_view()),
    path('doctor-details/all', DoctorDetailsListView.as_view()),
    path('doctor-details/<pk>', DoctorDetailsDetailView.as_view()),
    path('about-doctor', AboutDoctorListCreateView.as_view()),
    path('about-doctor/all', AboutDoctorListView.as_view()),
    path('about-doctor/<pk>', AboutDoctorDetailView.as_view()),
    path('doctor-listing', DoctorListingListCreateView.as_view()),
    path('doctor-listing/all', DoctorListingListView.as_view()),
    path('doctor-listing/<pk>', DoctorListingDetailView.as_view()),

]