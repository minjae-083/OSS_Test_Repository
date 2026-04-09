"""Todo 리스트 핵심 기능 모듈"""

from utils import get_today


class TodoManager:
    def __init__(self):
        self.todos = []

    def add(self, title):
        """할 일 추가"""
        todo = {
            "id": len(self.todos) + 1,
            "title": title,
            "done": False,
            "created": get_today(),
        }
        self.todos.append(todo)
        return todo

    def delete(self, todo_id):
        """할 일 삭제"""
        self.todos = [t for t in self.todos if t["id"] != todo_id]

    def list_all(self):
        """전체 할 일 조회"""
        return self.todos

    def complete(self, todo_id):
        """할 일 완료 처리"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["done"] = True
                return todo
        return None


if __name__ == "__main__":
    manager = TodoManager()
    manager.add("Git 보고서 작성")
    manager.add("Python 과제 제출")

    print("=== 할 일 목록 ===")
    for t in manager.list_all():
        status = "[완료]" if t["done"] else "[미완료]"
        print(f"  {t['id']}. {status} {t['title']} ({t['created']})")
