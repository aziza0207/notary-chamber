import random

import pytest
from django.urls import reverse
from rest_framework import status

from .factories import NewsFactory


@pytest.mark.django_db
def test_search_title_and_date(api_client):
    news_list_page = [NewsFactory() for i in range(10)]
    random_news_item = random.choice(news_list_page)
    url = reverse('content:news')

    # Search by title

    query_params = {"title": random_news_item.title}
    res = api_client.get(path=url, data=query_params)
    assert res.status_code == status.HTTP_200_OK
    assert res.data.get('count') > 0
    
    # Search by date

    # query_params = {"date": random_news_item.date}
    # res = api_client.get(path=url, data=query_params)
    # assert res.status_code == status.HTTP_200_OK
    # assert res.data.count() > 0
    
    
    # res_no_params = api_client.get(path=url)
    # for i in range(len(res_no_params.data.get('results'))):
    #     ...
    # res_no_params.data.get('results')[i].get('date')
    # assert res.status_code == status.HTTP_200_OK
    # assert res.data["full_name"] == payload["full_name"]
    # assert res.data["email"] == payload["email"]
