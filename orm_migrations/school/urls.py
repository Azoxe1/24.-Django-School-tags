from django.urls import path

from school.views import students_list

urlpatterns = [
    path('', students_list, name='students'),
]


# from school.views import StudentListView

# urlpatterns = [
#     path('', StudentListView.as_view()),
# ]
