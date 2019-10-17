from django.http import JsonResponse
from content.models import NodeA, NodeB, NodeC, NodeAB
# Create your views here.

def table(request):
    nodeA = list(NodeA.objects.values())
    nodeB = list(NodeB.objects.values())
    nodeC = list(NodeC.objects.values())
    nodeAB = list(NodeAB.objects.values())
    return JsonResponse({'A': nodeA,
                         'B': nodeB,
                         'C': nodeC,
                         'AB': nodeAB})
