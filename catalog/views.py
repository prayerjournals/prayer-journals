from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


from catalog.models import Note
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

#list view of all a person's notes
class index(LoginRequiredMixin, generic.ListView):
    model = Note
    paginate_by = 10
    ordering = ['-date']

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-date')





from django.contrib.auth.mixins import PermissionRequiredMixin

#list view of everyone's notes - used for staff 
class all_notes(PermissionRequiredMixin, generic.ListView):
    model = Note
    permission_required = 'catalog.can_view_all_notes'
    paginate_by = 10
    template_name ='catalog/note_list_all.html'
    ordering = ['-date']


@login_required
def note_view(request, pk):
    print("========", pk)
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404('Note does not exist')

    return render(request, 'catalog/note_view.html', context={'note' : note })

    


from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import NoteForm



# creates a completely new note 
@login_required
def note_new(request):
        
    if request.method == 'POST':
    
        noteForm = NoteForm(request.POST, request.FILES)
    
        if noteForm.is_valid():
            note_form = noteForm.save(commit=False)
            note_form.user = request.user
            note_form.save()
                    
            # use django messages framework
            print("updated form successfully")
            return HttpResponseRedirect("/")
        else:
            print(noteForm.errors)
    else:
        noteForm = NoteForm()
    return render(request, 'catalog/note_edit.html', {'noteForm': noteForm, })
    



# Fills in an existing note
from django.http import Http404
from django.http import HttpResponseForbidden

@login_required
def note_old(request, pk):

    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404('Note does not exist')

    if note.user == request.user or request.user.has_perm('catalog.can_view_all_notes'):
        #submitting the form
        if request.method == 'POST':

            #sending the data, overwrite an existing thing rather than create a new one 
            noteForm = NoteForm(request.POST, request.FILES, instance=note)

            if noteForm.is_valid():
                note_form = noteForm.save(commit=False)
                note_form.user = request.user
                note_form.save()

                # use django messages framework
                print("updated form successfully")
                return HttpResponseRedirect("/")
            else:
                print('cannot overwrite a note you have not made')
        else:
            #fill in data 
            f = NoteForm(initial={ 'title': note.title,
                                'body' : note.body, })

        return render(request, 'catalog/note_edit.html', {'noteForm': f, 'note': note})

    else:
        return HttpResponseRedirect("/") 
