set -e

cd /c/Users/KIIT/OneDrive/Desktop/Assignment/orgChartApi/unit-test-generator/build/third_party/googletest
/usr/bin/cmake.exe --regenerate-during-build -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
