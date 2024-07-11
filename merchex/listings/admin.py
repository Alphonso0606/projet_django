# listings/admin.py

from django.contrib import admin
from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')  # list the fields we want on the list display

admin.site.register(Band, BandAdmin)  # we modify this line, adding a second argument

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')  # ajouter ‘band' ici

admin.site.register(Listing, ListingAdmin)  # we modify this line, adding a second argument
