from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Database.models import TestItem
from utility.serializer import TestItemSerializer
from api.Pagination import CustomPagination   # 👈 correct import

# ✅ GET all items (with pagination)
@api_view(['GET'])
def get_testitems(request):
    items = TestItem.objects.all().order_by("id")  # order_by important for pagination
    paginator = CustomPagination()
    result_page = paginator.paginate_queryset(items, request)
    serializer = TestItemSerializer(result_page, many=True)

    return paginator.get_paginated_response({
        "success": 1,
        "message": "Test Items fetched with pagination",
        "data": serializer.data
    })


# ✅ GET single item
@api_view(['GET'])
def get_testitem(request, item_id):
    try:
        item = TestItem.objects.get(id=item_id)
        serializer = TestItemSerializer(item)
        return Response({
            "success": True,
            "message": "Single Test Item fetched successfully",
            "data": serializer.data
        })
    except TestItem.DoesNotExist:
        return Response({
            "success": False,
            "message": "Test Item not found",
            "data": None
        }, status=404)


# ✅ CREATE new item
@api_view(['POST'])
def create_testitem(request):
    name = request.data.get("name")
    description = request.data.get("description")
    if not name or not description:
        return Response({
            "success": False,
            "message": "Name and description required",
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)

    item = TestItem.objects.create(name=name, description=description)
    serializer = TestItemSerializer(item)
    return Response({
        "success": True,
        "message": "Test Item created successfully",
        "data": serializer.data
    }, status=status.HTTP_201_CREATED)


# ✅ UPDATE item
@api_view(['PUT'])
def update_testitem(request, item_id):
    try:
        item = TestItem.objects.get(id=item_id)
    except TestItem.DoesNotExist:
        return Response({
            "success": False,
            "message": "Item not found",
            "data": None
        }, status=status.HTTP_404_NOT_FOUND)

    item.name = request.data.get("name", item.name)
    item.description = request.data.get("description", item.description)
    item.save()

    serializer = TestItemSerializer(item)
    return Response({
        "success": True,
        "message": "Test Item updated successfully",
        "data": serializer.data
    })


# ✅ DELETE item
@api_view(['DELETE'])
def delete_testitem(request, item_id):
    try:
        item = TestItem.objects.get(id=item_id)
    except TestItem.DoesNotExist:
        return Response({
            "success": False,
            "message": "Item not found",
            "data": None
        }, status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response({
        "success": True,
        "message": "Item deleted successfully",
        "data": None
    }, status=status.HTTP_200_OK)
