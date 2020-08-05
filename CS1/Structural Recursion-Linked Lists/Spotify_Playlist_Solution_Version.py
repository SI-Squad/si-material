"""
As a software developer at Spotify, you've been asked to re-implement their playlist structure into a Linked List
structure. You've been told that along with displaying the current song in the playlist, listeners must also be able to
remove songs from their playlist and add songs anywhere in their playlist that they would like.

You'll first need to create the playlist from a text file. The text file is in the format of Song Title, Artist.

This is the solution version for the Spotify Playlist.
Created by Emma Lubes, eml5244, for the Academic Success Center Supplemental Instruction Program.
"""
# TODO: Import the correct imports for databases!
from dataclasses import dataclass
from typing import Any, Union
from time import sleep


@dataclass()
class Song:
    name: str
    artist: str


# TODO: Create the dataclass for you linked node structure.
# Hint: Keep in mind whether or not the structure should be able to change!
@dataclass(frozen=True)
class LinkedNode:
    value: Any
    next: Union["LinkedNode", None]


"""
Reads through the file to end up with a list of song dictionaries
e.g. [{"Sandstorm":Darude}, {"All Star":Smash Mouth}]
"""
def read_file(filename):
    all_songs = []
    with open(filename) as f:
        # TODO: Iterate through the file, put each song and artist into an instance of their dataclass, and then append
        # TODO: to the full list of songs
        for line in f:
            line = line.strip().split(", ")
            song = Song(line[0], line[1])
            all_songs.append(song)
    return all_songs


"""
Takes the created list of Songs and puts them into the linked node structure playlist
"""
def convert_to_playlist(song_list):
    # TODO: Check to make sure the song list isn't empty and create the LinkedNode structure playlist
    # Hint: use recursion!
    if len(song_list) is 0:
        return None
    else:
        return LinkedNode(song_list[0], convert_to_playlist(song_list[1:]))


"""
Given the playlist and the name of song, removes that song from the playlist 
"""
def remove_song(playlist, name):
    # TODO: Check to make sure the playlist isn't empty
    if playlist is None:
        return IndexError("There are no songs in the playlist to delete!")
    # TODO: Check if the song to be deleted is the current song in the playlist
    elif name in playlist.value.name:
        return playlist.next
    # TODO: Move on to the next song in the playlist (Hint: recursion!)
    else:
        return LinkedNode(playlist.value, remove_song(playlist.next, name))


"""
Plays the playlist! Prints the current song and artist and then sleeps for 2 seconds
"""
def play_playlist(playlist):
    # TODO: Loop through the playlist and play the songs! Don't forget to sleep!
    while playlist is not None:
        song_info = playlist.value
        print("Now Playing ", song_info.name, " by ", song_info.artist)
        playlist = playlist.next
        sleep(2)


"""
Adds a song to the playlist at a certain index
"""
def add_song(playlist, name, artist, index):
    # TODO: Check if the playlist is empty. If so, create the Song instance and add it to the structure there
    if playlist is None:
        song_info = Song(name, artist)
        return LinkedNode(song_info, None)
    # TODO: Check if the playlist is at the correct index. If so, create the Song instance and add it to the structure
    elif index == 0:
        song_info = Song(name, artist)
        return LinkedNode(song_info, playlist)
    # TODO: Move to the next song in the playlist
    else:
        return LinkedNode(playlist.value, add_song(playlist.next, name, artist, index-1))


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
