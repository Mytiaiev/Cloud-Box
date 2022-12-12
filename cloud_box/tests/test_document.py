import pytest
from cloud_box.models import Document


# Check write data to DOcument model
@pytest.mark.django_db
@pytest.mark.parametrize('file_path, hash_size,', [('path_1', 'hash_size_1')])
def test_drivers_create(file_path, hash_size):
    document = Document.objects.create(file_path=file_path,
                                       hash_size=hash_size)
    assert file_path == file_path
    assert Document.objects.count() == 1
