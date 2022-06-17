from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class CandidateSkills(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    skills_name = models.CharField(max_length=100)
