import pathlib
import sys

NB_ROOT = pathlib.Path(__file__).parent
PYNSTEIN_ROOT = pathlib.Path(__file__).parent.parent.parent.parent / 'utilities' / 'pystein'
GR2_ROOT = NB_ROOT.parent


def setup_nb():
	sys.path.append(PYNSTEIN_ROOT.as_posix())
	sys.path.append(GR2_ROOT.as_posix())
