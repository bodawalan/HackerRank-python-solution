class FileOwners:

    @staticmethod

    def group_by_owners(files):
        list_value={}
        for k,v in files.items():
            if v not in list_value:
                list_value[v]=[k]
            else:
                list_value[v].append(k)

        print(list_value)



files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy',
}
print(FileOwners.group_by_owners(files))

