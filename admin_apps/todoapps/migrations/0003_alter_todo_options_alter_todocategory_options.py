# Generated by Django 4.2.3 on 2023-07-23 06:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todoapps", "0002_alter_todo_options_alter_todocategory_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={"verbose_name": "TODOタスク", "verbose_name_plural": "TODOタスク"},
        ),
        migrations.AlterModelOptions(
            name="todocategory",
            options={"verbose_name": "TODOカテゴリ", "verbose_name_plural": "TODOカテゴリ"},
        ),
    ]
