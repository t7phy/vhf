## New files sidis
When uploading a file, replace all the cpp files in original/cpp (also remove all other files per sub folder to avoid issues, but do not delte the folders). After replacing the files, ensure they have correct spacing (if not manually save each file with an auto formatter.) First run categorizing.py. Then run change_cpp_to_python.py (to avoid mistakes change the desired file paths per (sub)folder).

## Notes

- When running 'test_ordered_vs_original.py' we do not pass the tests for 'x<1e-6'