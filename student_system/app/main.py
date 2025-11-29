from student_system.data.database import Database


def main() -> None:
    db = Database()

    while True:
        print("STUDENT SYSTEM")
        print("1. Add student")
        print("2. List students")
        print("3. Search students")
        print("4. Exit")
        choice = input("Choose option: ").strip()

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            city = input("City: ")
            index_number = input("Index: ")
            avg = float(input("Average grade: "))

            db.add_student(
                name=name,
                age=age,
                city=city,
                index_number=index_number,
                average_grade=avg,
            )
            print("Student added.\n")

        elif choice == "2":
            for s in db.list_students():
                print(
                    f"{s.id[:8]} | {s.name} | {s.city} | {s.index_number} | {s.average_grade}"
                )
            print()

        elif choice == "3":
            q = input("Search text (name/city/index): ")
            results = db.search_students(q)
            for s in results:
                print(
                    f"{s.id[:8]} | {s.name} | {s.city} | {s.index_number} | {s.average_grade}"
                )
            print()

        elif choice == "4":
            break
        else:
            print("Unknown option.\n")


if __name__ == "__main__":
    main()
