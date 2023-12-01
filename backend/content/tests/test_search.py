import pytest
from django.urls import reverse
from rest_framework import status

from ..models import News

from .factories import NewsFactory


@pytest.mark.django_db
def test_search_title(api_client):
    news_list_page = list()
    titles = list()
    dates = list()
    for _ in range(10):
        item = NewsFactory()
        titles.append(item.title)
        dates.append(item.date)
        news_list_page.append(item)
    url = reverse('content:news')
    query_params = {
        "title": ""
    }
    res = api_client.get(path=url, data=query_params)
    res_no_params = api_client.get(path=url)
    for i in range(len(res_no_params.data.get('results'))):
        ...
    res_no_params.data.get('results')[i].get('date')
    assert res.status_code == status.HTTP_200_OK
    # assert res.data["full_name"] == payload["full_name"]
    # assert res.data["email"] == payload["email"]
