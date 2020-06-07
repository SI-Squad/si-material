"""
As a software developer at Spotify, you've been asked to re-implement their playlist structure into a Linked List
structure. You've been told that along with displaying the current song in the playlist, listeners must also be able to
go back a song and skip to the next song.

You'll first need to create the playlist from a text file. The text file is in the format of Song Title, Artist.

This is the solution version for the Spotify Playlist.
Created by Emma Lubes, eml5244, for the Academic Success Center Supplemental Instruction Program.
"""
from dataclasses import dataclass
from typing import Any, Union


# TODO: Create the dataclass for you linked node structure.
# Hint: Keep in mind whether or not the structure should be able to change!
@dataclass(frozen=True)
class LinkedNode:
    value: Any
    next: Union["LinkedNode", None]


"""
Reads through the file to end up with a list of song dictionaries
e.g. [{"Sandstorm", Darude}, {"All Star", Smash Mouth}]
"""
def read_file(filename):
    all_songs = []
    with open(filename) as f:
        # TODO: Iterate through the file, put each song and artist into their own dictionary, and then append the
        # TODO: dictionary to the full list of songs
        for line in f:
            song_info = {}
            line = line.strip().split(", ")
            song = line[0]
            artist = line[1]
            song_info[song] = artist
            all_songs.append(song_info)
    return all_songs


def main():
    read_file("playlist.txt")


main()
