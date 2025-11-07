# Activity 10: CIS Major Progress Tracker 💻

## Learning Objectives
- Create a class from scratch with attributes and methods
- Create multiple independent objects (instances) from the same class
- Practice using `__init__` constructor and `self` keyword

## Overview
Build a progress tracker for **CIS students at Allegheny College**! Create a `CISMajor` class to track student name, major, and credits completed.

## Learning Objectives
- Create a class from scratch with attributes and methods
- Understand the relationship between classes and objects
- Create multiple independent objects (instances) from the same class
- Practice using `__init__` constructor and `self` keyword
- Work with instance attributes and methods

## Overview
You are building a progress tracker for **CIS students at Allegheny College**! Each student is pursuing one of four majors: Computer Science, Software Engineering, Data Science, or Informatics. In this activity, you'll create a `CISMajor` class and build multiple student instances to track their academic progress.

## The CIS Major Challenge
Create a student progress tracker that can:
- Track student name, major, and credits completed
- Complete courses and earn credits
- Add projects to portfolio
- Report academic status
- Calculate credits remaining until graduation

## Technical Requirements

### `CISMajor` Class

**Attributes:**
- `name` - Student's name (string)
- `major` - "Computer Science", "Software Engineering", "Data Science", or "Informatics" (string)
- `credits` - Credits completed (int, starts at 0)

**Methods:**

1. **`__init__(self, name, major)`** - Initialize a new CIS student
2. **`complete_course(self, course_name, credits)`** - Add credits and print confirmation
3. **`get_status(self)`** - Return formatted string with name, major, and credits
4. **`credits_to_graduation(self)`** - Return credits remaining (48 total required)

## Example Usage

```python
# Create 3 student instances
maria = CISMajor("Maria Garcia", "Computer Science")
jamal = CISMajor("Jamal Washington", "Software Engineering")
priya = CISMajor("Priya Patel", "Data Science")

# Check initial status
print(maria.get_status())
print(jamal.get_status())

# Complete courses
maria.complete_course("CMPSC 100", 4)
maria.complete_course("CMPSC 101", 4)
jamal.complete_course("CMPSC 100", 4)

# Check graduation progress
print(f"{maria.name} needs {maria.credits_to_graduation()} more credits")
print(f"{jamal.name} needs {jamal.credits_to_graduation()} more credits")
```

**Expected Output:**
```
🎓 Maria Garcia | Major: Computer Science | Credits: 0
🎓 Jamal Washington | Major: Software Engineering | Credits: 0
✅ Maria Garcia completed CMPSC 100 (+4 credits, total: 4)
✅ Maria Garcia completed CMPSC 101 (+4 credits, total: 8)
✅ Jamal Washington completed CMPSC 100 (+4 credits, total: 4)
Maria Garcia needs 40 more credits
Jamal Washington needs 44 more credits
```

**Key Concepts:**
- Use `self.name`, `self.major`, `self.credits` to access instance attributes
- Each student object is independent (maria's credits ≠ jamal's credits)
- Methods need `self` as first parameter

### Key OOP Concepts to Remember

1. **`self` keyword** - Refers to the current instance
   - Use `self.name` to access instance's name
   - Use `self.credits` to access instance's credits

2. **Instance independence** - Each object has its own data
   - `maria.credits` is separate from `jamal.credits`
   - Changing one student doesn't affect others

3. **Methods vs. Functions** - Methods are functions inside a class
   - Methods always have `self` as first parameter
   - Call methods on objects: `maria.complete_course(...)`

4. **Encapsulation** - Data and methods bundled together
   - Credits and projects managed through class methods
   - Can't accidentally set invalid data values

## What to Submit

- `src/main.py` - Your complete CISMajor class with all methods

## Grading Rubric

This activity is assessed on a **pass/fail basis**:

- **1 point**: Class implemented with most required methods, 3+ working instances demonstrated
- **0 points**: Class less than 50% complete

## Bonus Challenges (If You Finish Early)

1. **GPA tracking** - Add a `gpa` attribute and method to update it
2. **Course catalog** - Create a dictionary of actual CIS courses with their credit values
3. **Graduation check** - Method that returns `True` if student has >= 48 credits
4. **Project showcase** - Method that prints all projects in a formatted list
5. **Major requirements** - Track foundation, core, and elective courses separately
