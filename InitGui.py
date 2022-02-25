class WoodworkingWorkbench (Workbench):

	import os, sys
	import fakemodule
	path = os.path.dirname(fakemodule.__file__)
	iconPath = os.path.join(path, "Icons")

	MenuText = "Woodworking"
	ToolTip = "Workbech for woodworking."
	Icon = os.path.join(iconPath, "Woodworking.xpm")

	def Initialize(self):

		import FreeCADGui, PartGui, PartDesignGui, SketcherGui
		import DraftTools

		import loadTools
		self.appendToolbar("Macro tools", [ "BOM", "HTML", "CODE" ])
		
		import loadToolbar
		self.appendToolbar("Structure", loadToolbar.getItems("Structure"))
		self.appendToolbar("Furniture Parts", loadToolbar.getItems("Furniture Parts"))
		self.appendToolbar("Transformations", loadToolbar.getItems("Transformations"))
		self.appendToolbar("Operations", loadToolbar.getItems("Operations"))
		
	def Activated(self):
		# not needed now, maybe in the future
		return

	def Deactivated(self):
		# not needed now, maybe in the future
		return

	def ContextMenu(self, recipient):
		# not needed now, maybe in the future
		return

	def GetClassName(self): 
		return "Gui::PythonWorkbench"
       
Gui.addWorkbench(WoodworkingWorkbench())
