from django.contrib import admin
from .models import User, Books, Tracking, Note


admin.site.register(User)
admin.site.register(Books)
admin.site.register(Tracking)
admin.site.register(Note)
