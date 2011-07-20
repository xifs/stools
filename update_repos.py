#!/usr/bin/python2
#encoding=utf8

import os,time,subprocess

__author__ = 'lizaifang@gmail.com'
__version__ = 0.1

class UpdateRepo:

	repo_path = '/data/repo'
	cmd = {
		'git':['git','pull'],
		'git_svn':['git','svn','rebase'],
		'svn':['svn','up'],
		'hg':['hg','pull','-u'],
	}

	def identify_repo(self, dir):
		is_svn = os.path.join(dir, '.svn')
		is_git_svn = os.path.join(dir, '.git', 'svn')
		is_git = os.path.join(dir, '.git', 'config')
		is_hg = os.path.join(dir, '.hg')
		if os.path.exists(is_git_svn):
			return 'git_svn'
		elif os.path.exists(is_git):
			return 'git'
		elif os.path.exists(is_svn):
			return 'svn'
		elif os.path.exists(is_hg):
			return 'hg'
		else:
			return False
		#[svn-remote "svn"]

	def update_repo(self, dir, type):
		print '>Entering', dir
		os.chdir(dir)
		try:
			output = subprocess.check_output(self.cmd[type])
			return output
		except subprocess.CalledProcessError, e:
			return '>',e
		os.chdir(repo_path)
		print '>Leaving', dir

	def gc_repo(self, dir):
		print '>Entering', dir
		os.chdir(dir)
		try:
			output = subprocess.check_output(['git','gc'])
			return output
		except subprocess.CalledProcessError, e:
			return '>',e
		os.chdir(repo_path)
		print '>Leaving', dir

	def update_gc(self, repo_path=None):
		if repo_path is None:
			dir = os.listdir(self.repo_path)
		else:
			dir = os.listdir(repo_path)
		for item in dir:
			print dir.index(item),'/',len(dir)
			path = os.path.join(self.repo_path, item)
			if os.path.isdir(path):
				type = self.identify_repo(path)
				if type == 'git' or type == 'git_svn':
					print 'Detected : ' + type
					print self.gc_repo(path)
				else:
					print item, 'is not git repo'
			else:
				print item, 'is not dir'

	def update_all(self, repo_path=None):
		if repo_path is None:
			dir = os.listdir(self.repo_path)
		else:
			dir = os.listdir(repo_path)
		for item in dir:
			print dir.index(item),'/',len(dir)
			path = os.path.join(self.repo_path, item)
			if os.path.isdir(path):
				type = self.identify_repo(path)
				if type is not False:
					print 'Detected : ' + type
					print self.update_repo(path, type)
				else:
					print item, 'is not repo'
			else:
				print item, 'is not dir'

if __name__ == '__main__':
	git = UpdateRepo()
	print git.update_all('/data/repo')
	#print git.update_gc('/data/repo')

