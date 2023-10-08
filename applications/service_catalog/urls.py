from django.urls import path
from .views import (
    CreateListService,
    RetrieveUpdateDeleteService,
    CreateListDbserver,
    RetrieveUpdateDeleteDbserver,
    CreateListSchema,
    RetrieveUpdateDeleteSchema,
    CreateListTable,
    RetrieveUpdateDeleteTable,
    CreateListPolicy,
    RetrieveUpdateDeletePolicy,
)

urlpatterns = [
    # service
    path("service/add", CreateListService.as_view()),
    path("service/list", CreateListService.as_view()),
    path("service/update/<int:pk>", RetrieveUpdateDeleteService.as_view()),
    path("service/patch/<int:pk>", RetrieveUpdateDeleteService.as_view()),
    path("service/delete/<int:pk>", RetrieveUpdateDeleteService.as_view()),
    # DbServer
    path("dbserver/add", CreateListDbserver.as_view()),
    path("dbserver/list", CreateListDbserver.as_view()),
    path("dbserver/update/<int:pk>", RetrieveUpdateDeleteDbserver.as_view()),
    path("dbserver/patch/<int:pk>", RetrieveUpdateDeleteDbserver.as_view()),
    path("dbserver/delete/<int:pk>", RetrieveUpdateDeleteDbserver.as_view()),
    # schema
    path("schema/add", CreateListSchema.as_view()),
    path("schema/list", CreateListSchema.as_view()),
    path("schema/update/<int:pk>", RetrieveUpdateDeleteSchema.as_view()),
    path("schema/patch/<int:pk>", RetrieveUpdateDeleteSchema.as_view()),
    path("schema/delete/<int:pk>", RetrieveUpdateDeleteSchema.as_view()),
    # table
    path("table/add", CreateListTable.as_view()),
    path("table/list", CreateListTable.as_view()),
    path("table/update/<int:pk>", RetrieveUpdateDeleteTable.as_view()),
    path("table/patch/<int:pk>", RetrieveUpdateDeleteTable.as_view()),
    path("table/delete/<int:pk>", RetrieveUpdateDeleteTable.as_view()),
    # policy
    path("policy/add", CreateListPolicy.as_view()),
    path("policy/list", CreateListPolicy.as_view()),
    path("policy/update/<int:pk>", RetrieveUpdateDeletePolicy.as_view()),
    path("policy/patch/<int:pk>", RetrieveUpdateDeletePolicy.as_view()),
    path("policy/delete/<int:pk>", RetrieveUpdateDeletePolicy.as_view()),
]

# urlpatterns = [
#     # service
#     path('service/add', CreateListService.as_view({'post': 'post'})),
#     path('service/list', CreateListService.as_view({'get': 'get'})),
#     path('service/update/<int:pk>', RetrieveUpdateDeleteService.as_view({'put' : 'put'})),
# 	path('service/patch/<int:pk>', RetrieveUpdateDeleteService.as_view({'patch' : 'patch'})),
#     path('service/delete/<int:pk>', RetrieveUpdateDeleteService.as_view({'delete' : 'delete'})),
#
#     # DbServer
#     path('dbserver/add', CreateListDbserver.as_view({'post': 'post'})),
#     path('dbserver/list', CreateListDbserver.as_view({'get': 'get'})),
#     path('dbserver/update/<int:pk>', RetrieveUpdateDeleteDbserver.as_view({'put' : 'put'})),
# 	path('dbserver/patch/<int:pk>', RetrieveUpdateDeleteDbserver.as_view({'patch' : 'patch'})),
#     path('dbserver/delete/<int:pk>', RetrieveUpdateDeleteDbserver.as_view({'delete' : 'delete'})),
#
#     # schema
#     path('schema/add', CreateListSchema.as_view({'post': 'post'})),
#     path('schema/list', CreateListSchema.as_view({'get': 'get'})),
#     path('schema/update/<int:pk>', RetrieveUpdateDeleteSchema.as_view({'put' : 'put'})),
# 	path('schema/patch/<int:pk>', RetrieveUpdateDeleteSchema.as_view({'patch' : 'patch'})),
#     path('schema/delete/<int:pk>', RetrieveUpdateDeleteSchema.as_view({'delete' : 'delete'})),
#
#     # table
#     path('table/add', CreateListTable.as_view({'post': 'post'})),
#     path('table/list', CreateListTable.as_view({'get': 'get'})),
#     path('table/update/<int:pk>', RetrieveUpdateDeleteTable.as_view({'put' : 'put'})),
# 	path('table/patch/<int:pk>', RetrieveUpdateDeleteTable.as_view({'patch' : 'patch'})),
#     path('table/delete/<int:pk>', RetrieveUpdateDeleteTable.as_view({'delete' : 'delete'})),
#
#     # policy
#     path('policy/add', CreateListPolicy.as_view({'post': 'post'})),
#     path('policy/list', CreateListPolicy.as_view({'get': 'get'})),
#     path('policy/update/<int:pk>', RetrieveUpdateDeletePolicy.as_view({'put' : 'put'})),
# 	path('policy/patch/<int:pk>', RetrieveUpdateDeletePolicy.as_view({'patch' : 'patch'})),
#     path('policy/delete/<int:pk>', RetrieveUpdateDeletePolicy.as_view({'delete' : 'delete'})),
# ]
