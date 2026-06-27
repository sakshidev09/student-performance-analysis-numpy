import numpy as np

data = np.genfromtxt(
    "StudentsPerformance.csv",
    delimiter=",",
    skip_header=1,
    usecols=(5,6,7)
)
print("shape:",data.shape)
print("size:",data.size)
print("dimension:",data.ndim)
print("data type:",data.dtype)

#indexing and slicing
print("first row:",data[0]) #marks of first student
print("last row:",data[-1]) #marks of last student
print("marks of first 5 students:",data[0:5]) #marks of first 5 students
print("maths scores:",data[:10,0]) #maths scores of first 10 students
print("reading scores of 10 students:",data[:10,1]) #reading scores of first 10 students

#boolean masking
writing_scores = data[:, 2]

print("writing scores > 90:",writing_scores[writing_scores > 90])

reading_scores = data[:, 1]
print("reading scores < 40:",reading_scores[reading_scores < 40])

maths_scores = data[:, 0]
print("maths scores of students with reading score > 90:",maths_scores[reading_scores > 90])

#using statistical functions
#average()

subject_avg = np.mean(data, axis=0)
print("overall average:",np.mean(data))
print("Math Average:", subject_avg[0])
print("Reading Average:", subject_avg[1])
print("Writing Average:", subject_avg[2])

#max()
subject_max = np.max(data, axis=0)
print("maths max:",subject_max[0])
print("reading max:",subject_max[1])
print("writing max:",subject_max[2])

#min()
subject_min = np.min(data, axis=0)
print("maths min:",subject_min[0])
print("reading min:",subject_min[1])
print("writing min:",subject_min[2])

#std()
subject_std = np.std(data, axis=0)
print("maths std:",subject_std[0])
print("reading std:",subject_std[1])
print("writing std:",subject_std[2])

#variance()
subject_var = np.var(data, axis=0)
print("maths variance:",subject_var[0]) 
print("reading variance:",subject_var[1])
print("writing variance:",subject_var[2])

#best subject
subjects = np.array(["Math", "Reading", "Writing"])
best_subject_index = np.argmax(subject_avg)
best_subject = subjects[best_subject_index]

print("Best Performing Subject:", best_subject)

#worst subject
subjects = np.array(["Math", "Reading", "Writing"])
worst_subject_index = np.argmin(subject_avg)
worst_subject = subjects[worst_subject_index]

print("worst Performing Subject:", worst_subject)

#student analytICS
student_avg = np.mean(data,axis=1)

#top student
top_student_index = np.argmax(student_avg)
print("print top student index:",top_student_index)

top_student_scores = data[top_student_index]
print("Math:", top_student_scores[0])
print("Reading:", top_student_scores[1])
print("Writing:", top_student_scores[2])
print("avg of top students score:",np.mean(top_student_scores))

#lowest performing student
lowest_student_index = np.argmin(student_avg)
print("print lowest performing student index:",lowest_student_index)

lowest_student_scores = data[lowest_student_index]
print("Math:", lowest_student_scores[0])
print("Reading:", lowest_student_scores[1])
print("Writing:", lowest_student_scores[2])
print("avg of lowest students score:",np.mean(lowest_student_scores))

#students above class average

class_avg = np.mean(data)

students_above_avg = np.sum(student_avg > class_avg)

print("Class Average:", class_avg)
print("Students Above Class Average:", students_above_avg)

#students below class average

students_below_avg= np.sum(student_avg < class_avg)
print("students below class average:",students_below_avg)

#excellent students
excellent_students = student_avg > 90
excellent_count = np.sum(excellent_students)

print("Students with average above 90:", excellent_count)

#failing students
failed_students = np.any(data < 40, axis=1)
failed_count = np.sum(failed_students)


#pass percentage
total_students = data.shape[0]

passed_students = total_students - failed_count

pass_percentage = (passed_students / total_students) * 100

print("Total Students:", total_students)
print("Passed Students:", passed_students)
print("Failed Students:", failed_count)
print("Pass Percentage:", round(pass_percentage, 2), "%")

#vectorization
#np.where()


performance = np.where(student_avg >= 75,"good","needs improvement")
print(performance)

