
from django.urls import path
from .views import ( HomeView, DashboardView,    NoteListView, 
    NoteDetailView, 
    NoteCreateView, 
    NoteEditView,
    NoteDeleteView )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('notes/create/', NoteCreateView.as_view(), name='note_create'),
    path('notes/<slug:slug>/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/<slug:slug>/edit/', NoteEditView.as_view(), name='note_edit'),
    path('notes/<slug:slug>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]