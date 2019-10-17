from django.db import models


class NodeParrent(models.Model):
    name_parrent = models.CharField(max_length=75, blank=True, null=True)
    name_a = models.CharField(max_length=75, blank=True, null=True)
    name_b = models.CharField(max_length=75, blank=True, null=True)
    name_c = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Node Parrent'
        verbose_name = 'Node Parrent'
        db_table = 'Nodes'


class NodeA(models.Model):
    name_a = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Node A'
        verbose_name = 'Node A'
        db_table = 'Nodes'
        managed = False


class NodeB(models.Model):
    name_b = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Node B'
        verbose_name = 'Node B'
        db_table = 'Nodes'
        managed = False


class NodeC(models.Model):
    name_c = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Node C'
        verbose_name = 'Node C'
        db_table = 'Nodes'
        managed = False


class NodeAB(models.Model):
    name_a = models.CharField(max_length=75, blank=True, null=True)
    name_b = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Node AB'
        verbose_name = 'Node AB'
        db_table = 'Nodes'
        managed = False
