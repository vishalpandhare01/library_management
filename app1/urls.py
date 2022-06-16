
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('remove_book/<int:book_id>',views.remove_book,name='remove_book'),
    path('Update/<int:id>',views.Update,name='Update'),
    path('Update/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),

    path('new_user/',views.new_user,name='new_user'),
    path('LogIn/',views.LogIn,name='LogIn'),
    path('LogOut/',views.LogOut,name='LogOut'),
]