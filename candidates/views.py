from rest_framework.response import Response
from rest_framework.views import APIView
from candidates.models import Candidate, CandidateSkill
from candidates.serializers import CandidateSerializer, CandidateSkillSerializer


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
