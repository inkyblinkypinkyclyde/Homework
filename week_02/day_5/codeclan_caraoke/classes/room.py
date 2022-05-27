class Room:

    def __init__(self, name, max_occupancy):
        self.name = name
        self.max_occupancy = max_occupancy
        self.occupants = []
        self.now_playing = []
    
    def add_occupant(self, occupant):
        self.occupants.append(occupant)
    
    def play_song(self, play_song):
        self.now_playing.append(play_song)
    
    def stop_music(self):
        self.now_playing = []
    
    def check_room_for_guest(self, guest):
        for occupant in self.occupants:
            if occupant == guest:
                return True
        return False