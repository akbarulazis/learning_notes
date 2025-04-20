

from django.contrib.auth.mixins import LoginRequiredMixin
from apps.notes.models import Note
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import View, ListView, DetailView
from .forms import NoteForm


class HomeView(View):
    def get(self, request):
        return render(request, 'notes/home.html')

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        notes = Note.objects.filter(author=request.user).order_by('-created_at')
        context = {
            'notes': notes,
        }
        return render(request, 'notes/dashboard.html', context)
    


# Class-based view for listing notes
class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    
    def get_queryset(self):
        # Only show notes belonging to the current user
        return Note.objects.filter(author=self.request.user).order_by('-created_at')

# Class-based view for viewing a note
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'
    
    def get_queryset(self):
        # Only allow viewing notes that belong to the current user
        return Note.objects.filter(author=self.request.user)

# Class-based view for creating a note
class NoteCreateView(LoginRequiredMixin, View):
    template_name = 'notes/note_form.html'
    
    def get(self, request):
        form = NoteForm()
        context = {
            'form': form,
            'title': 'Create New Note',
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            messages.success(request, "Note created successfully!")
            return redirect('note_detail', slug=note.slug)
        
        context = {
            'form': form,
            'title': 'Create New Note',
        }
        return render(request, self.template_name, context)

# Class-based view for editing a note
class NoteEditView(LoginRequiredMixin, View):
    template_name = 'notes/note_form.html'
    
    def get(self, request, slug):
        note = get_object_or_404(Note, slug=slug, author=request.user)
        form = NoteForm(instance=note)
        context = {
            'form': form,
            'note': note,
            'title': 'Edit Note',
        }
        return render(request, self.template_name, context)
    
    def post(self, request, slug):
        note = get_object_or_404(Note, slug=slug, author=request.user)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            messages.success(request, "Note updated successfully!")
            return redirect('note_detail', slug=note.slug)
        
        context = {
            'form': form,
            'note': note,
            'title': 'Edit Note',
        }
        return render(request, self.template_name, context)


class NoteDeleteView(LoginRequiredMixin, View):
    template_name = 'notes/note_confirm_delete.html'
    
    def get(self, request, slug):
        note = get_object_or_404(Note, slug=slug, author=request.user)
        context = {
            'note': note,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, slug):
        note = get_object_or_404(Note, slug=slug, author=request.user)
        note.delete()
        messages.success(request, "Note deleted successfully!")
        return redirect('note_list')