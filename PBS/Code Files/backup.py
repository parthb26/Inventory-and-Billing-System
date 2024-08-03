import shutil
class BackUP:
    def __init__(self):
        source_path = ''
        destination_path = ''
    def bckup(self):
        source_path = "C:/Users/parth/OneDrive/Desktop/PBS/pbs.db"
        destination_path = "C:/Users/parth/OneDrive/Desktop/pbs_backup"
        shutil.copy2(source_path, destination_path)

        source_path = "C:/Users/parth/OneDrive/Desktop/PBS/user_credentials.db"
        destination_path = "C:/Users/parth/OneDrive/Desktop/pbs_backup"
        shutil.copy2(source_path, destination_path)
        
        source_path = "C:/Users/parth/OneDrive/Desktop/PBS/pbs.sqbpro"
        destination_path = "C:/Users/parth/OneDrive/Desktop/pbs_backup"
        shutil.copy2(source_path, destination_path)

        source_path = "C:/Users/parth/OneDrive/Desktop/PBS/user_credentials.sqbpro"
        destination_path = "C:/Users/parth/OneDrive/Desktop/pbs_backup"
        shutil.copy2(source_path, destination_path)
        
        quit(0)

if __name__ == "__main__":
    obj = BackUP()
    obj.bckup()