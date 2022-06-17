from rest_framework.response import Response
from rest_framework.views import APIView
from candidates.models import Candidate, CandidateSkill
from candidates.serializers import CandidateSerializer, CandidateSkillSerializer
from jobs.models import Job, JobSkill
from jobs.serializers import JobSerializer, JobSkillSerializer


class CandidateView(APIView):

    def get(self, request):
        '''List all candidates'''
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        '''Create a new candidate'''
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CandidateSkillView(APIView):

    def get(self, request):
        '''List all candidateskills'''
        candidateskills = CandidateSkill.objects.all()
        serializer = CandidateSkillSerializer(candidateskills, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''Create a new candidateskill'''
        serializer = CandidateSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BestCandidateView(APIView):

    def post(self, request):
        '''Return the best candidate with the most matched skill for the job'''
        job = JobSerializer(data=request.data)
        if not job.is_valid():
            return Response(job.errors, status=400)
        job_skills = JobSkill.objects.filter(job_id__job_title=job.data['job_title']).values_list('skills_name', flat=True)
        candidates = Candidate.objects.all()
        best_candidate = None
        best_match = 0
        for candidate in candidates:
            candidate_skills = CandidateSkill.objects.filter(candidate_id=candidate.id).values_list('skills_name', flat=True)
            overlaping_skills = set(candidate_skills).intersection(set(job_skills))
            overlaping_percentage = float(len(overlaping_skills) / len(job_skills)) * 100
            if overlaping_percentage > best_match:
                best_match = overlaping_percentage
                best_candidate = candidate
        serializer = CandidateSerializer(best_candidate)
        return Response(serializer.data)
