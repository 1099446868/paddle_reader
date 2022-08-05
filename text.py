import linecache


class LoadText(object):

    def read(self, path):
        fo = open(path, "r", encoding='utf-8')
        while True:
            text = fo.readline()
            if text:
                return text
            else:
                continue
        fo.close()

    def read2(self, path, line):
        return linecache.getline(path, line).strip()

    def write(self, path, content):
        fo = open(path, "w", encoding='utf-8')
        content = str(content)
        fo.write(content)
        fo.close()

    def getLineNum(self, path):
        fo = open(path, "r", encoding='utf-8')
        return len(fo.readlines())
