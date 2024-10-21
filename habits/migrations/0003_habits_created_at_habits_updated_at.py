from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="habits",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
        migrations.AddField(
            model_name="habits",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Укажите дату изменения",
                null=True,
                verbose_name="Дата изменения",
            ),
        ),
    ]
