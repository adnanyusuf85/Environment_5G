from event_emitter import SimulatorCog

class RoadEnvironment(SimulatorWorker, TrafficSenseInterface):

    def __init__(self):
        self.initialize_environment()

    # SimulatorEnvironment Implementation
    def initialize(self):
        print("Initializing road environment...")
        self.reset()

    def step(self):
        print("Taking a step in the road environment\n")

    def reset(self):
        print("Resetting environment simulator\n")

    # ##########################

    # TrafficSenseInterface Implementation
    def get_trafficstate_segment(self):
        print("Sensing")
    # ##########################