from django.urls import path

from . import views
from django.conf.urls.static import static
from testsite import settings
urlpatterns = [
	path("", views.index, name= 'index'),
	path('register/', views.register, name = "register"),
	path('profile/', views.profile, name = 'profile'),
	path('profile/edit/', views.edit, name = 'edit'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)