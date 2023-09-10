from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from.views import TrendAPIView

urlpatterns = [
    path('api/getTrend/<str:span>/<str:lang>', TrendAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)