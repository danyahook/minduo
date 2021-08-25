from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from cards.models import Card
from cards.serializers import CardSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def card_list(request):
    if request.method == 'GET':
        cards = Card.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            cards = cards.filter(title__icontains=title)

        cards_serializer = CardSerializer(cards, many=True)
        return JsonResponse(cards_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        card_data = JSONParser().parse(request)
        card_serializer = CardSerializer(data=card_data)
        if card_serializer.is_valid():
            card_serializer.save()
            return JsonResponse(card_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Card.objects.all().delete()
        return JsonResponse({'message': '{} Cards were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def card_detail(request, pk):
    try:
        card = Card.objects.get(pk=pk)
    except Card.DoesNotExist:
        return JsonResponse({'message': 'The card does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        card_serializer = CardSerializer(card)
        return JsonResponse(card_serializer.data)

    elif request.method == 'PUT':
        card_data = JSONParser().parse(request)
        card_serializer = CardSerializer(card, data=card_data)
        if card_serializer.is_valid():
            card_serializer.save()
            return JsonResponse(card_serializer.data)
        return JsonResponse(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        card.delete()
        return JsonResponse({'message': 'Card was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
