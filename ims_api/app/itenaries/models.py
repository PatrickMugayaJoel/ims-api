from django.db import models
from ims_api.app.authentication.models import Company


class Itenary(models.Model):
    """
    Model class for creating and manipulating an itenary
    """
    name = models.CharField(max_length=300)
    thumbnail = models.TextField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateField(null=True)
