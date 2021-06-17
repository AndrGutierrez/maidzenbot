"""Memes for the bot commands"""
from classes.meme import Meme

memes = {}

thigs = Meme((232, 324), (463, 396), (-1000,-1000), './assets/thigs.jpg')
omg = Meme((1100, 700), (600, 600), (770,1010), './assets/omg.png')
supremacy = Meme((100, 80),  (100, 100), (250,90), './assets/supremacy.jpg')
fuckgirl = Meme((550, 450), (400, 400), (-1000,-1000), './assets/fuckgirl.jpg')
obstucalo = Meme((0, 162), (500, 350), (-1000,-1000), './assets/obstucalo.png')

bzoomer = Meme((0,0), (1,1), (100, 1120), './assets/boomervszoomer.jpg')
dogs = Meme((0,0), (1,1), (30, 30), './assets/dogs.jpg')
nordichad = Meme((0,0), (1,1), (60, 770), './assets/nordicchad.jpg')
virginvschads = Meme((0,0), (1,1), (40, 20), './assets/virginvschads.png')

memes={
    "simp": [thigs, fuckgirl, obstucalo, omg],
    "chadvsvirgin": [bzoomer, dogs, nordichad, virginvschads]
}
