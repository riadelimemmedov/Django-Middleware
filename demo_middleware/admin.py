from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
from .models import *
# Register your models here.

@admin.register(NewStats)
class NewStatsAdmin(admin.ModelAdmin):
    def changelist_view(self,request,extra_context=None):
        stat_data = (
            NewStats.objects.all().annotate().values('win','mac','iph','android','oth')
        )

        #?If used serializers.serialize
        # data = NewStats.objects.all()
        # newdata = serializers.serialize('json',list(data),fields=('win','mac','iph','android','oth'))
        # print('Serialized newData ', newdata)
        
        #!Or used djangoJsonEncoder
        as_json = json.dumps(list(stat_data),cls=DjangoJSONEncoder)#The JSON dump method takes an optional cls parameter to pass your own JSON encoder implementation. The custom JSON encoder will be used for Python to JSON conversions instead of the base JSONEncoder class.
        extra_context = extra_context or {"stat_data":as_json}
        
        #return response to template
        return super(NewStatsAdmin,self).changelist_view(request,extra_context=extra_context)
    