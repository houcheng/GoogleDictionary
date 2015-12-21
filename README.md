# Sublime Filefinder plugin

Introduction
------------

With google dictionary plugin, user can translate selected text into 
his lanauge by Google's translation service. First, user select
the word or phrase needed to translte. Then, he press the google dictionary
hot key, default is ctrl-b, and the translated text will be shown on
the sublime status bar, in the left bottom corner of sublime window.

This plug-in also provides translate mode, when enter this mode by hot key
ctrl-alt-b, every time when user select a phrase or word, the selected text
would be translated and display on status bar at left-bottom corner.


Usage
-----

- Set the "lang" in menu: /Preference/Packages/Google dictionary/Settings User.
- Restart sublime.
- Select a phrase or word, then click "ctrl+b" to translate
- Or use "ctrl+alt+b" to enter translate mode, then further select will be translated.


Setting
-------

#### Default Setting

```
{
    // trasnlate target language
    "lang" : "zh-TW",

    // display time of translated text.
    "status_display_period" : 10,
}
```

Supported lang include:

- Arabic – ar
- Bulgarian – bg
- Chinese (Simplified) – zh-CN
- Chinese (Traditional) – zh-TW (only available as a destination language)
- Croatian – hr
- Czech – cs
- Danish – da
- Dutch – nl
- English – en
- Finnish – fi
- French – fr
- German – de
- Greek – el
- Hebrew – iw
- Hindi – hi
- Italian – it
- Japanese – ja
- Korean – ko
- Norwegian – no
- Polish – pl
- Portuguese – pt
- Romanian – ro
- Russian – ru
- Spanish – es
- Swedish – sv

#### Default hot key

```
    { "command": "googledict", "keys": ["ctrl+b"] },
    { "command": "googledictmode", "keys": ["ctrl+alt+b"] }
```


Installation
------------

Via the [Sublime Package Manager](http://wbond.net/sublime_packages/package_control):

* `Ctrl+Shift+P` or `Cmd+Shift+P` in Linux / Windows / OS X
* Type `install`, select `Package Control: Install Package`
* Select `Google dictionary`
