from django.db import migrations


def copy_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(name=flat.owner,
                                               phonenumber=flat.owners_phonenumber,
                                               defaults={'phone_pure': flat.owner_phone_pure}
                                               )

        owner.flats.add(flat)

        owner.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(copy_owners),
    ]
