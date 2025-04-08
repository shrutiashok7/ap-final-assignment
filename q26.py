class Score:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks

class Student:
    def __init__(self, name, subjects, marks):
        self.name = name
        self.scores = []
        for i in range(len(subjects)):
            self.scores.append(Score(subjects[i], marks[i]))
    
    def __str__(self):
        result = f"Student {self.name} has the following scores:\n"
        for score in self.scores:
            result += f"{score.subject}: {score.marks}\n"
        return result.strip()
    
    def average(self):
        total = 0
        for score in self.scores:
            total += score.marks
        return total // len(self.scores)

def classAverage(students):
    subject_totals = {}
    subject_counts = {}
    
    for student in students:
        for score in student.scores:
            if score.subject in subject_totals:
                subject_totals[score.subject] += score.marks
                subject_counts[score.subject] += 1
            else:
                subject_totals[score.subject] = score.marks
                subject_counts[score.subject] = 1
    
    result = []
    for subject in sorted(subject_totals.keys()):
        avg = subject_totals[subject] // subject_counts[subject]
        result.append(f"{subject}:{avg}")
    
    return result

# Example usage
s1 = Student('X', ['C1', 'C2', 'C3', 'C4'], [10, 20, 30, 80])
s2 = Student('Y', ['C1', 'C2'], [40, 50])
s3 = Student('Z', ['C2', 'C3'], [60, 70])

print(s1)
print(s1.average())
print(classAverage([s1, s2, s3]))