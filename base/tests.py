from django.test import TestCase
from .models import State


class StateTestCase(TestCase):
    def setUp(self):
        State(name="Paraíba", abbreviation="PB").save()
        State(name="Paraná", abbreviation="PR").save()
        State(name="Rio Grande do Norte", abbreviation="RN").save()

    def test_get_state(self):
        e = State.objects.filter(abbreviation="PB").get()
        self.assertEqual(str(e), "Paraíba")