grades = np.where(student_avg >= 90, "A", np.where(student_avg >= 75, "B", np.where(student_avg >= 60, "C", "D")))
print(grades)

#grading
a_count = np.sum(grades == "A")
a_percentage = (a_count / total_students) * 100 
print(f"A Grade : {a_count} students ({a_percentage:.2f}%)")

b_count = np.sum(grades == "B")
b_percentage = (b_count / total_students) * 100
print(f"B Grade : {b_count} students ({b_percentage:.2f}%)")
 
c_count = np.sum(grades == "C")
c_percentage = (c_count / total_students) * 100
print(f"C Grade : {c_count} students ({c_percentage:.2f}%)") 

d_count = np.sum(grades == "D")
d_percentage = (d_count / total_students) * 100 
print(f"D Grade : {d_count} students ({d_percentage:.2f}%)")

#broadcasting
grace_marks = np.array([5,2,3])
updated_scores = data + grace_marks
print("updated scores:",np.clip(updated_scores,0,100))

#after giving grace marks
new_class_avg = np.mean(updated_scores) #new class avg

#new failed students
new_failed_students = np.sum(np.any(updated_scores < 40, axis=1))

total_students = updated_scores.shape[0]

new_pass_percentage = ((total_students - new_failed_students) / total_students) * 100

new_student_avg = np.mean(updated_scores, axis=1) # new student avg
new_grades = np.where(new_student_avg >= 90, "A",np.where(new_student_avg >= 75, "B",np.where(new_student_avg >= 60, "C", "D")))

new_a_grades = np.sum(new_grades == "A") #new A grade

new_failed_students = np.sum(np.any(updated_scores < 40, axis=1)) #new failed students

print("\n===== AFTER GRACE MARKS =====")

print("Class Average      :", round(new_class_avg, 2))
print("Pass Percentage    :", round(new_pass_percentage, 2), "%")
print("A Grade Students   :", new_a_grades)
print("Failed Students    :", new_failed_students)

# ADVANCED INDEXING & SORTING
#  SORT STUDENT AVERAGES


sorted_avg = np.sort(student_avg)

print("\n===== SORTED STUDENT AVERAGES =====")
print("Lowest Average :", sorted_avg[0])
print("Highest Average:", sorted_avg[-1])



# SORT INDICES


sorted_index = np.argsort(student_avg)

print("\n===== SORTED INDICES =====")
print(sorted_index)



#TOP STUDENT USING ARGSORT


top_student = sorted_index[-1]

print("\n===== TOP STUDENT =====")
print("Student Index :", top_student)
print("Average Score :", student_avg[top_student])
print("Grade :", grades[top_student])



# TOP 10 STUDENTS

top10 = sorted_index[-10:]

print("\n===== TOP 10 STUDENTS (Ascending) =====")
print(top10)
print(student_avg[top10])


#TOP 10 RANKING (Descending)


top10 = sorted_index[-10:][::-1]

print("\n===== MERIT LIST =====")

for rank, index in enumerate(top10, start=1):
    print("-" * 40)
    print(f"Rank : {rank}")
    print(f"Student Index : {index}")
    print(f"Average Score : {student_avg[index]:.2f}")
    print(f"Grade : {grades[index]}")



#BOTTOM 10 STUDENTS


bottom10 = sorted_index[:10]

print("\n===== BOTTOM 10 STUDENTS =====")

for rank, index in enumerate(bottom10, start=1):
    print("-" * 40)
    print(f"Rank : {rank}")
    print(f"Student Index : {index}")
    print(f"Average Score : {student_avg[index]:.2f}")
    print(f"Grade : {grades[index]}")



# FANCY INDEXING


print("\n===== SCORES OF TOP 10 STUDENTS =====")
print(data[top10])



#TOP 10 MATH STUDENTS


math_scores = data[:, 0]

math_rank = np.argsort(math_scores)[-10:][::-1]

print("\n===== TOP 10 MATH STUDENTS =====")

for rank, index in enumerate(math_rank, start=1):
    print("-" * 40)
    print(f"Rank : {rank}")
    print(f"Student Index : {index}")
    print(f"Math Score : {math_scores[index]}")



# TOP 10 READING STUDENTS


reading_scores = data[:, 1]

