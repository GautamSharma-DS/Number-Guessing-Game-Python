class SoundManager:
    def __init__(self):
        try:
            import winsound

            self._winsound = winsound
        except ImportError:
            self._winsound = None

    def _beep(self, frequency, duration):
        if self._winsound is not None:
            self._winsound.Beep(frequency, duration)

    def win(self):
        self._beep(900, 120)
        self._beep(1200, 160)

    def lose(self):
        self._beep(350, 250)

    def wrong(self):
        self._beep(500, 90)

    def error(self):
        self._beep(300, 80)
