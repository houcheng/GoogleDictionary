import sublime, sublime_plugin
import mdpopups

class TipDisplay:
    @staticmethod
    def display(view, msg):
        mdpopups.show_popup(view, msg,
            css="default.css", location=-1, max_width=600, max_height=350,
            flags=sublime.COOPERATE_WITH_AUTO_COMPLETE)
