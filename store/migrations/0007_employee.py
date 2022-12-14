# Generated by Django 4.1.1 on 2022-10-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Name_Of_the_Person_taking_Appointment', models.CharField(max_length=50)),
                ('Relationship_with_patient', models.CharField(max_length=50)),
                ('PDA', models.IntegerField(default=0)),
                ('Dr', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(default=0)),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
    ]
