class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False
        self.current_memory = 0

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, app, app_memory):
        if app_memory > self.memory - self.current_memory:
            return f"Not enough memory to install {app}"
        elif app_memory > self.memory - self.current_memory or not self.is_on:
            return f"Turn on your phone to install {app}"
        self.apps.append(app)
        self.current_memory += app_memory
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory - self.current_memory}"
