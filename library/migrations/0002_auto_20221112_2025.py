# Generated by Django 3.1.14 on 2022-11-12 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, default='', max_length=500)),
                ('title', models.CharField(blank=True, default='', max_length=500)),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(max_length=500)),
                ('featured_field', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='note',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='note_name',
            field=models.CharField(default='notename', max_length=500),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='note',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booknotes', to='library.books'),
        ),
        migrations.AddConstraint(
            model_name='books',
            constraint=models.UniqueConstraint(fields=('author', 'title'), name='books'),
        ),
    ]
