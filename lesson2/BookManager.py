import json
import os

class Book:
    def __init__(self,isbn,title,author,quantity):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.quantity=quantity

    def to_dict(self):
        return{
            "isbn":self.isbn,
            "title":self.title,
            "author":self.author,
            "quantity":self.quantity
        }
    
class BookManager:
    def __init__(self,filename="books.json"):
        self.filename=filename
        self.books=[]
        self.load_from_file()

    def add_book(self):
        try:
            isbn=input("请输入图书编号（ISBN）：")
            if any(b.isbn==isbn for b in self.books):
                raise Exception("错误：图书编号已经存在！")

        
            title=input("请输入书名：")
            author=input("请输入作者：")
            quantity=int(input("请输入数量："))

            new_book=Book(isbn,title,author,quantity)
            self.books.append(new_book)
            print("添加成功！")

        except ValueError:
            print("错误：数量必须是整数！")
        except Exception as e:
            print(e)
    

    def show_all_books(self):
        if not self.books:
            print("书库里空空如也。")
            return
        
        sorted_books=sorted(self.books,key=lambda x:x.title)
        print("\n-- 图书列表（按书名排序） --")
        for b in sorted_books:
            print(f"编号：{b.isbn} | 书名：{b.title} | 作者：{b.author} | 数量：{b.quantity}")

    
    def search_book(self):
        keyword=input("请输入要查询的ISBN或书名：")
        results=[b for b in self.books if keyword in b.isbn or keyword in b.title]

        if results:
            for b in results:
                print(f"找到：{b.title}(库存：{b.quantity})")
        else:
            print("未找到匹配图书。")

    def update_quantity(self):
        isbn=input("请输入图书数量：")
        for b in self.books:
            if b.isbn==isbn:
                try:
                    new_q=int(input(f"当前数量为：{b.quantiy},请输入新数量："))
                    b.quantity=new_q
                    print("修改成功！")
                    return
                except ValueError:
                    print("错误：输入格式无效！")
                    return
        print("未找到该编号的图书。")


    def delete_book(self):
        isbn=input("请输入要删除的图书编号：")
        initial_cnt=len(self.books)
        self.books=[b for b in self.books if b.isbn!=isbn]
        if len(self.books) <initial_cnt:
            print("删除成功！")
        else:
            print("未找到该图书。")


    def save_to_file(self):
        with open(self.filename,'w',encoding='utf-8') as f:
            json.dump([b.to_dict() for b in self.books],f,ensure_ascii=False,indent=4)
        print("数据已保存至文件。")

    def load_from_file(self):
            if os.path.exists(self.filename):
                try:
                    with open(self.filename,'r',encoding='utf-8') as f:
                        data=json.load(f)
                        self.books=[Book(**item) for item in data]
                    
                except Exception:
                    print("加载文件时出错，可能是文件损坏。")    

        
    def main():
            manager=BookManager()

            while True:
                print("\n====图书管理系统====")
                print("1.添加图书")
                print("2.查看所有图书")
                print("3.查询图书")
                print("4.修改图书数量")
                print("5.删除图书")
                print("6.保存并退出")

                choice=input("请选择操作（1到6）：")

                if choice=='1':
                    manager.add_book()
                elif choice=='2':
                    manager.show_all_books()
                elif choice=='3':
                    manager.update_quantity()
                elif choice=='4':
                    manager.delete_book()
                elif choice=='5':
                    manager.save_to_file()
                    print("谢谢使用，再见。")
                    break
                else:
                    print("无效选择，请重新输入。")


    if __name__=="__main__":
        main()


        