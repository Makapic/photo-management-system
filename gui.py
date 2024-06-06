# import tkinter as tk
# from main import PhotoAlbum, Photo
#
# class PlaceholderEntry(tk.Entry):
#     def __init__(self, master=None, placeholder="", **kwargs):
#         super().__init__(master, **kwargs)
#         self.placeholder = placeholder
#         self.insert(0, self.placeholder)
#         self.bind("<FocusIn>", self._clear_placeholder)
#         self.bind("<FocusOut>", self._set_placeholder)
#
#     def _clear_placeholder(self, event):
#         if self.get() == self.placeholder:
#             self.delete(0, tk.END)
#
#     def _set_placeholder(self, event):
#         if not self.get():
#             self.insert(0, self.placeholder)
#
# # 创建一个 PhotoAlbum 实例
# photo_album = PhotoAlbum()
# photo_album.load_data()  # 在创建实例后加载数据
#
# # 定义 GUI 窗口
# root = tk.Tk()
# root.title("照片管理")
#
# # 定义功能函数
# def create_category():
#     category_name = category_entry.get()
#     photo_album.create_category(category_name)
#     photo_album.save_data()
#     category_entry.delete(0, tk.END)
#     update_category_list()
#
# def add_photo():
#     photo_path = photo_path_entry.get()
#     category = photo_category_entry.get()
#     caption = photo_caption_entry.get()
#     photo = Photo(photo_path, category, caption)
#     photo_album.add_photo(photo)
#     photo_album.save_data()
#     photo_path_entry.delete(0, tk.END)
#     photo_category_entry.delete(0, tk.END)
#     photo_caption_entry.delete(0, tk.END)
#     update_photo_list()
#
# def remove_photo():
#     category_name = photo_category_entry.get()
#     photo_path = photo_path_remove_entry.get()
#     photo_album.remove_photo(category_name, photo_path)
#     photo_album.save_data()
#     photo_path_remove_entry.delete(0, tk.END)
#     update_photo_list()
#
# def change_category():
#     old_category = old_category_entry.get()
#     new_category = new_category_entry.get()
#     photo_path = photo_path_entry.get()
#     photo_album.change_category(old_category, new_category, photo_path)
#     photo_album.save_data()
#     old_category_entry.delete(0, tk.END)
#     new_category_entry.delete(0, tk.END)
#     photo_path_entry.delete(0, tk.END)
#     update_photo_list()
#
# def list_photos():
#     category_name = category_list_entry.get()
#     photo_album.list_photos(category_name)
#
# def view_photo():
#     category_name = photo_category_entry.get()
#     photo_path = photo_path_entry.get()
#     photo_album.view_photo(category_name, photo_path)
#
# def update_category_list():
#     category_list.delete(0, tk.END)
#     for category in photo_album.categories:
#         category_list.insert(tk.END, category)
#
# def update_photo_list():
#     photo_list.delete(0, tk.END)
#     for category in photo_album.categories:
#         for photo in photo_album.categories[category]:
#             photo_list.insert(tk.END, f"{category}: {photo.path}")
#
# # 创建 GUI 元素
# category_label = tk.Label(root, text="创建照片类别:")
# category_entry = PlaceholderEntry(root, placeholder="输入类别名称")
#
# category_button = tk.Button(root, text="创建", command=create_category)
#
# photo_path_label = tk.Label(root, text="添加照片:")
# photo_path_entry = PlaceholderEntry(root, placeholder="输入照片路径")
# photo_category_entry = PlaceholderEntry(root, placeholder="输入类别名称")
# photo_caption_entry = PlaceholderEntry(root, placeholder="输入照片标题")
# photo_add_button = tk.Button(root, text="添加", command=add_photo)
#
# photo_remove_label = tk.Label(root, text="移除照片:")
# photo_path_remove_entry = PlaceholderEntry(root, placeholder="输入照片路径")
# photo_remove_button = tk.Button(root, text="移除", command=remove_photo)
#
# category_change_label = tk.Label(root, text="更改照片类别:")
# old_category_entry = PlaceholderEntry(root, placeholder="输入原类别名称")
# new_category_entry = PlaceholderEntry(root, placeholder="输入新类别名称")
# category_change_button = tk.Button(root, text="更改", command=change_category)
#
# list_photos_label = tk.Label(root, text="列出照片:")
# category_list_entry = PlaceholderEntry(root, placeholder="输入类别名称")
# list_photos_button = tk.Button(root, text="列出", command=list_photos)
#
# view_photo_label = tk.Label(root, text="查看照片:")
# view_photo_button = tk.Button(root, text="查看", command=view_photo)
#
# category_list = tk.Listbox(root, width=30)
# photo_list = tk.Listbox(root, width=60)
#
# # 布局 GUI 元素
# category_label.grid(row=0, column=0)
# category_entry.grid(row=0, column=1)
# category_button.grid(row=0, column=2)
#
# photo_path_label.grid(row=1, column=0)
# photo_path_entry.grid(row=1, column=1)
# photo_category_entry.grid(row=1, column=2)
# photo_caption_entry.grid(row=1, column=3)
# photo_add_button.grid(row=1, column=4)
#
# photo_remove_label.grid(row=2, column=0)
# photo_path_remove_entry.grid(row=2, column=1)
# photo_remove_button.grid(row=2, column=2)
#
# category_change_label.grid(row=3, column=0)
# old_category_entry.grid(row=3, column=1)
# new_category_entry.grid(row=3, column=2)
# category_change_button.grid(row=3, column=3)
#
# list_photos_label.grid(row=4, column=0)
# category_list_entry.grid(row=4, column=1)
# list_photos_button.grid(row=4, column=2)
#
# view_photo_label.grid(row=5, column=0)
# view_photo_button.grid(row=5, column=1)
#
# category_list.grid(row=6, column=0, rowspan=2)
# photo_list.grid(row=6, column=1, columnspan=4, rowspan=2)
#
# flag = 0
# if photo_album.categories:
#     update_category_list()
#     for category in photo_album.categories:
#         for photo in photo_album.categories[category]:
#             flag = 1
#     if flag == 1:
#         update_photo_list()
#
# root.mainloop()
import tkinter as tk
from tkinter import filedialog
from main import PhotoAlbum, Photo
import sys
from io import StringIO


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.insert(0, self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._set_placeholder)

    def _clear_placeholder(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)

    def _set_placeholder(self, event):
        if not self.get():
            self.insert(0, self.placeholder)


