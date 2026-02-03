import os

# データの保存先ファイル名
FILE_NAME = "tasks.txt"


def load_tasks():
    """ファイルからタスクを読み込む関数"""
    if not os.path.exists(FILE_NAME):
        return []  # ファイルがなければ空のリストを返す

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        # 改行を除いてリストに格納
        return [line.strip() for line in f.readlines()]


def save_tasks(tasks):
    """ファイルにタスクを保存する関数"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    """現在のタスクを表示する関数"""
    print("\n--- 現在のタスク ---")
    if not tasks:
        print("タスクはありません。")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("------------------")


def main():
    tasks = load_tasks()  # 最初に読み込み

    while True:
        show_tasks(tasks)
        print("1. 追加  2. 削除  3. 終了")
        choice = input("操作を選んでください: ")

        if choice == "1":
            new_task = input("追加するタスクを入力: ")
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)  # 変更のたびに保存
                print("追加しました！")

        elif choice == "2":
            if not tasks:
                print("削除するタスクがありません。")
                continue
            try:
                task_num = int(input("削除する番号を入力: "))
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)  # 変更のたびに保存
                print(f"「{removed}」を削除しました。")
            except (ValueError, IndexError):
                print("正しい番号を入力してください。")

        elif choice == "3":
            print("プログラムを終了します。お疲れ様でした！")
            break
        else:
            print("1〜3の数字を選んでください。")


if __name__ == "__main__":
    main()
