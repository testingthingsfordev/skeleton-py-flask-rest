from unittest import TestCase

from api.application.ping_service import PingService
from api.infrastructure.ping_controller import PingController
from api.tests import database


class PingControllerTest(TestCase):

    def setUp(self):
        ping_service = PingService(database)
        self.ping_controller = PingController(ping_service)

    def test_it_should_return(self):
        result, status = self.ping_controller.get()

        self.assertEqual(result, {"data": "pong"})
        self.assertEqual(status, 200)