# 创建一个 PhotoAlbum 实例
photo_album = PhotoAlbum()
photo_album.load_data()  # 在创建实例后加载数据

# 定义 GUI 窗口
root = tk.Tk()
root.title("照片管理")
cur_catrgory = None
cur_path = ""

# 定义功能函数
def create_category():
    category_name = category_entry.get()
    photo_album.create_category(category_name)
    photo_album.save_data()
    category_entry.delete(0, tk.END)
    update_category_list()
    display_output("创建照片类别: " + category_name)


def remove_category():
    if category_list.curselection() == ():
        display_output("删除类别: 请选择目标类别！")
        return
    category_name = category_list.get(category_list.curselection())
    photo_album.remove_category(category_name)
    photo_album.save_data()
    update_category_list()
    display_output("删除照片类别: " + category_name)


def choose_path():
    global cur_path
    cur_path = filedialog.askopenfilename(filetypes=[("Photo files", "*")])
    if cur_path == "":
        return
    else:
        photo_choose_entry.delete(0, tk.END)
        photo_choose_entry.insert(0, cur_path)


def add_photo():
    global cur_path
    photo_path = cur_path
    if photo_path == '':
        display_output("添加照片: 请选择路径！")
        return
    if category_list.curselection() == ():
        display_output("添加照片: 请选择目标类别！")
        return
    category = category_list.get(category_list.curselection())  # category = photo_category_entry.get()
    caption = photo_caption_entry.get()
    if caption == "输入照片标题":
        display_output("添加照片: 请输入图片标题！")
        return
    photo = Photo(photo_path, category, caption)
    photo_album.add_photo(photo)
    photo_album.save_data()
    photo_choose_entry.delete(0, tk.END)
    photo_choose_entry.insert(0, "请选择文件")
    cur_path = ''
    photo_caption_entry.delete(0, tk.END)
    update_photo_list(category)
    display_output("添加照片: " + photo_path)


def remove_photo():
    global cur_catrgory
    if photo_list.curselection() == ():
        print("移除照片：请选择照片！")
        return
    photo_caption = photo_list.get(photo_list.curselection())
    photo_album.remove_photo(cur_catrgory, photo_caption)
    photo_album.save_data()
    update_photo_list(cur_catrgory)
    display_output("移除照片: " + photo_caption)


