from django.urls import path

from webapp.views import AnnounceListView, AnnounceCreateView, AnnounceUpdateView, AnnounceDetailView, AnnounceNewList, \
    AnnounceModUpdate, AnnounceDeleteView

app_name = "webapp"

urlpatterns = [
    path('', AnnounceListView.as_view(), name="announce_list"),
    path('announce/create/', AnnounceCreateView.as_view(), name="announce_create"),
    path('announce/update/<int:pk>/', AnnounceUpdateView.as_view(), name="announce_update"),
    path('announce/detail/<int:pk>/', AnnounceDetailView.as_view(), name="announce_detail"),
    path('announce/moder/list/', AnnounceNewList.as_view(), name="announce_moder_list"),
    path('announce/moder/<int:pk>/update/', AnnounceModUpdate.as_view(),
         name="announce_moder_update"),
    path('announce/delete/<int:pk>/', AnnounceDeleteView.as_view(), name="announce_delete"),
]
