import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
EXAMPLES_BASE_DIR = BASE_DIR + "/examples/SQL/"

TEST_FILES_NAMES = [
	'test.sql',
	'test1.sql',
]

TEST_FILES_DIRS = [EXAMPLES_BASE_DIR + w for w in TEST_FILES_NAMES]

