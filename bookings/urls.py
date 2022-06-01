from . import views 
from django.urls import path


urlpatterns = [
    path('', views.Index, name='index'),
    path('inspiration/', views.Inspiration.as_view(), name='photos'),
    path('appointment_bookings/', views.NewBooking, name="appointment_bookings"),
    # Blank path indicates its the default (home page)

]