from parse import parseSMD

with open('/Users/grigorygusev/smd-tool/smd-tool/test.smd', 'r') as f:
    smd = parseSMD(f)

with open('/Users/grigorygusev/smd-tool/smd-tool/my0.smd', 'a') as f:
    f.write(str(smd))