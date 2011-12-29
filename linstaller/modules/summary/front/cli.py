# -*- coding: utf-8 -*-
# linstaller summary module frontend - (C) 2011 Eugenio "g7" Paolantonio and the Semplice Team.
# All rights reserved. Work released under the GNU GPL license, version 3 or later.
#
# This is a module of linstaller, should not be executed as a standalone application.

import linstaller.frontends.cli as cli
import t9n.library
_ = t9n.library.translation_init("linstaller")

from linstaller.core.main import warn,info,verbose

class Frontend(cli.Frontend):
	def start(self):
		""" Start the frontend """
		
		self.header(_("Summary"))
				
		print(_("%(distroname)s will be installed in %(rootpartition)s.") % {"distroname":self.moduleclass.main_settings["distro"], "rootpartition":self.moduleclass.modules_settings["partdisks"]["root"]})
		print(_("%(swappartition)s will be used as swap.") % {"swappartition":self.moduleclass.modules_settings["partdisks"]["swap"]})
		print
		
		print(_("The default locale will be %(locale)s.") % {"locale":self.moduleclass.modules_settings["language"]["language"]})
		print(_("The default keyboard layout will be %(layout)s") % {"layout":self.moduleclass.modules_settings["language"]["keyboard"]})
		print
		
		print(_("The main user will be %(userfullname)s (%(username)s).") % {"userfullname":self.moduleclass.modules_settings["userhost"]["userfullname"], "username":self.moduleclass.modules_settings["userhost"]["username"]})
		if self.moduleclass.modules_settings["userhost"]["root"]:
			# Root enabled
			print(_("Root account is enabled."))
		print(_("The computer hostname will be %(hostname)s.") % {"hostname":self.moduleclass.modules_settings["userhost"]["hostname"]})
		print(_("The machine will use this timezone: %(timezone)s.") % {"timezone":self.moduleclass.modules_settings["timezone"]["timezone"]})
		print
		
		print(_("The bootloader (%(bootloader)s) will be installed in %(bootloaderpath)s.") % {"bootloader":self.moduleclass.modules_settings["bootloader"]["bootloader"],"bootloaderpath":self.moduleclass.modules_settings["bootloader"]["device"]})
		print
				
		# We should continue?
		res = self.question(_("Do you really want to continue?"), default=True)
		if not res: self.end()
		
		verbose("Beginning installation.")
		
		self.header(_("Installing..."))