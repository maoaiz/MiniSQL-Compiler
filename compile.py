from src.SCM import SCMCompiler

def main(code_file_dir=None):
    if code_file_dir:
        print "Compiling: ", code_file_dir
        obj = SCMCompiler(src=code_file_dir)
        obj.compile()

def test():
    from src.test import TEST_FILES_NAMES, TEST_FILES_DIRS
    print "Choose a test file to compile:\n"
    for i,t in enumerate(TEST_FILES_NAMES, start=1):
        print "\t{}. {}".format(i, t)
    print ""
    test_file = raw_input("Your option [default 1]: ")
    option = test_file if test_file != "" else 1
    print option
    main(TEST_FILES_DIRS[int(option)-1])

if __name__ == '__main__':
    import sys, os
    if len(sys.argv) > 1:
        code_file_dir = sys.argv[1]
        if os.path.isabs(code_file_dir):
            print 'Argument List:', code_file_dir
            main(code_file_dir)
        else:
            print 'No es un archivo'
    else:
        print "Type --help to see the SCMCompiler help"
        test()