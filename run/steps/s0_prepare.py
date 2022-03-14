import os
import pathlib
import shutil

from tempfile import mkstemp
from shutil import move, copymode
import subprocess
from run.utils.utils import replace_in_file
from run.utils.logger import lprint, lsection
#*******************************************************************************
def s0_create_chess_project(root_path, project_name):
	project_path = os.path.join(root_path, "build", project_name)

	lprint("\n\nCreating brownie subprojects for " + project_name + " in " + project_path)

	# cleaning up the exchange path
	if os.path.exists(project_path):
		shutil.rmtree(project_path)
	os.makedirs(project_path)

    # filling the subproject folders
	subprojects = ["core"]
	for sp_name in subprojects:
		sp_path = os.path.join(project_path, sp_name)
		lprint("changing directory to " + sp_path)
		os.makedirs(sp_path)
		os.chdir(sp_path)

		subprocess.run(["brownie", "init"])
		
		brownie_subfolders = ["contracts", "interfaces"]
		for subfolder in brownie_subfolders:

			old_path = os.path.join(root_path, "src", "l1", sp_name, subfolder)
			new_path = os.path.join(sp_path, subfolder)
			shutil.rmtree(new_path)
			lprint("copying " + old_path + " to " + new_path)
			shutil.copytree(old_path, new_path)

		config_path = os.path.join(root_path, "src", "l1", sp_name, "brownie-config.yaml")
		if os.path.exists(config_path):
			shutil.copy(config_path, sp_path)
#*******************************************************************************
def s0_create_token_project(root_path):
	build_path = os.path.join(root_path, "build")
	lprint("\n\nCreating brownie subproject for ERC20 token")

	subprojects = ["erc20"]
	for sp_name in subprojects:
		sp_path = os.path.join(build_path, sp_name)
		if os.path.exists(sp_path):
			shutil.rmtree(sp_path)
		lprint("changing directory to " + sp_path)
		os.makedirs(sp_path)
		os.chdir(sp_path)

		subprocess.run(["brownie", "init"])
		
		brownie_subfolders = ["contracts", "interfaces"]
		for subfolder in brownie_subfolders:
			old_path = os.path.join(root_path, "src", "l1", sp_name, subfolder)
			new_path = os.path.join(sp_path, subfolder)
			shutil.rmtree(new_path)
			lprint("copying " + old_path + " to " + new_path)
			shutil.copytree(old_path, new_path)

		config_path = os.path.join(root_path, "src", "l1", sp_name, "brownie-config.yaml")
		if os.path.exists(config_path):
			shutil.copy(config_path, sp_path)