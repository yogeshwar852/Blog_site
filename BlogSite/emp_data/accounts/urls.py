from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('b_index/', views.b_index, name='b_index'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('employee_insert/', views.employee_insert, name='employee_insert'),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_Order, name="delete_order"),
    path('del_post/<int:id>/', views.del_post, name="del_post"),
    path('User_list/', views.User_list.as_view(), name="User_list"),
    path('blog/', views.blog, name="blog"),
    # path('blog_post/', views.blog_post, name="blog_post"),
    path('post/<int:id>', views.post, name="post"),
    path('logout/', views.logout_page, name='logout')
]