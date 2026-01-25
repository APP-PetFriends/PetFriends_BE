from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import WalkRecord
from pet.models import Pet  # pet 앱에 있는 진짜 Pet 모델을 가져옵니다.
from .serializers import WalkRecordSerializer

# 1. 목록 조회(GET) 및 생성(POST)을 담당하는 뷰
class WalkRecordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pet_id = request.query_params.get('pet') # URL 파라미터에서 pet ID 추출
        if not pet_id:
            return Response({"message": "pet_id가 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)

        # 최신순 정렬: -walk_date (날짜 내림차순), -id (최신 등록순)

        queryset = WalkRecord.objects.filter(pet_id=pet_id).order_by('-walk_date', '-id')
        serializer = WalkRecordSerializer(queryset, many=True)
        
        return Response({
            "total_count": queryset.count(),
            "records": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
         # request.data에서 pet_id를 직접 꺼내지 않고 시리얼라이저에 맡깁니다.

        serializer = WalkRecordSerializer(data=request.data)
        if serializer.is_valid():
            pet_id = request.data.get('pet')
            try:
                pet = Pet.objects.get(id=pet_id)
                 # 소유권 확인 (403 Forbidden)

                if pet.user != request.user:
                    return Response({"message": "요청된 반려동물의 소유권이 일치하지 않습니다."}, status=status.HTTP_403_FORBIDDEN)
                # 저장 시 pet 객체를 명시적으로 넘겨줌

                serializer.save(pet=pet)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Pet.DoesNotExist:
                return Response({"message": "해당 반려동물이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. 특정 기록 수정(PATCH) 및 삭제(DELETE)를 담당하는 뷰
# 이 클래스 이름이 urls.py에서 임포트하려는 이름과 정확히 일치해야 합니다.
class WalkRecordDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        # 내가 쓴 기록인지 확인하며 가져오기

        record = get_object_or_404(WalkRecord, id=pk)
         # 권한 확인: 기록의 주인이 현재 로그인한 유저인지 체크

        if record.pet.user != request.user:
            return Response({"message": "수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        # partial=True를 넣어야 일부 필드만 수정(PATCH)이 가능합니다.


        serializer = WalkRecordSerializer(record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        record = get_object_or_404(WalkRecord, id=pk)
        # 권한 확인

        if record.pet.user != request.user:
            return Response({"message": "삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

        record.delete()
        return Response({"message": "기록이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)