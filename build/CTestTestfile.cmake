# CMake generated Testfile for 
# Source directory: /c/Users/KIIT/OneDrive/Desktop/Assignment/orgChartApi/unit-test-generator
# Build directory: /c/Users/KIIT/OneDrive/Desktop/Assignment/orgChartApi/unit-test-generator/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(run_unit_tests "/c/Users/KIIT/OneDrive/Desktop/Assignment/orgChartApi/unit-test-generator/build/unit_tests.exe")
set_tests_properties(run_unit_tests PROPERTIES  _BACKTRACE_TRIPLES "/c/Users/KIIT/OneDrive/Desktop/Assignment/orgChartApi/unit-test-generator/CMakeLists.txt;28;add_test;/c/Users/KIIT/OneDrive/Desktop/Assignment/orgChartApi/unit-test-generator/CMakeLists.txt;0;")
subdirs("third_party/googletest")
