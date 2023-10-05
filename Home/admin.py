from django.contrib import admin
from .models import Contact
from .models import Feedback
from .models import Full_stack_developer
from .models import UI_UX_Designer
from .models import Front_End_Developer
from .models import Technical_Lead
from .models import Engineering_Manager

admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Full_stack_developer)
admin.site.register(UI_UX_Designer)
admin.site.register(Front_End_Developer)
admin.site.register(Technical_Lead)
admin.site.register(Engineering_Manager)