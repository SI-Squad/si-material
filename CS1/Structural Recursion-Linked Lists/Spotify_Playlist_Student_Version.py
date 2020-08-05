"""
As a software developer at Spotify, you've been asked to re-implement their playlist structure into a Linked List
structure. You've been told that along with displaying the current song in the playlist, listeners must also be able to
remove songs from their playlist and add songs anywhere in their playlist that they would like.

You'll first need to create the playlist from a text file. The text file is in the format of Song Title, Artist.

This is the solution version for the Spotify Playlist.
Created by Emma Lubes, eml5244, for the Academic Success Center Supplemental Instruction Program.
"""
# TODO: Import the correct imports for databases!
from time import sleep

# TODO: Uncomment this once the correct imports have been added!
"""
@dataclass()
class Song:
    name: str
    artist: str
"""

# TODO: Create the dataclass for you linked node structure.
# Hint: Keep in mind whether or not the structure should be able to change!



"""
Reads through the file to end up with a list of song dictionaries
e.g. [{"Sandstorm":Darude}, {"All Star":Smash Mouth}]
"""
def read_file(filename):
    all_songs = []
    with open(filename) as f:
        # TODO: Iterate through the file, put each song and artist into an instance of their dataclass, and then append
        # TODO: to the full list of songs
        print("Get rid of me once you've filled in the loop")
    return all_songs


"""
Takes the created list of Songs and puts them into the linked node structure playlist
"""
def convert_to_playlist(song_list):
    # TODO: Check to make sure the song list isn't empty and create the LinkedNode structure playlist
    # Hint: use recursion!
    print("Get rid of me once you've filled in the loop!")
    return 0


"""
Given the playlist and the name of song, removes that song from the playlist 
"""
def remove_song(playlist, name):
    # TODO: Check to make sure the playlist isn't empty
    print("Get rid of me once you've filled in the loop!")
    # TODO: Check if the song to be deleted is the current song in the playlist
    print("Get rid of me once you've filled in the loop!")
    # TODO: Move on to the next song in the playlist (Hint: recursion!)
    print("Get rid of me once you've filled in the loop!")
    return 0


"""
Plays the playlist! Prints the current song and artist and then sleeps for 2 seconds
"""
def play_playlist(playlist):
    # TODO: Loop through the playlist and play the songs! Don't forget to sleep!
    print("Get rid of me once you've filled in the loop!")
    return 0


"""
Adds a song to the playlist at a certain index
"""
def add_song(playlist, name, artist, index):
    # TODO: Check if the playlist is empty. If so, create the Song instance and add it to the structure there
    print("Get rid of me once you've filled in the loop")
    # TODO: Check if the playlist is at the correct index. If so, create the Song instance and add it to the structure
    print("Get rid of me once you've filled in the loop")
    # TODO: Move to the next song in the playlist
    print("Get rid of me once you've filled in the loop")
    return 0


def main():
    all_songs = read_file("playlist.txt")
    playlist = convert_to_playlist(all_songs)
    print(playlist)
    play_playlist(playlist)
    playlist = remove_song(playlist, '"Never Gonna Give You Up"')
    print(playlist)
    playlist = remove_song(playlist, '"Sandstorm"')
    print(playlist)
    playlist = add_song(playlist, '"Reflection"', "Mulan", 1)
    print(playlist)


main()
