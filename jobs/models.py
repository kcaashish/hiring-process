from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title

class JobSkill(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    skills_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skills_name