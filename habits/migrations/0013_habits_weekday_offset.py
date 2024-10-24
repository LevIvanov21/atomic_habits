from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0012_habits_utc_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="habits",
            name="weekday_offset",
            field=models.IntegerField(
                default=0,
                verbose_name="Смещение дня недели относительно UTC. Заполняется автоматически.",
            ),
        ),
    ]
