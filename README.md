# Sublime Google Dictionary plugin

Introduction
------------

With google dictionary plugin, user can translate selected text into 
his lanauge by Google's translation service. First, user select
the word or phrase needed to translte. Then, he press the google dictionary
hot key and the translated text will be shown.

This plug-in also provides translate mode, when enter this mode by hot key every time when user select a phrase or word, the selected text
would be translated.


Installation and usage
----------------------

Install and configure this plugin:

- Install "google dictionary" by package control.
- Set the "lang" in menu: /Preference/Packages/Google dictionary/Settings User.
- Define hot-key for googledict and googledictmode command in menu: Preference/Key-Binding User
- Restart sublime.

To use the goodl dictionary:

- Select a phrase or word, then press hot-key to translate
- Or enter translate mode, then further select will be translated.


Setting
-------

#### Default Setting

```
{
    // trasnlate target language
    "lang" : "zh-TW",
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

#### Hot key setting

```
    { "command": "googledict", "keys": ["ctrl+t"] },
    { "command": "googledictmode", "keys": ["ctrl+alt+t"] }
```


Usage of package control
-------------------------

Via the [Sublime Package Manager](http://wbond.net/sublime_packages/package_control):

* `Ctrl+Shift+P` or `Cmd+Shift+P` in Linux / Windows / OS X
* Type `install`, select `Package Control: Install Package`
* Select `Google dictionary`
