from django.contrib import admin
from .models import UploadFile, Report
from django.utils.html import format_html

# Register your models here.

class ReportInline(admin.TabularInline):
    model = Report
    can_delete = True

@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):
    # to change display in admin panel
    list_display = ['id', 'user_name', 'type', 'show_file_location']
    list_filter = ['user_name']
    search_fields = ['user_name']
    inlines = [ReportInline]

    def show_file_location(self, obj):
        if obj.link_to_file is not None:
            return format_html(f'<a href = "{obj.link_to_file}" target= "_blank"> {obj.link_to_file} </a>')
        else:
            return ''

    show_file_location.short_description = "URL"



@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    # to change display in admin panel
    list_display = ['upload_file', 'calculate_date']
    list_filter = ['upload_file', 'calculate_date']