# Generated by Django 3.0 on 2020-10-15 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookBlog', '0004_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='book',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Book', to='BookBlog.Books'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='genre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='BookBlog.Genre'),
            preserve_default=False,
        ),
    ]
