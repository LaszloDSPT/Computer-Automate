#!/usr/bin/python
 # -*-coding:Latin-1 -*
import os 
import shutil

 # We count the number of images for each type of image
pic_1=os.popen("ls *.jpg | wc -l", "r").read()
pic_2=os.popen("ls *.png | wc -l","r").read()

# We count the number of music for each type of music
music_1=os.popen("ls *.mp3 | wc -l","r").read()
music_2=os.popen("ls *.aac | wc -l","r").read()

# We count the number of movies for each type of movie
movie_1=os.popen("ls *.avi | wc -l","r").read() 
movie_2=os.popen("ls *.wmv | wc -l","r").read()
movie_3=os.popen("ls *.mp4 | wc -l","r").read()
movie_4=os.popen("ls *.mov | wc -l","r").read()
movie_5=os.popen("ls *.mkv | wc -l","r").read()
#functions
def image_pic_1():
  if pic_1 >0 :
   if not os.path.exists('pictures'):
     os.mkdir('pictures')
     shutil.move("~/download/*.jpg", "~/pictures/*.jpg")
   elif os.path.exists('pictures'):
     shutil.move("~/download/*.jpg", "~/pictures/*.jpg")
def image_pic_2():
  if pic_2 >0 :
    if not os.path.exists('pictures'):
     os.mkdir('pictures')
     shutil.move("~/download/*.png", "~/pictures/*.png")
   elif os.path.exists('pictures'):
     shutil.move("~/download/*.png", "~/pictures/*.png")
def fmusic_1():
 if music_1 >0 :
  if not os.path.exists('music'):
   os.mkdir('music')
   shutil.move("~/download/*.mp3", "~/music/*.mp3")
  elif os.path.exits('music') :
   shutil.move("~/download/*.mp3", "~/music/*.mp3")
def fmusic_2():
  if music_2 >0 :
   if not os.path.exists('music'):
    os.mkdir('music')
    shutil.move("~/download/*.aac", "~/music/*.aac")
   elif os.path.exits('music') :
    shutil.move("~/download/*.aac", "~/music/*.aac")
def fmovie_1():
  if movie_1 >0 :
   if not os.path.exists('movie'):
    os.mkdir('movie')
    shutil.move("~/download/*.avi", "~/movie/*.avi")
   elif os.path.exits('music') :
    shutil.move("~/download/*.avi", "~/movie/*.avi)"
def fmovie_2():
 if movie_2 >0 :
   if not os.path.exists('movie'):
    os.mkdir('movie')
    shutil.move("~/download/*.wmv", "~/movie/*.wmv")
   elif os.path.exits('music') :
    shutil.move("~/download/*.wmv", "~/movie/*.wmv)"
def fmovie_3():
  if movie_3 >0 :
   if not os.path.exists('movie'):
    os.mkdir('movie')
    shutil.move("~/download/*.mp4", "~/movie/*.mp4")
   elif os.path.exits('music') :
    shutil.move("~/download/*.mp4", "~/movie/*.mp4)"
def fmovie_4():
   if movie_4 >0 :
    if not os.path.exists('movie'):
     os.mkdir('movie')
     shutil.move("~/download/*.mov", "~/movie/*.mov")
    elif os.path.exits('music') :
     shutil.move("~/download/*.mov", "~/movie/*.mov)"
def fmovie_5():
   if movie_5 >0 :
    if not os.path.exists('movie'):
      os.mkdir('movie')
      shutil.move("~/download/*.mkv", "~/movie/*.mkv")
    elif os.path.exits('music') :
      shutil.move("~/download/*.mkv", "~/movie/*.mkv)"
 #main
 #pic
image_pic_1();
image_pic_2();
#music
music_1();
music_2();
#movie
fmovie_1():
fmovie_2():
fmovie_3():
fmovie_4():
fmovie_5(:)
