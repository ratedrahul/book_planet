from django.urls import path,include
from . import views
# from .views import CustomLoginView,RegistrationView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.homepage,name = "homepage"),
    path('index/',views.index,name = "index"),
    path('blog/',views.blog,name = "blog_page"),
    # path('register/',views.register,name = "register"),
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('upload-to/', views.upload_to, name='upload_to'),
    path('coding-books/', views.coding_books, name='coding_books'),

    path('book_collection/<str:pdf_filename>/', views.view_pdf, name='view_pdf'),
    # path('register/', RegistrationView.as_view(), name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
