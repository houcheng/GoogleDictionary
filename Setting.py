import sublime, sublime_plugin

'''
should load lazily or load on plugin reload. Got problem if directly load
on class initialization.
'''
class SettingSingleton:
    settings = None

    @staticmethod
    def getInstance():
        if SettingSingleton.settings == None:
            SettingSingleton.settings = sublime.load_settings('GoogleDictionary.sublime-settings')
        return SettingSingleton.settings
