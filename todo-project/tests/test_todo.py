"""TodoManager 테스트 모듈"""

import sys
sys.path.append("../src")

from todo import TodoManager


def test_add():
    manager = TodoManager()
    todo = manager.add("테스트 할 일")
    assert todo["title"] == "테스트 할 일"
    assert todo["done"] is False
    print("[PASS] test_add")


def test_delete():
    manager = TodoManager()
    manager.add("삭제할 항목")
    manager.delete(1)
    assert len(manager.list_all()) == 0
    print("[PASS] test_delete")


def test_complete():
    manager = TodoManager()
    manager.add("완료할 항목")
    result = manager.complete(1)
    assert result["done"] is True
    print("[PASS] test_complete")


if __name__ == "__main__":
    test_add()
    test_delete()
    test_complete()
    print("\n모든 테스트 통과!")
