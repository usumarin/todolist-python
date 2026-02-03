import os
import datetime

# データの保存先ファイル名
FILE_NAME = "tasks.txt"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    tasks = []  # 1. 読み込んだタスクを入れるための「空のバケツ」を用意

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f.readlines():  # 2. 「for 変数 in リスト:」の形にする
            line = line.strip()
            if not line:  # 空行があればスキップする安全策
                continue

            parts = line.split(",")  # カンマで分ける

            # 3. 分けたデータを「名前」と「状態」に戻してリストにする
            task_name = parts[0]
            is_done = parts[1] == "True"

            # バケツに [名前, 状態] のセットを追加
            tasks.append([task_name, is_done])

    return tasks  # 最後に全部入ったバケツを返す


def save_tasks(tasks):
    """ファイルにタスクを保存する関数"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(f"{task[0]},{task[1]}\n")


def show_tasks(tasks):
    """現在のタスクを表示する関数"""
    print("\n--- 現在のタスク ---")
    if not tasks:
        print("タスクはありません。")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task[1] else "[ ]"
            print(f"{i}. {status} {task[0]}")
    print("------------------")


def main():
    tasks = load_tasks()  # 最初に読み込み

    while True:
        show_tasks(tasks)
        print("1. 追加  2. 削除  3. 完了にする  4. 終了")
        choice = input("操作を選んでください: ")

        if choice == "1":
            new_task = input("追加するタスクを入力: ")
            if new_task:
                tasks.append([new_task, False])
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
            if not tasks:
                print("削除するタスクがありません。")
                continue
            try:
                task_num = int(input("削除する番号を入力: "))
                tasks[task_num - 1][1] = True
                save_tasks(tasks)  # 変更のたびに保存
                print(f"「{tasks[task_num - 1][0]}」を完了にしました。")
            except (ValueError, IndexError):
                print("正しい番号を入力してください。")
            break
        elif choice == "4":
            print("プログラムを終了します。お疲れ様でした！")
            break
        else:
            print("1〜3の数字を選んでください。")


if __name__ == "__main__":
    main()
