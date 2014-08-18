from django.test import TestCase
from .models import Artist
class TestArtists(TestCase):

	def setUp(self):
		self.artists = Artist.objects.create(first_name='david',last_name='boewe')

	def test_existe_vista(self):
		#print self.client.get('/artists/%d/'%self.artists.id)
		res = self.client.get('/artists/%d/'%self.artists.id)
		self.assertEqual(res.status_code,200)
		self.assertTrue('david' in res.content)

	def test_no_existe_vista(self):
		id_viejo = self.artists.id
		self.artists.delete()
		res = self.client.get('/artists/%d/'%id_viejo)
		self.assertEqual(res.status_code,404)
