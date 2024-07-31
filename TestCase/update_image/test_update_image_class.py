import json
import pytest
import allure
from Models.pets import Pet


@pytest.mark.run(order=8)
class TestUploadImage:

    @allure.title(""""
      Scenario: Uploading an image to a pet record
      Given a logged-in user
      And a pet with a valid ID
      When the user uploads a valid image to the pet record with description of the image
      Then the image should be uploaded successfully
      And the pet will have the photo in the system""")
    def test_upload_image(self):
        pet = Pet()
        resp = pet.upload_pet_image(1667,
                                    'TestCase/update_image/panda.jpg',
                                    "This is a good pic")
        assert resp.status_code == 200

    @allure.title(""""
            Scenario: Uploading an image to a pet record with a non-existent user ID
            Given a non-existent user
            And a pet with a valid ID
            When the user uploads a valid image to the pet record with a description of the image
            Then the image upload should fail
            And an appropriate error message should be returned""")
    def test_upload_pet_image_non_existent_id(self):
        pet = Pet()
        with pytest.raises(ValueError, match="We can't upload a photo for the pet because ID does not exist"):
            pet.upload_pet_image(996669669, 'TestCase/update_image/panda.jpg', "This is a good pic")
