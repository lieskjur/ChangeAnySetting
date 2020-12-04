import sublime
import sublime_plugin

class ToggleAnySettingCommand(sublime_plugin.ApplicationCommand):
	def run(self, settings_base_name="Preferences.sublime-settings" , setting="dummy_setting"):
		self.settings = sublime.load_settings(settings_base_name)
		state = self.settings.get(setting)
		
		#print("previously:", self.settings.get(setting))

		if state == True:
			self.settings.set(setting,False)
		elif state == False:
			self.settings.set(setting,True)
		else:
			print("setting not present")

		sublime.save_settings(settings_base_name)

		#print("currently:", self.settings.get(setting))

# Test in console:
# window.run_command("toggle_any_setting", {"setting": "auto_complete"})