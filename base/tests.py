from django.test import TestCase
from .models import Estado

class EstadoTestCase(TestCase):
    def setUp(self):
        Estado(state="Paraíba", abbreviation="PB").save()
        Estado(state="Rio Grande do Norte", abbreviation="RN").save()
        Estado(state="Paraná", abbreviation="PR").save()

    def test_get_estado(self):
        e = Estado.objects.filter(abbreviation="PB").get()
        self.assertEqual(str(e), "Paraíba")
