from django.urls import path
from .views import CreateListExecution, RetrieveUpdateDeleteExecution

urlpatterns = [
    # service
    path("execution/add", CreateListExecution.as_view()),
    path("execution/list", CreateListExecution.as_view()),
    path("execution/update/<int:pk>", RetrieveUpdateDeleteExecution.as_view()),
    path("execution/patch/<int:pk>", RetrieveUpdateDeleteExecution.as_view()),
    path("execution/delete/<int:pk>", RetrieveUpdateDeleteExecution.as_view()),
    # path('execution/add', CreateListExecution.as_view({'post': 'post'})),
    # path('execution/list', CreateListExecution.as_view({'get': 'get'})),
    # path('execution/update/<int:pk>', RetrieveUpdateDeleteExecution.as_view({'put' : 'put'})),
    # path('execution/patch/<int:pk>', RetrieveUpdateDeleteExecution.as_view({'patch' : 'patch'})),
    # path('execution/delete/<int:pk>', RetrieveUpdateDeleteExecution.as_view({'delete' : 'delete'})),
]
