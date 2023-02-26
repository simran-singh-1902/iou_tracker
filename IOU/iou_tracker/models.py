from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    owes = models.JSONField(default=dict)
    owed_by = models.JSONField(default=dict)
    balance = models.JSONField(default=dict)

    def _str_(self):
        return self.name

    def update_balance(self):
        total_owed = sum(self.owed_by.values())
        total_owes = sum(self.owes.values())
        self.balance = {'owed': total_owed, 'owes': total_owes, 'net_balance': total_owed - total_owes}
        self.save()
