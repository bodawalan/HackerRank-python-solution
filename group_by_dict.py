class FileOwners:
    @staticmethod
    def group_by_owners(files):
        result={}
        for k,v in files.items():
            result[v] = result.get(v,[])+[k]
        return result





files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))