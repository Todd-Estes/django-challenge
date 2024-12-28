from django.db import models

# Create your models here.


class Template(models.Model):
  body = models.CharField(max_length=100, blank=False)

  def __str__(self):
    return self.body[:50]
  
  class Meta:
    db_table = 'templates'

class Notification(models.Model):
  phone_number = models.CharField(max_length=15, blank=False)
  template = models.ForeignKey(
    Template,
    on_delete=models.CASCADE,
    related_name='notifications',
    null=False
  )

  personalization = models.CharField(max_length=50, blank=True, null=True)

  def __str__(self):
    return f"Notification for {self.phone_number}"
  
  class Meta:
    db_table = 'notifications'

