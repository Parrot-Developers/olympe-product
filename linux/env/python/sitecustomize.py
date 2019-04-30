import site
import sys
import os

# This adds the following workspace directory to sys.path:
# - out/final/usr/local/lib/pythonX.Y/site-packages
# - out/final/usr/lib/python

current_dir = os.path.dirname(__file__)
autotest_dir = os.path.abspath(os.environ.get(
    "GROUNDSDK_WORKSPACE_DIR", "{}/../../".format(site.PREFIXES[0])))
out_root_dir = (
    "{}/out/olympe-linux/final".format(autotest_dir))
prefix_local_dir = "{}/usr/local".format(out_root_dir)
prefix_dir = "{}/usr".format(out_root_dir)

site_dirs = (
    "{}/lib/python{}.{}/site-packages".format(
        prefix_local_dir, sys.version_info.major, sys.version_info.minor),
    "{}/lib/python/site-packages".format(prefix_local_dir),
    "{}/lib/python{}.{}/site-packages".format(
        prefix_dir, sys.version_info.major, sys.version_info.minor),
    "{}/lib/python/site-packages".format(prefix_dir),
)
python_dirs = (
    "{}/lib/python".format(prefix_local_dir),
    "{}/lib/python".format(prefix_dir),
)
first_site = next(
    (path for path in sys.path if path.endswith('site-packages')),
    None
)
if first_site:
    site_index = sys.path.index(first_site)
else:
    site_index = len(sys.path) - 1

for path in python_dirs + site_dirs:
    # insert to sys.path only if necessary
    if path not in sys.path:
        sys.path.insert(site_index, path)
