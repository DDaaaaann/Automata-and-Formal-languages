class FA(object):
    states = {}

    def __init__(self, Q, Sigma, delta, s, F):
        self.alphabet = Sigma
        self.transition_table = delta
        self.start_state = s
        self.final_state = F

        for name in Q:
            start_state = (name == s)
            state = self.State(name, self.transition_table[name], start_state, (name in F))

            if start_state:
                self.current_state = state

            self.states[name] = state

    def move(self, input):
        try:
            self.current_state = self.states[self.current_state.transition_table[input]]
            return True
        except:
            return False


    class State(object):
        transition_table = dict()
        def __init__(self, name, transitions, start_state, final_state):
            self.name = name
            self.transition_table = transitions
            self.start_state = start_state
            self.final_state = final_state
