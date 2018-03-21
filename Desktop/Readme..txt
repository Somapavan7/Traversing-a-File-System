•Built a python script which traverses over the directory structure(contains 200 files each 500mb approx.). The script handles the soft-links and hard-links. As a result the script reports the duplicate files with same content.
•To deal directories with very large size I used Incremental hashing to improve the performance.
