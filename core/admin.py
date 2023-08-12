from django.contrib import admin

from .models import JobPosition, Employee, Service, Feature

@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ['position', 'active']
    ordering = ['id']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'description','active']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'icon']
    ordering = ['id']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active']
    ordering = ['id']
    
