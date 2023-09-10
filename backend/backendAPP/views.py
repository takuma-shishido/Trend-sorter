from rest_framework.views import APIView
from rest_framework.response import Response
from .trend import find_trend
from .models import Repository

class TrendAPIView(APIView):
    def get(self, request, span, lang):
        responceData = []

        datas = Repository.objects.filter(span=span,lang=lang).all()
        for data in datas:
            responceData.append({
                "Name": data.name,
                "URL":  data.url, 
                "Description": data.description,
                "Lang": data.lang,
                "Star": data.star,
                "StarBySpan": data.star_by_span,
                "Fork": data.fork
            })
    
        return Response(responceData)