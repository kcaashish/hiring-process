from rest_framework.response import Response
from rest_framework.views import APIView
from jobs.models import Job, JobSkill
from jobs.serializers import JobSerializer, JobSkillSerializer

class JobView(APIView):

    def get(self, request):
        '''List all jobs'''
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''Create a new job'''
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class JobSkillView(APIView):

    def get(self, request):
        '''List all jobskills'''
        jobskills = JobSkill.objects.all()
        serializer = JobSkillSerializer(jobskills, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''Create a new jobskill'''
        serializer = JobSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
