from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("touche2.wav")
play(song)