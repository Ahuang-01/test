import os

class NoteManager:
    def __init__(self,notes_dir = "notes"):
        self.notes_dir = notes_dir
        if not os.path.exists(notes_dir):
            os.makedirs(notes_dir)
    
    def create_note(self,title,content):
        """创建新笔记"""
        filename = f"{self.notes_dir}/{title}.txt"
        with open(filename,'w',encoding='utf-8') as f:
            f.write(content)
        print(f"笔记'{title}'已创建")
    
    def list_notes(self):
        """列出所有笔记"""
        notes = [f for f in os.listdir(self.notes_dir) if f.endswith('.txt')]
        if not notes:
            print("没有找到笔记")
            return
        
        print("所有笔记:")
        for i,note in enumerate(notes,1):
            print(f"{i}.{note[:-4]}")
    
    