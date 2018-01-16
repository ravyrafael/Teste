# Generated by Django 2.0.1 on 2018-01-16 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='historico',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teste.Usuario'),
        ),
    ]