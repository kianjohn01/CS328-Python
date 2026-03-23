class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_report(self):
        avg = self.calculate_average()
        

        get_category = lambda score: (
            'A' if score >= 90 else
            'B' if score >= 80 else
            'C' if score >= 70 else
            'D' if score >= 60 else 'F'
        )
        
        category = get_category(avg)
        
        print(f"\n--- Student Report ---")
        print(f"Student Name: {self.name}")
        print(f"Grades:       {self.grades}")
        print(f"Average:      {avg:.2f}")
        print(f"Category:     {category}")


if __name__ == "__main__":
    student_name = input("Enter student name: ")
    raw_grades = input("Enter grades separated by space: ")
    student_grades = [int(g) for g in raw_grades.split()]

    student_obj = Student(student_name, student_grades)
    student_obj.display_report()
