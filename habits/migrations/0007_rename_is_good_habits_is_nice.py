from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0006_alter_habits_prize"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habits",
            old_name="is_good",
            new_name="is_nice",
        ),
    ]
