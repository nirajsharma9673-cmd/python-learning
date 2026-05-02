

# ─────────────────────────────────────────────
# We define a class called Student
# A class is a blueprint for creating objects
# ─────────────────────────────────────────────
class Student:

    # __init__ is the constructor — runs automatically
    # when you create a Student object.
    # We store values in "private" attributes (_name, _marks)
    # The underscore _ is a convention meaning: "don't touch directly"
    def __init__(self, name, marks):
        self._name  = name    # private: stores the actual name
        self._marks = marks   # private: stores the actual marks

    # ─────────────────────────────────────────────
    # GETTER for 'name'
    # @property makes this method behave like an attribute.
    # When you write  student.name  → this method runs.
    # No parentheses needed — Python calls it for you!
    # ─────────────────────────────────────────────
    @property
    def name(self):
        # We can add any logic here before returning
        return self._name

    # ─────────────────────────────────────────────
    # SETTER for 'name'
    # @name.setter runs when you write  student.name = "something"
    # This is where we VALIDATE the value before storing it
    # ─────────────────────────────────────────────
    @name.setter
    def name(self, value):
        if not value.strip():           # .strip() removes spaces
            raise ValueError("Name cannot be empty!")
        self._name = value.strip()      # store clean version

    # ─────────────────────────────────────────────
    # GETTER for 'marks'
    # Reading  student.marks  runs this method
    # ─────────────────────────────────────────────
    @property
    def marks(self):
        return self._marks

    # ─────────────────────────────────────────────
    # SETTER for 'marks'
    # Validates: marks must be between 0 and 100
    # student.marks = 85   → runs this setter
    # ─────────────────────────────────────────────
    @marks.setter
    def marks(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Marks must be between 0 and 100!")
        self._marks = value

    # ─────────────────────────────────────────────
    # COMPUTED PROPERTY — read-only getter (no setter)
    # 'grade' is calculated on the fly from marks.
    # student.grade  → runs this, no value is stored
    # ─────────────────────────────────────────────
    @property
    def grade(self):
        if   self._marks >= 90: return "A+"
        elif self._marks >= 75: return "A"
        elif self._marks >= 60: return "B"
        elif self._marks >= 40: return "C"
        else:                    return "F"

    # ─────────────────────────────────────────────
    # __str__ → what prints when you do print(student)
    # ─────────────────────────────────────────────
    def __str__(self):
        return f"Student: {self._name} | Marks: {self._marks} | Grade: {self.grade}"


# ══════════════════════════════════════════════
# HOW TO USE THE CLASS
# ══════════════════════════════════════════════

# 1. Create a student object (calls __init__)
s = Student("Niraj", 85)

# 2. READ via getter — no () needed, like a normal attribute
print(s.name)    # → Niraj     (getter ran)
print(s.marks)   # → 85        (getter ran)
print(s.grade)   # → A         (computed getter ran)

# 3. UPDATE via setter — just assign, like a normal attribute
s.name  = "Niraj Patil"  # setter validates, then stores
s.marks = 92               # setter validates 0<=92<=100 ✓

# 4. See the result
print(s)         # → Student: Niraj Patil | Marks: 92 | Grade: A+

# 5. Setter REJECTS bad values
s.marks = 150    # → ValueError: Marks must be between 0 and 100!
s.name  = "   "  # → ValueError: Name cannot be empty!
s.grade = 99     # → AttributeError: no setter for grade (read-only!)