def change_category():
    global cur_catrgory
    if photo_list.curselection() == ():
        print("修改类别：请选择照片！")
        return
    photo_caption = photo_list.get(photo_list.curselection())
    old_category = cur_catrgory
    new_category = new_category_entry.get()
    photo_album.change_category(old_category, new_category, photo_caption)
    photo_album.save_data()
    new_category_entry.delete(0, tk.END)
    update_photo_list(old_category)
    display_output("更改照片类别: " + photo_caption)


def list_photos(event):
    global cur_catrgory
    if category_list.curselection() == ():
        display_output("列出照片: 请选择目标类别！")
        return
    category_name = category_list.get(category_list.curselection())
    cur_catrgory = category_name
    update_photo_list(category_name)
    display_output("列出类别 " + category_name + " 中的照片:")


def view_photo(event):
    global cur_catrgory
    photo_caption = photo_list.get(photo_list.curselection())
    photo_album.view_photo(cur_catrgory, photo_caption)
    display_output("查看照片: " + photo_caption)


def update_category_list():
    category_list.delete(0, tk.END)
    for category in photo_album.categories:
        category_list.insert(tk.END, category)


def update_photo_list(catagory):
    photo_list.delete(0, tk.END)
    for photo in photo_album.categories[catagory]:
        photo_list.insert(tk.END, photo.caption)


def display_output(text):
    output_text.insert(tk.END, text + "\n")


# 创建 GUI 元素
category_label = tk.Label(root, text="创建照片类别:")
category_entry = PlaceholderEntry(root, placeholder="输入类别名称")

category_button = tk.Button(root, text="创建", command=create_category)

remove_category_label = tk.Label(root, text="删除照片类别:")
remove_category_button = tk.Button(root, text="删除", command=remove_category)

photo_path_label = tk.Label(root, text="添加照片:")
photo_path_button = tk.Button(root, text="选择照片", command=choose_path)
photo_choose_entry = PlaceholderEntry(root, placeholder="未选择文件")
photo_caption_entry = PlaceholderEntry(root, placeholder="输入照片标题")
photo_add_button = tk.Button(root, text="添加", command=add_photo)

photo_remove_label = tk.Label(root, text="移除照片:")
photo_remove_button = tk.Button(root, text="移除", command=remove_photo)

category_change_label = tk.Label(root, text="更改照片类别:")
new_category_entry = PlaceholderEntry(root, placeholder="输入新类别名称")
category_change_button = tk.Button(root, text="更改", command=change_category)

# list_photos_label = tk.Label(root, text="列出照片:")
# category_list_entry = PlaceholderEntry(root, placeholder="输入类别名称")
# list_photos_button = tk.Button(root, text="列出", command=list_photos)

# view_photo_label = tk.Label(root, text="查看照片:")
# view_photo_button = tk.Button(root, text="查看", command=view_photo)

category_list = tk.Listbox(root, width=30)
photo_list = tk.Listbox(root, width=60)
category_list.bind('<Double-Button-1>', list_photos)
photo_list.bind('<Double-Button-1>', view_photo)

output_text = tk.Text(root, height=10, width=80)


# 重定向标准输出到输出文本框
class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)


sys.stdout = StdoutRedirector(output_text)

# 布局 GUI 元素
category_label.grid(row=0, column=0)
category_entry.grid(row=0, column=1)
category_button.grid(row=0, column=2)

remove_category_label.grid(row=1, column=0)
remove_category_button.grid(row=1, column=1)

photo_path_label.grid(row=2, column=0)
photo_path_button.grid(row=2, column=1)
photo_choose_entry.grid(row=2, column=2)
photo_caption_entry.grid(row=2, column=3)
photo_add_button.grid(row=2, column=4)

photo_remove_label.grid(row=3, column=0)
photo_remove_button.grid(row=3, column=1)

category_change_label.grid(row=4, column=0)
new_category_entry.grid(row=4, column=1)
category_change_button.grid(row=4, column=2)

# list_photos_label.grid(row=4, column=0)
# category_list_entry.grid(row=4, column=1)
# list_photos_button.grid(row=4, column=2)

# view_photo_label.grid(row=5, column=0)
# view_photo_button.grid(row=5, column=1)

category_list.grid(row=6, column=0, rowspan=2)
photo_list.grid(row=6, column=1, columnspan=4, rowspan=2)
output_text.grid(row=8, column=0, columnspan=5)

if photo_album.categories:
    update_category_list()
    # for category in photo_album.categories:
    #     for photo in photo_album.categories[category]:
    #         flag = 1
    # if flag == 1:
    #     update_photo_list()
root.mainloop()
