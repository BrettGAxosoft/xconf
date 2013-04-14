from django.contrib import admin
from .models import Type, Slot, Track, Schedule


class SlotInline(admin.TabularInline):
    model = Slot


class TrackAdmin(admin.ModelAdmin):
    inlines = [
        SlotInline,
    ]


class TrackInline(admin.TabularInline):
    model = Track


class ScheduleAdmin(admin.ModelAdmin):
    inlines = [
        TrackInline,
    ]


admin.site.register(Type)
admin.site.register(Slot)
admin.site.register(Track, TrackAdmin)
admin.site.register(Schedule, TrackAdmin)