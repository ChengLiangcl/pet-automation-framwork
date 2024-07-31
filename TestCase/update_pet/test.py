def validate_pet_data(pet_data):
    assert 'id' in pet_data, "id field is missing"
    assert isinstance(pet_data['id'], int), "id must be an integer"
    # Validate 'category' field
    category = pet_data.get('category')
    assert category is not None, "category field is missing"
    assert isinstance(category, dict), "category must be a dictionary"
    assert 'id' in category, "category id field is missing"
    assert isinstance(category['id'], int), "category id must be an integer"
    assert 'name' in category, "category name field is missing"
    assert isinstance(category['name'], str), "category name must be a string"

    # Validate 'name' field
    assert 'name' in pet_data, "name field is missing"
    assert isinstance(pet_data['name'], str), "name must be a string"

    # Validate 'photoUrls' field
    photo_urls = pet_data.get('photoUrls')
    assert photo_urls is not None, "photoUrls field is missing"
    assert isinstance(photo_urls, list), "photoUrls must be a list"
    for url in photo_urls:
        assert isinstance(url, str), "each photoUrl must be a string"

    # Validate 'tags' field
    tags = pet_data.get('tags')
    assert tags is not None, "tags field is missing"
    assert isinstance(tags, list), "tags must be a list"
    for tag in tags:
        assert isinstance(tag, dict), "each tag must be a dictionary"
        assert 'id' in tag, "tag id field is missing"
        assert isinstance(tag['id'], int), "tag id must be an integer"
        assert 'name' in tag, "tag name field is missing"
        assert isinstance(tag['name'], str), "tag name must be a string"

    # Validate 'status' field
    assert 'status' in pet_data, "status field is missing"
    assert isinstance(pet_data['status'], str), "status must be a string"
    assert pet_data['status'] in ['available', 'pending', 'sold'], "status must be available, pending, or sold"


validate_pet_data({
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "name": "Test_2",
    "photoUrls": [
        "http://example.com/photos/buddy.jpg"
    ],
    "tags": [
        {
            "id": 1,
            "name": "friendly"
        }
    ],
    "status": "available"
}
)
