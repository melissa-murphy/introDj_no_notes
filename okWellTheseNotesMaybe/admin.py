from django.contrib import admin
from .models import Note
from .models import NoteAdmin
from .models import PersonalNote

admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)
