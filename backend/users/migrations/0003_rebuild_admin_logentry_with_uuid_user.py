from django.db import migrations


def rebuild_admin_logentry_for_uuid_user(apps, schema_editor):
    LogEntry = apps.get_model("admin", "LogEntry")

    with schema_editor.connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM django_admin_log")
        row_count = cursor.fetchone()[0]

    if row_count:
        raise RuntimeError(
            "Cannot rebuild django_admin_log automatically because it contains "
            f"{row_count} row(s). Clear or migrate that data manually first."
        )

    schema_editor.delete_model(LogEntry)
    schema_editor.create_model(LogEntry)


class Migration(migrations.Migration):
    dependencies = [
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("users", "0002_alter_user_role"),
    ]

    operations = [
        migrations.RunPython(
            rebuild_admin_logentry_for_uuid_user,
            migrations.RunPython.noop,
        ),
    ]
