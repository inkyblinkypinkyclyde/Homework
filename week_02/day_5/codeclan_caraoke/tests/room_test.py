import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.room1 = Room("Disco Room", 20)
        self.room2 = Room("Jazz Room", 5)
        self.room3 = Room("Cloak Room", 2)
        self.guest1 = Guest("Boris")
        self.guest2 = Guest("Carrie")
        self.guest3 = Guest("Dom")
        self.song1 = Song("Dancing Queen")
        self.song2 = Song("Flamenco Sketches")
        self.song3 = Song("Just The Two of Us")
    
    def test_room_has_name(self):
        self.assertEqual("Disco Room", self.room1.name)
    
    def test_room_is_empty(self):
        self.assertEqual(0, len(self.room1.occupants))
    
    def test_can_add_customer_to_room(self):
        self.room1.add_occupant(self.guest1)
        self.assertEqual(1, len(self.room1.occupants))
    
    def test_no_song_is_playing(self):
        self.assertEqual(0, len(self.room1.now_playing))

    def test_song_is_playing(self):
        self.room1.play_song(self.song1)
        self.assertEqual(1, len(self.room1.now_playing))

    def test_music_off(self):
        self.room1.play_song(self.song1)
        self.room1.stop_music()
        self.assertEqual(0, len(self.room1.now_playing))

    def test_check_room_for_guest_not_found(self):
        self.assertEqual(False, self.room1.check_room_for_guest(self.guest1))

    def test_check_room_for_guest_found(self):
        self.room1.add_occupant(self.guest1)
        self.assertEqual(True, self.room1.check_room_for_guest(self.guest1))