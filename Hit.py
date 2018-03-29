# Hit class stores intersection position and color
class Hit:

    # When Hit object initiated than position and color are given at this time
    def __init__(self, p_t, p_color):
        self.t = p_t
        self.color = tuple(p_color)