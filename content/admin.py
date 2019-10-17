from django.contrib import admin
import content.models as models


@admin.register(models.NodeParrent)
class NodeParrentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_parrent', 'name_a', 'name_b', 'name_c')


@admin.register(models.NodeA)
class NodeAAdmin(admin.ModelAdmin):
    list_display = ('id',  'name_a',)


@admin.register(models.NodeB)
class NodeBAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_b',)


@admin.register(models.NodeC)
class NodeCAdmin(admin.ModelAdmin):
    list_display = ('id',  'name_c')


@admin.register(models.NodeAB)
class NodeCAdmin(admin.ModelAdmin):
    list_display = ('id',  'name_a', 'name_b')