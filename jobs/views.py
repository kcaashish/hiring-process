from django.http import JsonResponse
from rest_framework.views import APIView
from jobs.models import Job, JobSkill
from jobs.serializers import JobSerializer, JobSkillSerializer

class JobView(APIView):

    def get(self, request):
        '''List all jobs'''
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        '''Create a new job'''
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)


class JobSkillView(APIView):

    def get(self, request):
        '''List all jobskills'''
        jobskills = JobSkill.objects.all()
        serializer = JobSkillSerializer(jobskills, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        '''Create a new jobskill'''
        serializer = JobSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)
