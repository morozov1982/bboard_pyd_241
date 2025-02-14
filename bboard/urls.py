from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic.dates import WeekArchiveView, DayArchiveView
from django.views.generic.edit import CreateView

from bboard.models import Bb
from bboard.views import (index, by_rubric, BbCreateView,
                          add_and_save, bb_detail, BbRubricBbsView,
                          BbDetailView, BbEditView, BbDeleteView, BbIndexView,
                          BbRedirectView, edit, rubrics, bbs, search, api_rubrics, api_rubric_detail)

app_name = 'bboard'

urlpatterns = [
    path('api/rubrics/<int:pk>/', api_rubric_detail),
    path('api/rubrics/', api_rubrics),

    path('rubrics/', rubrics, name='rubrics'),
    path('bbs/<int:rubric_id>/', bbs, name='bbs'),

    path('add/', BbCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
    # path('edit/<int:pk>/', edit, name='edit'),

    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),

    path('<int:rubric_id>/',
         BbRubricBbsView.as_view(),
         # cache_page(60 * 5)(BbRubricBbsView.as_view()),
         # cache_page(30)(BbRubricBbsView.as_view()),
         name='by_rubric'),

    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),

    path('search/', search, name='search'),

    path('', index, name='index'),
    # path('', BbIndexView.as_view(), name='index'),
]
