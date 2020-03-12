import sublime
import sublime_plugin

#########################################################################
# Place this file in the {user_appdata}/Sublime Text 3\Packages\User directory
#########################################################################
# modifyied the example on sublime text 3 website
# there were lots of fixes that needed to take place as the example did not function correctly 
# to setup key bindings it would look something like this
#########################################################################
# [
#    { "keys": ["ctrl+shift+/"],  "command": "slash_to_forward" },
#    { "keys": ["ctrl+shift+\\"], "command": "slash_to_back" },
#    { "keys": ["ctrl+shift+."],  "command": "to_first_slash_type" },
#    { "keys": ["ctrl+shift+,"],  "command": "to_last_slash_type" },
#    { "keys": ["ctrl+shift+m"],  "command": "to_majority_slash_type" },
# ]
#########################################################################
# To run commands from the sublime commandline
# >>> view.run_command('slash_to_back')
# >>> view.run_command('slash_to_forward')
#########################################################################
# also to note: use the command slash_to_forward exactly as is no matter how you type spell the actual class
# SlashToForwardCommand, slashToForwardCommand: Sublime does some funny business behind the scenes to PEP8'ify it
#########################################################################

def to_forward_slash(val):
    return val.replace('\\','/')
def to_back_slash(val):
    return val.replace('/','\\')


class slash_to_forwardCommand(sublime_plugin.TextCommand):
    '''All slashes in selection are replaced by forward slashes'''
    def run(self, editObj):
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                selection = self.view.substr(region)
                # Replace the selection with transformed text
                self.view.replace(editObj, region, to_forward_slash(selection))


class slash_to_backCommand(sublime_plugin.TextCommand):
    '''All slashes in selection are replaced by back slashes'''
    def run(self, editObj):
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                selection = self.view.substr(region)
                # Replace the selection with transformed text
                self.view.replace(editObj, region, to_back_slash(selection))


class to_first_slash_typeCommand(sublime_plugin.TextCommand):
    '''All slashes are replaced by first slash or backslash occurance in selection'''
    def run(self, editObj):
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                selection = self.view.substr(region)
                # which is first/last
                fs = selection.find('/')
                bs = selection.find('\\')
                if bs < fs:
                    selection = to_back_slash(selection)
                elif fs < bs:
                    selection = to_forward_slash(selection)
                # Replace the selection with transformed text
                if selection != self.view.substr(region):
                    self.view.replace(editObj, region, selection)


class to_last_slash_typeCommand(sublime_plugin.TextCommand):
    '''All slashes are replaced by last slash or backslash occurance in selection'''
    def run(self, editObj):
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                selection = self.view.substr(region)
                # which is first/last
                fs = selection.find('/')
                bs = selection.find('\\')
                if bs > fs:
                    selection = to_back_slash(selection)
                elif fs > bs:
                    selection = to_forward_slash(selection)
                # Replace the selection with transformed text
                # if selection != self.view.substr(region):
                self.view.replace(editObj, region, selection)


class to_majority_slash_typeCommand(sublime_plugin.TextCommand):
    '''All slashes are replaced by majority of slash or backslash found in selection'''
    def run(self, editObj):
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                selection = self.view.substr(region)
                # which is first/last
                fsp = selection.split('/')
                bsp = selection.split('\\')
                if bsp > fsp:
                    selection = to_back_slash(selection)
                elif fsp > bsp:
                    selection = to_forward_slash(selection)
                # Replace the selection with transformed text
                # if selection != self.view.substr(region):
                self.view.replace(editObj, region, selection)