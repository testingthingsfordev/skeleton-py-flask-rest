from unittest import TestCase

from api.application.ping_service import PingService
from api.tests import database


class PingServiceTest(TestCase):

    def setUp(self):
        self.ping_service = PingService(database)

    def test_it_should_return(self):
        result = self.ping_service.ping()

        self.assertEqual(result, {"data": "pong"})
