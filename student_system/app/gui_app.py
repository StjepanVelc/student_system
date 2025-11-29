import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

from student_system.data.database import Database
from student_system.io.export_csv import export_students_to_csv


class StudentApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Student System")
        self.geometry("700x400")

        self.db = Database()

        self._build_widgets()
        self._refresh_list()

    def _build_widgets(self) -> None:
        form = ttk.Frame(self)
        form.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        ttk.Label(form, text="Name").grid(row=0, column=0)
        ttk.Label(form, text="Age").grid(row=0, column=1)
        ttk.Label(form, text="City").grid(row=0, column=2)
        ttk.Label(form, text="Index").grid(row=0, column=3)
        ttk.Label(form, text="Avg grade").grid(row=0, column=4)

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.city_var = tk.StringVar()
        self.index_var = tk.StringVar()
        self.avg_var = tk.StringVar()

        ttk.Entry(form, textvariable=self.name_var, width=15).grid(
            row=1, column=0, padx=2
        )
        ttk.Entry(form, textvariable=self.age_var, width=5).grid(
            row=1, column=1, padx=2
        )
        ttk.Entry(form, textvariable=self.city_var, width=10).grid(
            row=1, column=2, padx=2
        )
        ttk.Entry(form, textvariable=self.index_var, width=10).grid(
            row=1, column=3, padx=2
        )
        ttk.Entry(form, textvariable=self.avg_var, width=7).grid(
            row=1, column=4, padx=2
        )

        ttk.Button(form, text="Add", command=self._on_add).grid(row=1, column=5, padx=5)

        search_frame = ttk.Frame(self)
        search_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.search_var, width=25).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(search_frame, text="Go", command=self._on_search).pack(side=tk.LEFT)
        ttk.Button(search_frame, text="Reset", command=self._refresh_list).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(search_frame, text="Export CSV", command=self._on_export).pack(
            side=tk.RIGHT
        )

        self.tree = ttk.Treeview(
            self,
            columns=("name", "age", "city", "index", "avg"),
            show="headings",
        )
        self.tree.heading("name", text="Name")
        self.tree.heading("age", text="Age")
        self.tree.heading("city", text="City")
        self.tree.heading("index", text="Index")
        self.tree.heading("avg", text="Avg grade")

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def _on_add(self) -> None:
        try:
            age = int(self.age_var.get())
            avg = float(self.avg_var.get())
        except ValueError:
            messagebox.showerror("Error", "Age must be int, avg grade must be number.")
            return

        self.db.add_student(
            name=self.name_var.get(),
            age=age,
            city=self.city_var.get(),
            index_number=self.index_var.get(),
            average_grade=avg,
        )

        self.name_var.set("")
        self.age_var.set("")
        self.city_var.set("")
        self.index_var.set("")
        self.avg_var.set("")

        self._refresh_list()

    def _refresh_list(self) -> None:
        for row in self.tree.get_children():
            self.tree.delete(row)

        for s in self.db.list_students():
            self.tree.insert(
                "",
                tk.END,
                values=(s.name, s.age, s.city, s.index_number, s.average_grade),
            )

    def _on_search(self) -> None:
        q = self.search_var.get().strip()
        if not q:
            self._refresh_list()
            return

        results = self.db.search_students(q)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for s in results:
            self.tree.insert(
                "",
                tk.END,
                values=(s.name, s.age, s.city, s.index_number, s.average_grade),
            )

    def _on_export(self) -> None:
        export_path = Path("exports") / "students_gui_export.csv"
        export_students_to_csv(self.db.list_students(), export_path)
        messagebox.showinfo("Export", f"Exported to {export_path}")


def main() -> None:
    app = StudentApp()
    app.mainloop()


if __name__ == "__main__":
    main()
