
from django.conf.urls import url
from django.contrib import admin
from MySubmissions import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.login_view,name="login"),
    url(r'logout/$',views.logout_view,name="logout"),
    url(r'index/$',views.index,name="index"),
    url(r'posts/$',views.posted,name="post"),
    url(r'^assignmentList/(?P<subjects>[\f\w-]+)/$',views.assignmentList,name='assignmentList'),
    url(r'^uploadsInfo/(?P<upload>[\f\w-]+)/$',views.uploadInfo,name='uploadInfo'),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
