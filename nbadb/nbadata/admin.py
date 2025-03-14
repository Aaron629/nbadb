from django.contrib import admin
from nbadata.models import Nba_news
# Register your models here.
class Nba_newsAdmin(admin.ModelAdmin):
  list_display=('title','ldate','luser','iobool')
  search_fields=('title',)
admin.site.register(Nba_news,Nba_newsAdmin)