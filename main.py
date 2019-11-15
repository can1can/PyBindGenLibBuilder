import sys
sys.path.append("/path/to/build/lib/")
import test_lib
# test_lib
test_lib.printer()
a = test_lib.MyModuleDoAction()
print(a)