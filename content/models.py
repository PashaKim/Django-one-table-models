from django.db import models


class NodeParrent(models.Model):
    name_parrent = models.CharField(max_length=75, blank=True, null=True)
    name_a = models.CharField(max_length=75, blank=True, null=True)
    name_b = models.CharField(max_length=75, blank=True, null=True)
    name_c = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        db_table = 'Nodes'


class NodeA(models.Model):

    name_a = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        db_table = 'Nodes'
        managed = False


class NodeB(models.Model):

    name_b = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        db_table = 'Nodes'
        managed = False


class NodeC(models.Model):

    name_c = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        db_table = 'Nodes'
        managed = False


class NodeAB(models.Model):
    name_a = models.CharField(max_length=75, blank=True, null=True)
    name_b = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        db_table = 'Nodes'
        managed = False
