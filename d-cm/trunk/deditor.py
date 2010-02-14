#!/usr/bin/env python

#DEDITOR.py

import pygtk
pygtk.require('2.0')
import gtk
import os.path
from ftplib import FTP
import time
import gobject

class DEDITOR:
	def initialize(self):
		try:
			f = open("./Deditor/" + self.config, 'r')
		except:
			self.textbuffer.set_text('Configuration File(s) Missing!')
			self.cmdbuf.set_text('Initializing Failed!')
		loc = "location"
		start = "startlast"
		txt = "last-opened"
		host = "host"
		usr = "user"
		pswd = "password"
		dir = "directory"
		ftpfile = "ftpfilename"
		for line in f:
			if loc.strip() in line.strip().split(" ")[0]:
				self.location = line.strip().split(" ")[1]
				self.lastopened = self.location
		f.close()
		try:
			f = open(self.config, 'r')
		except:
			self.textbuffer.set_text('Configuration File(s) Missing!')
			self.cmdbuf.set_text('Initializing Failed!')
		for line in f:
			if host.strip() in line.strip().split(" ")[0]:
				self.host = line.strip().split(" ")[1]
		f.close()
		try:
			f = open(self.config, 'r')
		except:
			self.textbuffer.set_text('Configuration File(s) Missing!')
			self.cmdbuf.set_text('Initializing Failed!')
		for line in f:
			if usr.strip() in line.strip().split(" ")[0]:
				self.usr = line.strip().split(" ")[1]
		f.close()
		try:
			f = open(self.config, 'r')
		except:
			self.textbuffer.set_text('Configuration File(s) Missing!')
			self.cmdbuf.set_text('Initializing Failed!')
		for line in f:
			if pswd.strip() in line.strip().split(" ")[0]:
				self.pswd = line.strip().split(" ")[1]
		f.close()
		try:
			f = open(self.config, 'r')
		except:
			self.textbuffer.set_text('Configuration File(s) Missing!')
			self.cmdbuf.set_text('Initializing Failed!')
		for line in f:
			if dir.strip() in line.strip().split(" ")[0]:
				self.dir = line.strip().split(" ")[1]
		f.close()
		try:
			f = open(self.config, 'r')
		except:
			self.textbuffer.set_text('Configuration File(s) Missing!')
			self.cmdbuf.set_text('Initializing Failed!')
		for line in f:
			if ftpfile.strip() in line.strip().split(" ")[0]:
				self.ftpfile = line.strip().split(" ")[1]
		f.close()
		f = open(self.config, 'r')
		for line in f:
			if start.strip() in line.strip().split(" ")[0]:
				startt = line.strip().split(" ")[1]
				if startt == "YES":
					fz = open(self.config, 'r')
					for line in fz:
						if txt.strip() in line.strip().split(" ")[0]:
							found = line.strip().split(" ")[1]
							fl = open(found, 'r')
							text = ""
							for line in fl.readlines():
								text = text + line
								self.textbuffer.set_text(text)
							fl.close
							self.filepath = found
							lastopened = os.path.dirname(found)
							lastopnd = os.path.basename(found)
							self.opnd = 'Opened: ' + lastopnd
							self.cmdbuf.set_text(self.opnd)
							self.lastopened = lastopened
					fz.close()
				elif startt == "CHOSEN":
					chosen = "chosen-opened"
					fz = open(self.config, 'r')
					for line in fz:
						if chosen.strip() in line.strip().split(" ")[0]:
							found = line.strip().split(" ")[1]
							fl = open(found, 'r')
							text = ""
							for line in fl.readlines():
								text = text + line
								self.textbuffer.set_text(text)
							fl.close
							self.filepath = found
							lastopened = os.path.dirname(found)
							lastopnd = os.path.basename(found)
							self.opnd = 'Opened: ' + lastopnd
							self.cmdbuf.set_text(self.opnd)
							self.lastopened = lastopened
							self.lastopen(found)
					fz.close()
				else:
					help = self.location + '/help.txt'
					try:
						fl = open(help, 'r')
						text = ""
						for line in fl.readlines():
							text = text + line
							self.textbuffer.set_text(text)
						fl.close()
						self.lastopen("/home/darragh/Documenten/programs/help.txt")
					except:
						self.textbuffer.set_text("Help Files Missing, Check your Configuration File!")
						self.cmdbuf.set_text("HELP FILES MISSING")
		f.close

	def lastopen(self, new):
		t = open(self.config, 'r')
		text = "last-opened "
		for line in t:
			if text.strip() in line.strip().split(" ")[0]:
				last = line.strip().split(" ")[1]
		t.close()
		s = open(self.config, 'r').read()
		txt = ""
		s = s.replace(last, new)
		f = open(self.config, 'w')
		f.write(s)
		f.close()
		self.filepath = new
		self.lastopened = os.path.dirname(new)

	def new_file(self, w, date):
		self.textbuffer.set_text('')
		self.cmdbuf.set_text('Creating new file...')
		self.filepath = "None"

	def open_file(self, w, date):
		chooser = gtk.FileChooserDialog("Open File",None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
		chooser.set_default_response(gtk.RESPONSE_OK)
		chooser.set_current_folder(self.lastopened)
		filter = gtk.FileFilter()
		filter.set_name("Deditor")
		filter.add_pattern("*.ded")
		chooser.add_filter(filter)
		filter = gtk.FileFilter()
		filter.set_name("Scripts (.txt/.py)")
		filter.add_mime_type("Scripts/txt")
		filter.add_mime_type("Scripts/py")
		filter.add_pattern("*.txt")
		filter.add_pattern("*.py")
		chooser.add_filter(filter)
		filter = gtk.FileFilter()
		filter.set_name("SSA")
		filter.add_pattern("*.ssa")
		chooser.add_filter(filter)
		response = chooser.run()
		if response == gtk.RESPONSE_OK:
			self.textbuffer.set_text('')
			self.filepath = chooser.get_filename()
			self.opnd = 'Opened: ' + os.path.basename(self.filepath)
			self.cmdbuf.set_text(self.opnd)
			self.filename = os.path.basename(self.filepath)
			f = open(self.filepath, 'r')
			start = self.textbuffer.get_start_iter()
			end = self.textbuffer.get_end_iter()
			text = self.textbuffer.get_text(start,end)
			for line in f.readlines():
				text = text + line
				self.textbuffer.set_text(text)
			f.close()
			self.lastopen(chooser.get_filename())
		elif response == gtk.RESPONSE_CANCEL:
			print 'cancel'
		chooser.destroy()

	def save_file(self, w, date):
		if self.filepath == "None":
			self.cmdbuf.set_text("Use Save As Instead..")
		else:
			try:
				f = open(self.filepath, 'r+')
				text = ''
				start = self.textbuffer.get_start_iter()
				end = self.textbuffer.get_end_iter()
				txt = self.textbuffer.get_text(start,end)
				for line in txt:
					f.write(line)
				f.close()
				svd = 'Saved: ' + os.path.basename(self.filepath)
				self.cmdbuf.set_text(svd)
			except:
				self.cmdbuf.set_text("Deditor was not able to save your file..")

	def saveas_file(self, w, date):
		chooser = gtk.FileChooserDialog("Save File",None,gtk.FILE_CHOOSER_ACTION_SAVE,(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE,gtk.RESPONSE_OK))
		chooser.set_default_response(gtk.RESPONSE_OK)
		filter = gtk.FileFilter()
		filter.set_name("Scripts")
		filter.add_mime_type("Scripts/txt")
		filter.add_mime_type("Scripts/py")
		filter.add_pattern("*.txt")
		filter.add_pattern("*.py")
		chooser.add_filter(filter)
		filter = gtk.FileFilter()
		filter.set_name("SSA")
		filter.add_pattern("*.ssa")
		chooser.add_filter(filter)
		response = chooser.run()
		if response == gtk.RESPONSE_OK:
			self.filepath = chooser.get_filename()
			self.filename = os.path.basename(self.filepath)
			f = open(self.filepath, 'w+')
			text = ''
			start = self.textbuffer.get_start_iter()
			end = self.textbuffer.get_end_iter()
			txt = self.textbuffer.get_text(start,end)
			for line in txt:
				f.write(line)
			f.close()
			svd = 'Saved: ' + os.path.basename(self.filepath)
			self.cmdbuf.set_text(svd)
		elif response == gtk.RESPONSE_CANCEL:
			print 'cancel'
		chooser.destroy()

	def about(self, w, date):
		txt = "This app is made by Kruptein."
		self.textbuffer.set_text(txt)
		self.cmdbuf.set_text('About Deditor')

	def options(self, w, date):
		txt = ''
		f = open(self.config, 'r')
		for line in f.readlines():
			txt = txt + line
			self.textbuffer.set_text(txt)
		f.close()
		self.cmdbuf.set_text('Deditor Configuration File')
		self.filepath = self.config

	def help(self, w, date):
		help = self.location + '/help.txt'
		f = open(help, 'r')
		for line in f.readlines():
			txt = txt + line
			self.textbuffer.set_text(txt)
		f.close()
		self.cmdbuf.set_text('Deditor Help File')
		self.filepath = help

	def curfile(self, w, date):
		extension = self.opnd.strip().split(".")[1]
		if extension == "py":
			ext = "Python"
		elif extension == "ssa":
			ext = "SSA"
		elif extension == "txt":
			ext = "Text"
		elif extension == "ded":
			ext = "Deditor"
		else:
			ext = "Unknown"
		curfileinfo = "Type: " + ext
		size = os.path.getsize(self.filepath)
		curfileinfo = curfileinfo + "\nSize: " + str(size) + "bytes"
		lastmod = os.path.getmtime(self.filepath)
		curfileinfo = curfileinfo + "\nLast Modified: " + str(lastmod) + " seconds ago"
		lastacc = os.path.getatime(self.filepath)
		curfileinfo = curfileinfo + "\nLast Accesed: " + str(lastacc) + " seconds ago"
		self.textbuffer.set_text(curfileinfo)
		self.cmdbuf.set_text("Info")

	#def progress_timeout(self, pbobj):
	        # Calculate the value of the progress bar using the
       		# value range set in the adjustment object
       	#	new_val = self.pbar.get_fraction() + 0.01
       	#	if new_val > 1.0:
       	#		new_val = 0.0
		        # Set the new value
	#	        self.pbar.set_fraction(new_val)

	    	# As this is a timeout function, return TRUE so that it
		# continues to get called
	#	return True

	#def set_progress(self, percent):
	#	progrss = str(percent) + ' % progress'
	#	self.pbar.set_text(progrss)
	#	self.pbar.set_fraction(percent)
	   #     self.progress_timeout(self.pbar)
        	#return

	def ftp(self, w, date):
        	#self.win = gtk.Window(gtk.WINDOW_POPUP)
#	        self.win.set_resizable(True)
#	        self.win.set_title("ProgressBar")
#	        self.win.set_border_width(0)
#	        fvbox = gtk.VBox(False, 5)
#	        fvbox.set_border_width(10)
#	        self.win.add(fvbox)
#	        fvbox.show()
	        # Create a centering alignment object
   #     	align = gtk.Alignment(0.5, 0.5, 0, 0)
      #  	fvbox.pack_start(align, False, False, 5)
	 #       align.show()
        	# Create the ProgressBar
        #	self.pbar = gtk.ProgressBar()
        #	align.add(self.pbar)
        #	self.pbar.show()
        	# Add a timer callback to update the value of the progress bar
	   #     self.win.show()
		#self.progress_timeout
		ftp = FTP(self.host)
#		self.set_progress(0.1)
		ftp.login(self.usr,self.pswd)
#		self.set_progress(0.2)
		ftp.cwd(self.dir)
#		self.set_progress(0.3)
		retr = 'RETR ' + self.ftpfile
		ftpp = self.location + '/ftp.ded'
		ftp.retrbinary(retr, open(ftpp, 'w').write)
#		self.set_progress(0.4)
		ftp.quit()
#		self.set_progress(0.5)
		txt = ''
		f = open(ftpp, 'r')
 #		self.set_progress(0.6)
		for line in f.readlines():
			txt = txt + line
			self.textbuffer.set_text(txt)
		f.close()
#		self.set_progress(0.9)
		self.cmdbuf.set_text('Opened: ftp.ded')
#		self.set_progress(1.0)
#		self.win.destroy()
		self.opnd = 'ftp.ded'

	def quit(self, w, date):
		gtk.main_quit()

	def get_main_menu(self, window):
		accel_group = gtk.AccelGroup()
		item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", accel_group)
		item_factory.create_items(self.menu_items)
		window.add_accel_group(accel_group)
		self.item_factory = item_factory
		return item_factory.get_widget("<main>")

	def __init__(self):
		config = "/home/darragh/Documenten/programs/configuration.ded"
		self.config = config
		self.menu_items = (
			( "/File",            None,         None,             0, "<Branch>" ),
			( "/File/_New",       "<control><shift>N", self.new_file,    0, None ),
			( "/File/_Open",      "<control><shift>O", self.open_file,   0, None ),
			( "/File/_Save",      "<control><shift>S", self.save_file,   0, None ),
			( "/File/Save _As",   "<control><shift>A", self.saveas_file, 0, None ),
			( "/File/sep1",       None,         None,             0, "<Separator>" ),
			( "/File/_Quit",       "<control><shift>Q", self.quit,    0, None ),
			( "/Options",         None,         None,             0, "<Branch>" ),
			( "/Options/Current _File", "<control><shift>F", self.curfile, 0, None),
			( "/Options/FTP", None, self.ftp, 0, None),
			( "/Options/_Configuration", "<control><shift>C",         self.options,             0, None ),
			( "/Help",            None,         None,             0, "<Branch>" ),
			( "/Help/About",      None,         self.about,             0, None ),
			( "/Help/_Help", "<control><shift>H", self.help, 0, None),
			)
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_default_size(2000, 2000)
		window.set_title("DEDITOR")
		window.connect("destroy", lambda w: gtk.main_quit())	
		self.main_vbox = gtk.VBox(False, 1)
		self.main_vbox.set_border_width(1)
		window.add(self.main_vbox)
		self.main_vbox.show()
		menubar = self.get_main_menu(window)
		self.main_vbox.pack_start(menubar, False, True, 0)
		menubar.show()
		self.cmd = gtk.TextView()
		self.cmd.set_editable(False)
		self.cmdbuf = self.cmd.get_buffer()
		self.main_vbox.pack_start(self.cmd, False, True, 0)
		self.cmdbuf.set_text("Welcome")
		self.textview = gtk.TextView()
		self.textbuffer = self.textview.get_buffer()
		scrollwindow = gtk.ScrolledWindow(hadjustment=None, vadjustment=None)
		scrollwindow.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		scrollwindow.add_with_viewport(self.textview)
		self.main_vbox.pack_start(scrollwindow, True, True, 0)
		self.textview.show()
		window.show_all()
		self.initialize()

def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	DEDITOR()
	main()
