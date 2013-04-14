from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin

from .models import Type, Slot, Track, Schedule


class SlotInline(TabularDynamicInlineAdmin):
    model = Slot
    extra = 10

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
admin.site.register(Schedule, ScheduleAdmin)