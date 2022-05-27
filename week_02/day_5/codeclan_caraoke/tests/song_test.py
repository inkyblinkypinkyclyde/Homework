import unittest

from classes.song import Song
# from classes.guest im`port Guest
# from classes.room import room`

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Dancing Queen")


    def test_song_has_name(self):
        self.assertEqual("Dancing Queen", self.song1.name)
