# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import os
import re

SETTINGS_FILE = "narrowing.sublime-settings"
extensions = None
regions = None
src_file = None
tmp_file = None

class NarrowCommand(sublime_plugin.TextCommand):
    window = None
    # param "action" = 'edit' / 'replace'
    def run(self, edit, action='edit'):
        global regions
        global src_file
        global tmp_file
        self.window = sublime.active_window()
        if action == 'edit':
            sel = self.view.sel()
            if not sel:return
            regions = []
            string_insert = ''
            src_file = self.view.file_name()
            name, ext = os.path.splitext(src_file)
            tmp_file = '%s%s%s' % (name, '__TEMP__', ext)
            ext = ext[1:]
            comment_char = extensions[ext.lower()]
            if not comment_char:comment_char = ["#",""]
            delimiter_line = "%s ===== DELIMITER LINE ===== %s\n" % (comment_char[0],comment_char[1])
            n = 0
            for region in sel:
                n += 1
                text = self.view.substr(region)
                regions.append([region.a, region.b])
                sdelim = delimiter_line if n > 1 else ''
                string_insert = '%s%s%s\n' % (string_insert, sdelim, text)
            with open(tmp_file, 'w') as f:
                f.write(string_insert)
            self.window.open_file(tmp_file)

        elif action == 'replace':
            sdelim = '===== DELIMITER LINE ====='
            # be sure, that TMP file is active
            view_tmp = self.window.find_open_file(tmp_file)
            self.window.focus_view(view_tmp)
            # read all text
            region = sublime.Region(0, self.view.size())
            text = self.view.substr(region)
            # if text has delimiter --> split to parts
            if sdelim in text:
                # replace delimiter line with one character and split by this
                patt = re.compile('\n(.+===== DELIMITER LINE =====.+)\n')
                text = re.sub(patt, chr(7), text)
                replace = re.findall('([^\a]+)', text)
            else:
                replace = [text]
            # close TMP file
            self.window.run_command("save")
            self.window.run_command("close")
            # activate the source buffer
            view_src = self.window.find_open_file(src_file)
            self.window.focus_view(view_src)
            selection = view_src.sel()
            selection.clear()
            # replace from end to start
            for i in range(len(replace)-1, -1, -1):
                region = sublime.Region(regions[i][0],regions[i][1])
                view_src.replace(edit, region, replace[i])
            # delete TMP file
            os.remove(tmp_file)
            regions = None
            src_file = None
            tmp_file = None


def plugin_loaded():
    global extensions
    settings = sublime.load_settings(SETTINGS_FILE)
    extensions = settings.get("extensions")