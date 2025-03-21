from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=250)
    last_name = fields.CharField(max_length=250)
    username = fields.CharField(max_length=250)
    birthdate = fields.DateField()
    time_left = fields.CharField(max_length=250)
    share_link = fields.CharField(max_length=250)

    class Meta:
        table = "users"
