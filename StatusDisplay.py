import sublime, sublime_plugin

from Timer import Timer, TimerTask

class StatusDisplay:
    class StatusDisplayTask(TimerTask):
        def __init__(self, view, msg, overwrite):
            self.view = view
            if overwrite:
                self.view.set_status("Googledict", msg+'\n')
            else:
                self.view.set_status("Googledict", msg)

        def doJob(self):
            self.view.erase_status("Googledict")

    def __init__(self, timeout):
        self.timer = Timer(timeout)

    def set_status(self, view, msg, overwrite):
        self.clear(view)
        task = StatusDisplay.StatusDisplayTask(view, msg, overwrite)
        self.timer.schedule(task)

    def clear(self, view):
        view.erase_status("Googledict")

'''
should load lazily or load on plugin reload. Got problem if directly load
on class initialization.
'''
class StatusDisplaySingleton:
    statusDisplay = None

    @staticmethod
    def getInstance(timeout):
        if StatusDisplaySingleton.statusDisplay == None:
            StatusDisplaySingleton.statusDisplay = StatusDisplay(timeout)
        return StatusDisplaySingleton.statusDisplay
