"""Write some more songs using this and make sure you understand that you're passing a list of strings as the lyrics.
Put the lyrics in a separate variable, then pass that variable to the class to use instead.
See if you can hack on this and make it do more things. Don't worry if you have no idea how, just give it a try, see what happens. Break it, trash it, thrash it, you can't hurt it."""


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])


the_wind=Song(["Come little leaves, said the wind one day",
           "Come over the meadows with me and play",
           "Put on your dresses of red and gold",
           "For summer is gone, and the days grow cold."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

the_wind.sing_me_a_song()

the_rabbit=["The moon is shining o'er the field" ,
            "A little breeze is blowing ",
            "The radish leaves are crisp and green" ,
            "The lettuces are growing."]
rabbit_song=Song(the_rabbit)
rabbit_song.sing_me_a_song()

