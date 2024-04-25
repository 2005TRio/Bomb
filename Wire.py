class Wires(PhaseThread):
    def __init__(self, component, target, name="Wires"):
        super().__init__(name, component, target)
        # Assuming component has attributes for each wire's state
        self.wires = {
            'blue': False,  # True if unplugged, False otherwise
            'purple': False,
            'black': False
        }

    def run(self):
        self._running = True
        while self._running:
            # Check each wire's state to see if unplugged
            self.wires['blue'] = self.component.blue_wire_unplugged()
            self.wires['purple'] = self.component.purple_wire_unplugged()
            self.wires['black'] = self.component.black_wire_unplugged()
            
            # Check if all required wires are unplugged
            if all(self.wires.values()):
                self._defused = True
                self._running = False  # Stop the thread when defused
            sleep(0.1)  # Check periodically

    def __str__(self):
        if self._defused:
            return "DEFUSED"
        else:
            # Return a string indicating which wires are still connected
            connected_wires = ', '.join([color for color, unplugged in self.wires.items() if not unplugged])
            return f"Connected: {connected_wires}"