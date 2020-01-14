from django.db import migrations

import phonenumbers


def set_owner_phone_pure(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():

        if not flat.owners_phonenumber:
            continue

        parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')

        if not phonenumbers.is_possible_number(parsed_number):
            continue

        if not phonenumbers.is_valid_number(parsed_number):
            continue

        flat.owner_phone_pure = phonenumbers.format_number(parsed_number,
                                                           phonenumbers.PhoneNumberFormat.E164)

        flat.save()


def reset_owner_phone_pure(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        flat.owner_phone_pure = None

        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0007_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(set_owner_phone_pure, reset_owner_phone_pure),
    ]