reading_rank = np.argsort(reading_scores)[-10:][::-1]

print("\n===== TOP 10 READING STUDENTS =====")

for rank, index in enumerate(reading_rank, start=1):
    print("-" * 40)
    print(f"Rank : {rank}")
    print(f"Student Index : {index}")
    print(f"Reading Score : {reading_scores[index]}")



#TOP 10 WRITING STUDENTS


writing_scores = data[:, 2]

writing_rank = np.argsort(writing_scores)[-10:][::-1]

print("\n===== TOP 10 WRITING STUDENTS =====")

for rank, index in enumerate(writing_rank, start=1):
    print("-" * 40)
    print(f"Rank : {rank}")
    print(f"Student Index : {index}")
    print(f"Writing Score : {writing_scores[index]}")



# STUDENTS ABOVE 95 AVERAGE


high_achievers = np.where(student_avg > 95)[0]

print("\n===== STUDENTS WITH AVERAGE ABOVE 95 =====")

for index in high_achievers:
    print(f"Student {index} --> Average : {student_avg[index]:.2f}")



#SCHOLARSHIP ELIGIBLE STUDENTS


scholarship = np.where(
    (student_avg >= 90) &
    (np.all(data >= 85, axis=1))
)[0]

print("\n===== SCHOLARSHIP ELIGIBLE STUDENTS =====")

for index in scholarship:
    print("-" * 40)
    print(f"Student Index : {index}")
    print(f"Average : {student_avg[index]:.2f}")
    print(f"Scores : {data[index]}")



#GRADE IMPROVEMENT


improved_students = np.where(grades != new_grades)[0]

print("\n===== GRADE IMPROVEMENTS =====")

for index in improved_students:
    print("-" * 40)
    print(f"Student : {index}")
    print(f"Old Grade : {grades[index]}")
    print(f"New Grade : {new_grades[index]}")



# TOP 5 MOST IMPROVED STUDENTS


improvement = new_student_avg - student_avg

top5_improved = np.argsort(improvement)[-5:][::-1]

print("\n===== TOP 5 MOST IMPROVED STUDENTS =====")

for rank, index in enumerate(top5_improved, start=1):

    print("-" * 40)
    print(f"Rank : {rank}")
    print(f"Student : {index}")
    print(f"Old Average : {student_avg[index]:.2f}")
    print(f"New Average : {new_student_avg[index]:.2f}")
    print(f"Improvement : {improvement[index]:.2f}")



#  MATH IS HIGHEST SUBJECT


math_best = np.where(
    (data[:, 0] >= data[:, 1]) &
    (data[:, 0] >= data[:, 2])
)[0]

print("\n===== STUDENTS WHOSE BEST SUBJECT IS MATH =====")

for index in math_best:
    print("-" * 40)
    print(f"Student : {index}")
    print(f"Scores : {data[index]}")


# ==========================================================
#                 FINAL ANALYSIS REPORT
# ==========================================================

print("\n")
print("=" * 70)
print("           STUDENT PERFORMANCE ANALYSIS REPORT")
print("=" * 70)

# -------------------- DATASET OVERVIEW --------------------

print("\n DATASET OVERVIEW")
print("-" * 70)
print(f"Total Students              : {total_students}")
print(f"Total Subjects              : {data.shape[1]}")
print(f"Dataset Shape               : {data.shape}")

# -------------------- SUBJECT ANALYSIS --------------------

print("\n SUBJECT ANALYSIS")
print("-" * 70)
print(f"Average Math Score          : {subject_avg[0]:.2f}")
print(f"Average Reading Score       : {subject_avg[1]:.2f}")
print(f"Average Writing Score       : {subject_avg[2]:.2f}")

print(f"Highest Math Score          : {subject_max[0]}")
print(f"Highest Reading Score       : {subject_max[1]}")
print(f"Highest Writing Score       : {subject_max[2]}")

print(f"Lowest Math Score           : {subject_min[0]}")
print(f"Lowest Reading Score        : {subject_min[1]}")
print(f"Lowest Writing Score        : {subject_min[2]}")

print(f"Best Performing Subject     : {subjects[np.argmax(subject_avg)]}")
print(f"Weakest Performing Subject  : {subjects[np.argmin(subject_avg)]}")

