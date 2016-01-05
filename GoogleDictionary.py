import sublime, sublime_plugin
import sys, os

sys.path.append(os.path.dirname(__file__))
from textblob import TextBlob

from StatusDisplay import StatusDisplaySingleton
from Setting import SettingSingleton
from TipDisplay import TipDisplay
from Timer import Timer, TimerTask
import mdpopups

'''
reference popups:
https://github.com/facelessuser/sublime-markdown-popups
'''

class LazyLookup:
    class LazyLookupTask(TimerTask):
        def __init__(self, view, text):
            self.view = view
            self.text = text
        def doJob(self):
            self.view.erase_status("Googledict")
            display = StatusDisplaySingleton.getInstance()
            display.set_status(self.view, "google in progress...", True)
            blob = TextBlob(self.text)
            try:
                lang = SettingSingleton.getInstance().get('lang')
                hello = blob.translate(to = lang)
                display.clear(self.view)
                TipDisplay.display(self.view, hello.__str__())
            except Exception as e:
                TipDisplay.display(self.view, "translate error!")
                display.clear(self.view)

    def __init__(self):
        self.timer = Timer(0.5)

    def lookup(self, view, text):
        task = LazyLookup.LazyLookupTask(view, text)
        self.timer.schedule(task)

class LookupSelectionListener(sublime_plugin.EventListener):
    prevText = ""
    lazyLookup = LazyLookup()
    def on_selection_modified_async(self, view):
        if not GoogledictmodeCommand.getEnabled():
            return
        selectionText = view.substr(view.sel()[0])
        if selectionText == None:
            return
        if len(selectionText) == 0:
            self.prevText = selectionText
            view.erase_status("Googledict")
            return
        if selectionText != self.prevText:
            self.prevText = selectionText
            self.lazyLookup.lookup(view, selectionText)

'''
test word: 'hello world, This is captain picard!'
'''
class GoogledictCommand(sublime_plugin.TextCommand):
    lazyLookup = LazyLookup()
    def run(self, edit):
        display = StatusDisplaySingleton.getInstance()
        selectionText = self.view.substr(self.view.sel()[0])
        self.lazyLookup.lookup(self.view, selectionText)

'''
test phrase: 'hello world, This is captain picard!'
'''
class GoogledictmodeCommand(sublime_plugin.TextCommand):
    enabled = False
    def run(self, edit):
        GoogledictmodeCommand.enabled = not GoogledictmodeCommand.enabled
        if GoogledictmodeCommand.enabled:
            sublime.message_dialog("Enter goole dictionary translate mode!")
            self.view.set_status("Googledictmode", "[TRANSLATE MODE]\n")
        else:
            self.view.erase_status("Googledict")
            self.view.erase_status("Googledictmode")

    @staticmethod
    def getEnabled():
        return GoogledictmodeCommand.enabled
