import sys
sys.path.append("/home/ivan/workspace/projects/python/lib_builder/build/lib.linux-x86_64-3.7/")
import test_lib
# test_lib
test_lib.printer()
a = test_lib.MyModuleDoAction()
print(a)