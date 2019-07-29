import sys
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)
for i in installed_packages_list:
    if('django' in i):
        print('Found at ' + str(installed_packages_list.index(i)))
        sys.exit(0)
print("Not Found")





