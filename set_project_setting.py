import sublime
import sublime_plugin

class SetProjectSettingCommand(sublime_plugin.WindowCommand):
	def run(self,setting,value):
		
		# Sets "value" to a "setting" in the current window's .sublime-project file

		variables = self.window.extract_variables()
		current_project_name = sublime.expand_variables("$project_name",variables)
		
		project_data = self.window.project_data()
		project_settings = project_data["settings"]

		#print("current project's name: ", current_project_name)
		#print("project settings previously:", project_settings)
		
		project_data["settings"].update({setting: value})
		self.window.set_project_data(project_data)

		#print("project data currently:", self.window.project_data())

# Test in console:
# window.run_command("set_project_setting", {"setting": "line_padding_bottom", "value": 4} )