from django.db import models

class ExpirienceLevel(models.Model):
    level_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'edutime'


class Ratings(models.Model):
    rating_id = models.SmallIntegerField(primary_key=True)
    rating_description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        app_label = 'edutime'

class Specializations(models.Model):
    spec_id = models.AutoField(primary_key=True)
    spec_name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'edutime'

class Teachers(models.Model):
    teacher = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    work_company = models.CharField(max_length=100, blank=True, null=True)
    common_rate_per_hr = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'edutime'

class TeachersSpecializations(models.Model):
    teacher = models.ForeignKey(Teachers, models.DO_NOTHING, primary_key=True)
    spec = models.ForeignKey(Specializations, models.DO_NOTHING)
    exp_level = models.ForeignKey(ExpirienceLevel, models.DO_NOTHING)
    exp_time = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)

    class Meta:
        app_label = 'edutime'

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    credit_card_num = models.CharField(max_length=19, blank=True, null=True)
    balance = models.BigIntegerField(blank=True, null=True)

    class Meta:
        app_label = 'edutime'
