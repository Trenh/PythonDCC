import sys, os
import maya.cmds as cmds

cmds.loadPlugin( 'AbcExport.mll' )
cmds.loadPlugin( 'AbcImport.mll' )

in_file = sys.argv[3]
directory_out = sys.argv[4]
str_namespace = sys.argv[5]
cmds.file(new=True, force=True)
cmds.file(in_file, open=True)


exported_object = []

namespaces = str_namespace.split(' ')

for namespace in namespaces:
    cmds.ls(namespace)
    namespace = namespace.split(":")
    exported_object.append(namespace[0])

for abc_obj in exported_object:
    mycommand ="-frameRange 1 120 -uvWrite -dataFormat ogawa -root {0}:model -file {1}/{2}.abc".format(abc_obj, directory_out, abc_obj)
    cmds.AbcExport(j=mycommand)