from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0011_alter_habits_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="habits",
            name="utc_time",
            field=models.TimeField(
                blank=True,
                null=True,
                verbose_name="Время исполнения привычки в формате UTC, вычисляется автоматически по time_offset пользователя",
            ),
        ),
    ]
