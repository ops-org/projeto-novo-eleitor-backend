from django.test import TestCase
from politician.models import Politician, Party, Stats
from django.db.utils import ProgrammingError
from django.utils.timezone import datetime


class PartyTestCase(TestCase):
    def setUp(self):
        Party(abbreviation='PSB', name='PARTIDO SOCIALISTA BRASILEIRO').save()
        Party(abbreviation='PT', name='PARTIDO DOS TRABALHADORES').save()

    def test_get_id(self):
        p = Party.objects.filter(abbreviation='PT').get()
        self.assertEqual(p.name, "PARTIDO DOS TRABALHADORES")

    def test_avoid_noname(self):
        item = Party(abbreviation='PT')
        item.save()
        self.assertRaises(ProgrammingError, item.save())


class PoliticianTestCase(TestCase):
    def setUp(self):
        Party(abbreviation='PT', name='PARTIDO DOS TRABALHADORES').save()
        p = Party.objects.filter(abbreviation='PT').get()

        Politician(id_site=4400,
                   party=p,
                   name="JOAO NUNES",
                   name_full="JOAO NUNES SILVA",
                   sex='m',
                   birth_date=datetime(year=2018, month=1, day=1)
                   ).save()

    def test_politician_get_party_name(self):
        politician = Politician.objects.first()
        party = politician.party

        self.assertEqual(party.abbreviation, 'PT')
