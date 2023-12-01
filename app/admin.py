from django.contrib import admin
from .models import * #SignUp, About, Contact, Category_Cse, Cse, Eee, Category_Eee, Eng, Category_Eng, Bba, Category_Bba, Law, Category_Law, Civil, Category_Civil, Pharmacy, Category_Pharmacy


class SignUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'email', 'phone', 'image')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_title', 'about_desc', 'about_image')
    

class MissionAdmin(admin.ModelAdmin):
    list_display = ('mission_title', 'mission_desc', 'mission_image')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_title', 'team_desc', 'team_image')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_id', 'contact_message')
    
    
class CseAdmin(admin.ModelAdmin):
    list_display = ('cse_category', 'cse_book', 'cse_teacher')

class EeeAdmin(admin.ModelAdmin):
    list_display = ('eee_category', 'eee_book', 'eee_teacher')

class EngAdmin(admin.ModelAdmin):
    list_display = ('eng_category', 'eng_book', 'eng_teacher')

class BbaAdmin(admin.ModelAdmin):
    list_display = ('bba_category', 'bba_book', 'bba_teacher')

class LawAdmin(admin.ModelAdmin):
    list_display = ('law_category', 'law_book', 'law_teacher')

class CivilAdmin(admin.ModelAdmin):
    list_display = ('civil_category', 'civil_book', 'civil_teacher')

class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('pharmacy_category', 'pharmacy_book', 'pharmacy_teacher')
    
    
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('library_book', 'library_author')



# Register your models here.
admin.site.register(SignUp, SignUpAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category_Cse)
admin.site.register(Cse, CseAdmin)
admin.site.register(Category_Eee)
admin.site.register(Eee, EeeAdmin)
admin.site.register(Category_Eng)
admin.site.register(Eng, EngAdmin)
admin.site.register(Category_Bba)
admin.site.register(Bba, BbaAdmin)
admin.site.register(Category_Law)
admin.site.register(Law, LawAdmin)
admin.site.register(Category_Civil)
admin.site.register(Civil, CivilAdmin)
admin.site.register(Category_Pharmacy)
admin.site.register(Pharmacy, PharmacyAdmin)
admin.site.register(Library, LibraryAdmin)