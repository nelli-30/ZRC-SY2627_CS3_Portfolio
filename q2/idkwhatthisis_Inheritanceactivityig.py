# ==========================================
# PARENT: CD (Campus Director)
# ==========================================
class CD:
    def __init__(self, name, office):
        self.__name, self.__office = name, office

    @property
    def name(self): return self.__name
    @name.setter
    def name(self, val): self.__name = val

    @property
    def office(self): return self.__office
    @office.setter
    def office(self, val): self.__office = val

    def display_role(self):
        return f"Campus Director: {self.__name} ({self.__office})"


# ==========================================
# CHILD 1: CID & Its Children / Grandchild
# ==========================================
class CID(CD):
    def __init__(self, name, office, depts, status, progs):
        super().__init__(name, office)  # Inherits from CD
        self.__depts, self.__status, self.__progs = depts, status, progs

    @property
    def depts(self): return self.__depts
    @property
    def status(self): return self.__status
    @property
    def progs(self): return self.__progs

    def oversee(self): return f"CID Head ({self.name}) overseeing {self.__depts} departments."
    def evaluate(self): return f"Evaluating CID academic curriculum."

# CID Child 1
class AcademicDept(CID):
    def __init__(self, *args, majors):
        super().__init__(*args)
        self.__majors = majors

    @property
    def majors(self): return self.__majors
    def list_majors(self): return f"Offers {self.__majors} academic majors."

# CID Grandchild (Child of AcademicDept)
class SpecializedTrack(AcademicDept):
    def __init__(self, *args, track):
        super().__init__(*args)
        self.__track = track

    @property
    def track(self): return self.__track
    def show_track(self): return f"Specialized Track: {self.__track}"

# CID Child 2
class ResearchUnit(CID):
    def __init__(self, *args, grants):
        super().__init__(*args)
        self.__grants = grants

    @property
    def grants(self): return self.__grants
    def show_grants(self): return f"Active research grants: {self.__grants}"

# CID Child 3
class ExtensionService(CID):
    def __init__(self, *args, partners):
        super().__init__(*args)
        self.__partners = partners

    @property
    def partners(self): return self.__partners
    def outreach(self): return f"Community outreach partners: {self.__partners}"


# ==========================================
# CHILD 2: SSD & Its Child
# ==========================================
class SSD(CD):
    def __init__(self, name, office, students, facility):
        super().__init__(name, office)  # Inherits from CD
        self.__students, self.__facility = students, facility

    @property
    def students(self): return self.__students
    @property
    def facility(self): return self.__facility

    def support(self): return f"SSD Head ({self.name}) supporting {self.__students} students."
    def manage(self): return f"Student Facility Status: {self.__facility}"

# SSD Child
class Guidance(SSD):
    def __init__(self, *args, counselor):
        super().__init__(*args)
        self.__counselor = counselor

    @property
    def counselor(self): return self.__counselor
    def session(self): return f"Guidance counselor assigned: {self.__counselor}"


# ==========================================
# DEMONSTRATION
# ==========================================
if __name__ == "__main__":
    # Parent (Campus Director)
    cd = CD("Sir Edman", "CD Office")
    
    # Division Heads (Passing their own names into the inherited __init__)
    cid = CID("Ma'am Raznee", "CID Office", 5, "Accredited", ["STEM"])
    ssd = SSD("Sir Gamil", "Student Center", 450, "Operational")

    # CID Subclasses (Using Ma'am Raznee)
    dept = AcademicDept("Ma'am Raznee", "CID Office", 5, "Accredited", ["STEM"], majors=3)
    track = SpecializedTrack("Ma'am Raznee", "CID Office", 5, "Accredited", ["STEM"], majors=3, track="Computer Science")
    research = ResearchUnit("Ma'am Raznee", "CID Office", 5, "Accredited", ["STEM"], grants=4)
    extension = ExtensionService("Ma'am Raznee", "CID Office", 5, "Accredited", ["STEM"], partners=10)

    # SSD Subclass (Using Sir Gamil)
    guidance = Guidance("Sir Gamil", "Student Center", 450, "Operational", counselor="Guidance Counselor")

    # Outputs
    print(cd.display_role())
    print(cid.oversee())
    print(ssd.support())
    print(dept.list_majors())
    print(track.show_track())
    print(research.show_grants())
    print(extension.outreach())
    print(guidance.session())