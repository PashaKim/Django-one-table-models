# Generated by Django 2.2.6 on 2019-10-17 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NodeA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_a', models.CharField(blank=True, max_length=75, null=True)),
            ],
            options={
                'db_table': 'Nodes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NodeParrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_parrent', models.CharField(blank=True, max_length=75, null=True)),
                ('name_a', models.CharField(blank=True, max_length=75, null=True)),
                ('name_b', models.CharField(blank=True, max_length=75, null=True)),
                ('name_c', models.CharField(blank=True, max_length=75, null=True)),
            ],
            options={
                'db_table': 'Nodes',
            },
        ),
        migrations.CreateModel(
            name='NodeB',
            fields=[
                ('nodea_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.NodeA')),
                ('name_b', models.CharField(blank=True, max_length=75, null=True)),
            ],
            options={
                'db_table': 'Nodes',
                'managed': False,
            },
            bases=('content.nodea',),
        ),
        migrations.CreateModel(
            name='NodeC',
            fields=[
                ('nodeb_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.NodeB')),
                ('name_c', models.CharField(blank=True, max_length=75, null=True)),
            ],
            options={
                'db_table': 'Nodes',
                'managed': False,
            },
            bases=('content.nodeb',),
        ),
    ]
