import os
EXAMPLES_BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + "/examples/SQL/"
TEST_FILES_NAMES = os.listdir("examples/SQL")

TEST_FILES_DIRS = [EXAMPLES_BASE_DIR + w for w in TEST_FILES_NAMES]

