
from django.db import models

class LegalKnowledge(models.Model):
    category = models.CharField(max_length=255)
    query_keywords = models.TextField()
    legal_advice = models.TextField()
    applicable_laws = models.TextField()

    def __str__(self):
        return self.category
