from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("touche1.wav")
play(song)