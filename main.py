import os
from datetime import datetime
import webbrowser
import json
class Photo:
    def __init__(self, path, category, caption=None):
        self.path = path
        self.category = category
        self.caption = caption
        self.upload_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Photo: {self.path} | Category: {self.category} | Caption: {self.caption} | Uploaded: {self.upload_time}"

    def to_dict(self):
        """将 Photo 对象转换为字典,以便 JSON 序列化"""
        return {
            "path": self.path,
            "category": self.category,
            "caption": self.caption,
            "upload_time": self.upload_time
        }

    @classmethod
    def from_dict(cls, data):
        """从字典中创建 Photo 对象,用于 JSON 反序列化"""
        return cls(
            data["path"],
            data["category"],
            data["caption"]
        )
class PhotoAlbum:
    def __init__(self):
        self.categories = {}

    def load_data(self):
        """从JSON文件加载数据"""
        if os.path.exists("photo_album.json"):
            with open("photo_album.json", "r") as file:
                data = json.load(file)
                self.categories = {
                    category: [Photo.from_dict(photo_dict) for photo_dict in photos]
                    for category, photos in data.items()
                }

    def save_data(self):
        """将数据保存到JSON文件"""
        data = {
            category: [photo.to_dict() for photo in photos]
            for category, photos in self.categories.items()
        }
        with open("photo_album.json", "w") as file:
            json.dump(data, file, indent=4)

    def create_category(self, category_name):
        """创建自定义的照片类别"""
        if category_name == '':
            print("照片类别名不能为空")
        elif category_name not in self.categories:
            self.categories[category_name] = []
            print(f"成功创建照片类别: {category_name}")
        else:
            print(f"照片类别 {category_name} 已经存在.")

    def add_photo(self, photo):
        """将照片添加到指定类别"""
        category = photo.category
        if category in self.categories:
            self.categories[category].append(photo)
            print(f"照片 {photo.path} 已成功上传至类别 {category}")
        else:
            print(f"照片类别 {category} 不存在.")

    def remove_photo(self, category_name, photo_path):
        """从指定类别中移除照片"""
        if category_name in self.categories:
            photos = self.categories[category_name]
            for photo in photos:
                if photo.path == photo_path:
                    photos.remove(photo)
                    print(f"照片 {photo_path} 已从类别 {category_name} 中移除")
                    return
            print(f"类别 {category_name} 中不存在照片 {photo_path}")
        else:
            print(f"照片类别 {category_name} 不存在.")

    def change_category(self, old_category, new_category, photo_path):
        """将照片从一个类别移动到另一个类别"""
        if old_category in self.categories and new_category in self.categories:
            for photo in self.categories[old_category]:
                if photo.path == photo_path:
                    self.categories[old_category].remove(photo)
                    photo.category = new_category
                    self.categories[new_category].append(photo)
                    print(f"照片 {photo_path} 已从类别 {old_category} 移动到类别 {new_category}")
                    return
            print(f"类别 {old_category} 中不存在照片 {photo_path}")
        else:
            print(f"照片类别 {old_category} 或 {new_category} 不存在.")

    def list_photos(self, category_name=None):
        """列出指定类别或所有类别的照片"""
        if category_name:
            if category_name in self.categories:
                print(f"类别 {category_name} 中的照片:")
                for photo in self.categories[category_name]:
                    print(photo)
            else:
                print(f"照片类别 {category_name} 不存在.")
        else:
            print("所有照片:")
            for category, photos in self.categories.items():
                print(f"类别 {category}:")
                for photo in photos:
                    print(photo)

    def view_photo(self, category_name, photo_path):
        """使用默认图片查看器程序展示指定类别的照片"""
        if category_name in self.categories:
            photos = self.categories[category_name]
            for photo in photos:
                if photo.path == photo_path:
                    webbrowser.open(photo.path)
                    print(f"正在使用默认图片查看器程序打开照片: {photo.path}")
                    return
            print(f"类别 {category_name} 中不存在照片 {photo_path}")
        else:
            print(f"照片类别 {category_name} 不存在.")

# 交互式演示
photo_album = PhotoAlbum()

if __name__ == "__main__":
    while True:
        print("\n请选择操作:")
        print("1. 创建照片类别")
        print("2. 添加照片")
        print("3. 移除照片")
        print("4. 更改照片类别")
        print("5. 列出所有照片")
        print("6. 查看照片")
        print("7. 退出")

        photo_album.load_data()

        choice = input("输入数字选择操作: ")

        if choice == "1":
            category_name = input("输入新的照片类别名称: ")
            photo_album.create_category(category_name)
            photo_album.save_data()
        elif choice == "2":
            photo_path = input("输入照片路径: ")
            category = input("输入照片类别: ")
            caption = input("输入照片说明(可选): ")
            photo = Photo(photo_path, category, caption)
            photo_album.add_photo(photo)
            photo_album.save_data()
        elif choice == "3":
            category_name = input("输入照片所在类别: ")
            photo_path = input("输入要移除的照片路径: ")
            photo_album.remove_photo(category_name, photo_path)
            photo_album.save_data()
        elif choice == "4":
            old_category = input("输入照片原所在类别: ")
            new_category = input("输入照片要移动到的新类别: ")
            photo_path = input("输入要移动的照片路径: ")
            photo_album.change_category(old_category, new_category, photo_path)
            photo_album.save_data()
        elif choice == "5":
            category_name = input("输入要列出的类别(留空显示所有类别): ")
            photo_album.list_photos(category_name)
        elif choice == "6":
            category_name = input("输入照片所在类别: ")
            photo_path = input("输入要查看的照片路径: ")
            photo_album.view_photo(category_name, photo_path)
        elif choice == "7":
            photo_album.save_data()
            print("再见!")
            break
        else:
            print("无效的选择,请重试。")