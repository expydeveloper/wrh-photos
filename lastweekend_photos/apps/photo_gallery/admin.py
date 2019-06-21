from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User, PhotoOrder, Cart, Photo, PhotoPeople, PhotoTag, Event, Sponsor, Photographer, PhotoAds


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('gender', 'avatar')}),
    )


class PhotoAdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'ads_sponsor', 'ads_position', 'file', 'create_datetime', 'update_datetime')


admin.site.register(User, MyUserAdmin)
admin.site.register(Photographer)
admin.site.register(Sponsor)
admin.site.register(Event)
admin.site.register(PhotoTag)
admin.site.register(PhotoPeople)
admin.site.register(Photo)
admin.site.register(Cart)
admin.site.register(PhotoOrder)
admin.site.register(PhotoAds, PhotoAdsAdmin)
