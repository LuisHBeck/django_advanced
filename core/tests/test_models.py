import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    def setUp(self) -> None:
        self.file_name = f'{uuid.uuid4}.png'

    def test_get_file_path(self):
        archive = get_file_path(None, 'test.png')
        self.assertTrue(len(archive), len(self.file_name))


class ServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.service = mommy.make('Service')

    def test_str(self):
        self.assertEquals(str(self.service), self.service.name)


class JobPositionTestCase(TestCase):
    def setUp(self) -> None:
        self.position = mommy.make('JobPosition')

    def test_str(self):
        self.assertEquals(str(self.position), self.position.position)


class EmployeeTestCase(TestCase):
    def setUp(self) -> None:
        self.employee = mommy.make('Employee')

    def test_str(self):
        self.assertEquals(str(self.employee), self.employee.name)

    
class FeatureTestCase(TestCase):
    def setUp(self) -> None:
        self.feature = mommy.make('Feature')

    def test_str(self):
        self.assertEquals(str(self.feature), self.feature.name)