from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("touche3.wav")
play(song)