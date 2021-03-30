#!/bin/env python3

import os
import typing
from pathlib import Path

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # NOQA


class Inhibitor(typing.Protocol):
    def toggle(self):
        ...


class CmdIngibitor:
    on_command = ""
    off_command = ""

    _is_active = False

    def __init__(self):
        self.off()

    def off(self):
        os.system(self.off_command)
        self._is_active = False

    def on(self):
        os.system(self.on_command)
        self._is_active = True

    def toggle(self):
        if self._is_active:
            self.off()
        else:
            self.on()

        print(self.__class__.__name__, " is ", self._is_active)


class DmpsInhibitor(CmdIngibitor):
    on_command = "xset -dpms"
    off_command = "xset +dpms"


class XorgInhibitor(CmdIngibitor):
    on_command = "xset s off"
    off_command = "xset s on"


class App:
    _is_active = False

    def __init__(self, *inhibitors: Inhibitor):
        self._inhibitors = inhibitors
        icon_root = Path(__file__).absolute().parent
        self._off_icon = str(icon_root / "coffee.svg")
        self._on_icon = str(icon_root / "coffee-hot.svg")

        self._icon = Gtk.StatusIcon()
        self._icon.set_from_file(self._off_icon)
        self._icon.connect("activate", self.on_left_click)

    def toggle_icon(self):
        if self._is_active:
            self._icon.set_from_file(self._off_icon)
        else:
            self._icon.set_from_file(self._on_icon)

        self._is_active = not self._is_active

    def on_left_click(self, _):
        for inh in self._inhibitors:
            inh.toggle()
        self.toggle_icon()

    def run(self):
        return Gtk.main()


def main():
    app = App(DmpsInhibitor(), XorgInhibitor())
    app.run()


if __name__ == "__main__":
    main()
