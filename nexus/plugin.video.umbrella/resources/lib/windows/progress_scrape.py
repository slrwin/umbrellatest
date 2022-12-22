# -*- coding: utf-8 -*-
"""
	Umbrella Add-on
"""

from json import dumps as jsdumps
from resources.lib.modules.control import dialog, getSourceHighlightColor, addonIcon, setting as getSetting
from resources.lib.windows.base import BaseDialog

class ProgressScrape(BaseDialog):
	def __init__(self, *args, **kwargs):
		BaseDialog.__init__(self, args)
		self.window_id = 2085
		self.closed = False
		self.meta = kwargs.get('meta')
		self.icon = addonIcon()
		self.set_controls()

	def run(self):
		self.doModal()
		self.clearProperties()


	def onAction(self, action):
		if action in self.closing_actions or action in self.selection_actions:
			self.doClose()

	def doClose(self):
		self.closed = True
		self.close()
		del self

	def iscanceled(self):
		return self.closed

	def set_controls(self):
		if self.meta.get('clearlogo'): self.setProperty('umbrella.clearlogo', self.meta.get('clearlogo'))
		if self.meta.get('fanart'): self.setProperty('umbrella.fanart', self.meta.get('fanart'))
		if self.meta.get('title'): self.setProperty('umbrella.title', self.meta.get('title'))
		if 'tvshowtitle' in self.meta: self.setProperty('umbrella.tvtitle', self.meta.get('tvshowtitle'))
		if self.meta.get('plot'): self.setProperty('umbrella.plot', self.meta.get('plot', ''))
		self.setProperty('umbrella.highlight.color', getSourceHighlightColor())
		self.setProperty('percent', str(0))
		if getSetting('sources.dialog.fanartBG') == 'true':
			self.setProperty('umbrella.fanartBG', '1')
		else:
			self.setProperty('umbrella.fanartBG', '0')

	def update(self, percent=0, content='', icon=None):
		try:
			self.setProperty('percent', str(percent))
			self.getControl(2001).setText(content)
			self.getControl(5000).setPercent(percent)
			if icon: self.getControl(200).setImage(icon)
		except: pass