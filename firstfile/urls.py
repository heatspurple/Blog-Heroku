from django.contrib import admin
from django.urls import path, include
import secondfile.views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', secondfile.views.home, name="home"),
    path('create/', secondfile.views.create, name="create"),
    path('detail/<int:post_id>', secondfile.views.detail, name="detail"),
    path('read/', secondfile.views.read, name="read"),
    path('update/<int:post_id>', secondfile.views.update, name="update"),
    path('renew/<int:post_id>', secondfile.views.renew, name="renew"),
    path('delete/<int:post_id>', secondfile.views.delete, name="delete"),
    path('accounts/signup', accounts.signup, name="signup"),
    path('accounts/login', accounts.login, name="login"),   
    path('accounts/logout', accounts.logout, name="logout"),     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
