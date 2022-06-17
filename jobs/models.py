from django.db import models

class Jobs(models.Model):
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title

class JobSkills(models.Model):
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    skills_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skills_name