from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_role_shop"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AddConstraint(
            model_name="role",
            constraint=models.UniqueConstraint(
                fields=("shop", "name"),
                name="unique_role_name_per_shop",
            ),
        ),
    ]