# -------------------- STUDENT ANALYSIS --------------------

print("\n STUDENT ANALYSIS")
print("-" * 70)

print(f"Top Student Index           : {top_student_index}")
print(f"Top Student Average         : {student_avg[top_student_index]:.2f}")
print(f"Top Student Scores          : {data[top_student_index]}")

print()

print(f"Lowest Student Index        : {lowest_student_index}")
print(f"Lowest Student Average      : {student_avg[lowest_student_index]:.2f}")
print(f"Lowest Student Scores       : {data[lowest_student_index]}")

print()

print(f"Students Above Average      : {students_above_avg}")
print(f"Students Below Average      : {students_below_avg}")

# -------------------- GRADE ANALYSIS --------------------

print("\n GRADE DISTRIBUTION")
print("-" * 70)

print(f"A Grade Students            : {a_count} ({a_percentage:.2f}%)")
print(f"B Grade Students            : {b_count} ({b_percentage:.2f}%)")
print(f"C Grade Students            : {c_count} ({c_percentage:.2f}%)")
print(f"D Grade Students            : {d_count} ({d_percentage:.2f}%)")

# -------------------- PASS / FAIL --------------------

print("\n PASS / FAIL ANALYSIS")
print("-" * 70)

print(f"Passed Students             : {passed_students}")
print(f"Failed Students             : {failed_count}")
print(f"Pass Percentage             : {pass_percentage:.2f}%")

# -------------------- GRACE MARKS --------------------

print("\n GRACE MARKS IMPACT")
print("-" * 70)

print(f"New Class Average           : {new_class_avg:.2f}")
print(f"New Pass Percentage         : {new_pass_percentage:.2f}%")
print(f"New Failed Students         : {new_failed_students}")
print(f"New A Grade Students        : {new_a_grades}")

print()

print(f"Average Improvement         : {(new_class_avg-class_avg):.2f}")
print(f"Pass % Improvement          : {(new_pass_percentage-pass_percentage):.2f}%")
print(f"Additional A Grades         : {new_a_grades-a_count}")
print(f"Reduction in Failures       : {failed_count-new_failed_students}")

# -------------------- MERIT LIST --------------------

print("\n TOP 10 STUDENTS")
print("-" * 70)

for rank, index in enumerate(top10, start=1):
    print(f"{rank:>2}. Student {index:<4} | "
          f"Average : {student_avg[index]:6.2f} | "
          f"Grade : {grades[index]}")

# -------------------- BOTTOM 10 --------------------

print("\n BOTTOM 10 STUDENTS")
print("-" * 70)

for rank, index in enumerate(bottom10, start=1):
    print(f"{rank:>2}. Student {index:<4} | "
          f"Average : {student_avg[index]:6.2f} | "
          f"Grade : {grades[index]}")

# -------------------- SUBJECT TOPPERS --------------------

print("\n SUBJECT-WISE TOPPERS")
print("-" * 70)

print(f"Math Topper Index           : {math_rank[0]} | Score : {math_scores[math_rank[0]]}")
print(f"Reading Topper Index        : {reading_rank[0]} | Score : {reading_scores[reading_rank[0]]}")
print(f"Writing Topper Index        : {writing_rank[0]} | Score : {writing_scores[writing_rank[0]]}")

# -------------------- SCHOLARSHIP --------------------
print("\n SCHOLARSHIP ELIGIBLE STUDENTS")
print("-" * 70)

print(f"Eligible Students           : {len(scholarship)}")

# -------------------- PROJECT SUMMARY --------------------

print("\n PROJECT SUMMARY")
print("-" * 70)
print("✔ Dataset loaded and analysed successfully.")
print("✔ Statistical analysis performed using NumPy.")
print("✔ Student performance evaluated.")
print("✔ Grade distribution calculated.")
print("✔ Pass/Fail statistics generated.")
print("✔ Broadcasting used for grace marks.")
print("✔ Advanced indexing and sorting completed.")
print("✔ Merit list and scholarship analysis generated.")

print("\n" + "=" * 70)
print("          END OF STUDENT PERFORMANCE ANALYSIS")
print("=" * 70)