import pytest
from src.api_client import ApiClient
from src.config import API_CONFIG


def test_list_all_authors_using_author(api_client):
    response = api_client.get("/author")
    assert response.status_code == 200
    assert "Ernest Dowson" in str(response.content)
    assert "Emily Dickinson" in str(response.content)

def test_list_all_authors_using_authors(api_client):
    response = api_client.get("/authors")
    assert response.status_code == 200
    assert "Ernest Dowson" in str(response.content)
    assert "Emily Dickinson" in str(response.content)

def test_search_by_author(api_client):
    response = api_client.get("/author/Dowson")
    assert response.status_code == 200
    assert "Love stays a summer night" in str(response.content)
    assert "And the Debate was done." not in str(response.content)
    assert "Bereavement in their death to feel" not in str(response.content)
    assert '"title":' in str(response.content)
    assert '"author":' in str(response.content)
    assert '"lines":' in str(response.content)
    assert '"linecount":' in str(response.content)

def test_search_by_author_return_output_fields_format_as_text(api_client):
    response = api_client.get("/author/Dowson/title,lines,author.text")
    assert response.status_code == 200
    assert "Love stays a summer night" in str(response.content)
    assert "And the Debate was done." not in str(response.content)
    assert "Bereavement in their death to feel" not in str(response.content)
    assert "title" in str(response.content)
    assert "author" in str(response.content)
    assert "lines" in str(response.content)
    assert "linecount" not in str(response.content)