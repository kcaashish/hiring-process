from django.db import models

class Jobs(models.Model):
    job_title = models.CharField(max_length=100)

class JobSkills(models.Model):
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    skills_name = models.CharField(max_length=100)