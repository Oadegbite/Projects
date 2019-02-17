class agent:

    def __init__(self, name,env, debug=False):
        self.debug = debug
        self.name = name
        self.totalReward = 0
        self.env = env
        self.totalReward = 0
        print("agent init {}".format(self.name)) if (self.debug) else None

    def action(self, step):
        print("Action @ t = {} method for {}".format(step,self.name)) if (self.debug) else None
        return self.env.action_space.sample()
